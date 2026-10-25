import os
import time
import glob
import shutil
import threading
import http.server
import socketserver
import subprocess
import imageio_ffmpeg
from playwright.sync_api import sync_playwright

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='dist', **kwargs)
    def log_message(self, format, *args):
        pass

def get_audio_duration(ffmpeg_exe, audio_path):
    cmd = [ffmpeg_exe, "-i", audio_path]
    res = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    for line in res.stderr.splitlines():
        if "Duration:" in line:
            dur_str = line.split("Duration:")[1].split(",")[0].strip()
            h, m, s = dur_str.split(":")
            return float(h)*3600 + float(m)*60 + float(s)
    return 20.0

def record_scene(p, chrome_path, url, duration, out_dir, interaction_fn=None):
    os.makedirs(out_dir, exist_ok=True)
    # clean dir
    for f in glob.glob(f"{out_dir}/*"):
        os.remove(f)

    browser = p.chromium.launch(executable_path=chrome_path)
    context = browser.new_context(
        record_video_dir=out_dir,
        record_video_size={"width": 1920, "height": 1080},
        viewport={"width": 1920, "height": 1080}
    )
    page = context.new_page()
    page.goto(url)
    
    start_time = time.time()
    if interaction_fn:
        interaction_fn(page, duration)
    else:
        remaining = duration - (time.time() - start_time)
        if remaining > 0:
            time.sleep(remaining)

    page.close()
    context.close()
    browser.close()

    # Find the recorded webm
    webms = glob.glob(f"{out_dir}/*.webm")
    if not webms:
        raise Exception(f"No webm found in {out_dir}")
    return webms[0]

def scene3_interaction(page, duration):
    start_t = time.time()
    page.wait_for_timeout(2000)

    # Click action button
    action_btn = page.query_selector('button:has-text("Avaa kiertotie")')
    if not action_btn:
        action_btn = page.query_selector('button.bg-\\[\\#002855\\]')
    if action_btn:
        action_btn.click()
        page.wait_for_timeout(2500)
        # Close modal
        close_btn = page.query_selector('button:has-text("Selvä, kiitos!")')
        if close_btn:
            close_btn.click()
            page.wait_for_timeout(1000)

    # Click next story
    next_btn = page.query_selector('button[aria-label="Seuraava uutinen"]')
    if next_btn:
        next_btn.click()
        page.wait_for_timeout(2500)

    # Click headline to open broadsheet
    headline = page.query_selector('h2')
    if headline:
        headline.click()
        page.wait_for_timeout(3000)
        # Scroll modal
        page.evaluate("() => window.scrollBy(0, 300)")
        page.wait_for_timeout(2000)
        # Close broadsheet
        close_bs = page.query_selector('button[aria-label="Sulje"]')
        if not close_bs:
            close_bs = page.query_selector('button:has(.lucide-x)')
        if close_bs:
            close_bs.click()
            page.wait_for_timeout(1200)

    # Click next story again
    if next_btn:
        next_btn.click()
        page.wait_for_timeout(2000)

    # Toggle audio
    audio_btn = page.query_selector('button:has-text("Kuuntele")')
    if audio_btn:
        audio_btn.click()
        page.wait_for_timeout(2000)

    # Wait out remaining time
    elapsed = time.time() - start_t
    if duration > elapsed:
        time.sleep(duration - elapsed)

def main():
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

    # Start local server on 8998 for dist
    server = socketserver.TCPServer(('127.0.0.1', 8998), QuietHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print("Local web server active on 8998")

    scene_configs = [
        {
            "id": "scene1",
            "url": f"file:///{os.path.abspath('video_scenes/scene1.html')}",
            "audio": "audio/scene1_problem.mp3",
            "fn": None
        },
        {
            "id": "scene2",
            "url": f"file:///{os.path.abspath('video_scenes/scene2.html')}",
            "audio": "audio/scene2_solution.mp3",
            "fn": None
        },
        {
            "id": "scene3",
            "url": "http://127.0.0.1:8998",
            "audio": "audio/scene3_demo.mp3",
            "fn": scene3_interaction
        },
        {
            "id": "scene4",
            "url": f"file:///{os.path.abspath('video_scenes/scene4.html')}",
            "audio": "audio/scene4_agents.mp3",
            "fn": None
        },
        {
            "id": "scene5",
            "url": f"file:///{os.path.abspath('video_scenes/scene5.html')}",
            "audio": "audio/scene5_business.mp3",
            "fn": None
        }
    ]

    os.makedirs("video_parts", exist_ok=True)
    muxed_parts = []

    with sync_playwright() as p:
        for idx, sc in enumerate(scene_configs, 1):
            dur = get_audio_duration(ffmpeg_exe, sc["audio"])
            print(f"\n--- Recording Scene {idx}: {sc['id']} (Duration: {dur:.2f}s) ---")
            raw_webm = record_scene(
                p, chrome_path, sc["url"], dur + 0.3, f"raw_scene_{idx}", sc["fn"]
            )
            print(f"Recorded raw video: {raw_webm}")

            # Mux with audio using ffmpeg
            muxed_mp4 = f"video_parts/scene{idx}_muxed.mp4"
            print(f"Muxing {sc['id']} to {muxed_mp4}...")
            mux_cmd = [
                ffmpeg_exe, "-y",
                "-i", raw_webm,
                "-i", sc["audio"],
                "-c:v", "libx264",
                "-preset", "faster",
                "-crf", "21",
                "-pix_fmt", "yuv420p",
                "-c:a", "aac",
                "-b:a", "192k",
                "-shortest",
                muxed_mp4
            ]
            subprocess.run(mux_cmd, check=True)
            muxed_parts.append(muxed_mp4)

    server.shutdown()

    # Concatenate all scenes into final video
    concat_txt_path = "video_parts/concat_list.txt"
    with open(concat_txt_path, "w", encoding="utf-8") as f:
        for part in muxed_parts:
            # ffmpeg concat file path format
            abs_p = os.path.abspath(part).replace("\\", "/")
            f.write(f"file '{abs_p}'\n")

    final_output = "Kaleva_Tasku_Demo_Video.mp4"
    print(f"\nConcatenating all {len(muxed_parts)} scenes into {final_output}...")
    concat_cmd = [
        ffmpeg_exe, "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", concat_txt_path,
        "-c", "copy",
        final_output
    ]
    subprocess.run(concat_cmd, check=True)

    final_dur = get_audio_duration(ffmpeg_exe, final_output)
    final_size_mb = os.path.getsize(final_output) / (1024 * 1024)
    print(f"\n=======================================================")
    print(f"DEMO VIDEO GENERATED: {final_output}")
    print(f"Total Duration: {final_dur:.2f} seconds ({final_dur/60:.2f} minutes)")
    print(f"File Size: {final_size_mb:.2f} MB")
    print(f"Resolution: 1920x1080 Full HD with AAC Audio")
    print(f"=======================================================")

if __name__ == '__main__':
    main()
