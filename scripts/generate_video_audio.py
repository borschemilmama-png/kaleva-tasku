import os
import asyncio
import edge_tts
import imageio_ffmpeg
import subprocess

SCENES = [
    {
        "id": "scene1_problem",
        "title": "The Arctic Information Desert",
        "text": "In Arctic Oulu, over 5,000 international students and tech workers face dangerous isolation during crises. When blizzards freeze transit or alarms sound, they cannot read Finnish news. Rumors and panic erupt on WhatsApp and Jodel, while standard machine translation fails to explain Finnish civic laws."
    },
    {
        "id": "scene2_solution",
        "title": "Introducing Kaleva Tasku",
        "text": "Enter Kaleva Tasku: a community-driven, agentic newsroom for multilingual residents, connecting 125 years of Kaleva's trusted journalism with visual-first ergonomics. Our Dual-Engine format delivers fast, swipeable cards for mobile readers, while one click opens the classic 1899 broadsheet with full journalistic depth."
    },
    {
        "id": "scene3_demo",
        "title": "Live Product Walkthrough",
        "text": "Each story features our Zero-Translation Situation Diagram: problem on the left, clear bypass route on the right, understood in two seconds. Key civic terms like PSOAS, Kela, and Baana open interactive drawers explaining legal protections and tenant advice. Every card concludes with direct action: live bus navigation, safety alerts, or event passes."
    },
    {
        "id": "scene4_agents",
        "title": "3-Agent Pipeline & JSN Ethics",
        "text": "Powering the newsroom is an autonomous three-agent pipeline. Agent Radar monitors open civic data and community tips under strict GDPR compliance. Agent Ethics Auditor runs mathematical verification against official databases. And our Cultural Decoder contextualizes alerts to prevent panic. An editor-in-the-loop retains full cockpit oversight under Finland's JSN ethics code."
    },
    {
        "id": "scene5_business",
        "title": "Arctic Voice & Business Model",
        "text": "For minus twenty conditions, our 30-second Korva voice stream briefs users without taking off winter gloves. And we never charge students. Instead, institutions like the University of Oulu, Nokia, and Oulu 2026 fund the service, generating 114,000 euros in annual revenue at an 84 percent margin. Kaleva Tasku: verified civic news for everyone."
    }
]

async def generate_scene_audio():
    os.makedirs("audio", exist_ok=True)
    voice = "en-US-ChristopherNeural"
    
    total_duration = 0.0
    for scene in SCENES:
        out_path = f"audio/{scene['id']}.mp3"
        comm = edge_tts.Communicate(scene['text'], voice, rate="+7%")
        await comm.save(out_path)
        
        ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
        cmd = [ffmpeg_exe, "-i", out_path]
        res = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        for line in res.stderr.splitlines():
            if "Duration:" in line:
                dur_str = line.split("Duration:")[1].split(",")[0].strip()
                h, m, s = dur_str.split(":")
                dur_sec = float(h)*3600 + float(m)*60 + float(s)
                scene["duration"] = dur_sec
                total_duration += dur_sec
                print(f"{scene['id']}: {dur_sec:.2f}s")
                break
                
    print(f"\nTOTAL NARRATION DURATION: {total_duration:.2f}s ({total_duration/60:.2f} minutes)")

if __name__ == "__main__":
    asyncio.run(generate_scene_audio())
