import os
import asyncio
import edge_tts
import imageio_ffmpeg
import subprocess

SCENES = [
    {
        "id": "scene1_problem",
        "title": "The Arctic Information Desert",
        "text": "In sub-zero Oulu, over 5,000 international students and tech engineers live in an information desert. When blizzards freeze transit or alarms sound, they cannot read Finnish news. Rumors erupt on WhatsApp and Jodel, while standard machine translation fails on civic terms like Pääkallokeli and Baana."
    },
    {
        "id": "scene2_solution",
        "title": "Introducing Kaleva Tasku",
        "text": "Introducing Kaleva Tasku: a community-driven, agentic civic newsroom connecting 125 years of Kaleva's trusted journalism with visual-first ergonomics. Our Dual-Engine model delivers instant situational awareness on mobile cards, while one click opens the classic 1899 broadsheet with full journalistic depth."
    },
    {
        "id": "scene3_demo",
        "title": "Live Product Walkthrough",
        "text": "Here is the live app in action. Every micro-card features the verified orange masthead and a zero-translation situation diagram: incident on the left, salad-green arrow, and clear actionable solution on the right, understood in under two seconds. At minus twenty, the 30-second Korva audio stream briefs users directly in their earbuds so gloves stay on. And one tap on the headline opens the deep, Council for Mass Media certified broadsheet story."
    },
    {
        "id": "scene4_agents",
        "title": "3-Agent Pipeline & JSN Ethics",
        "text": "Powering the newsroom is an autonomous three-agent pipeline. Agent Ingest monitors civic feeds under strict GDPR compliance. Agent Synthesizer distills stories into vector diagrams and audio scripts. And Agent Ethics Auditor runs mathematical verification against official police and rescue sources. A desk editor in the loop maintains one-click cockpit sovereignty under Finland's JSN ethics code."
    },
    {
        "id": "scene5_business",
        "title": "B2B Business Model & Oulu 2026",
        "text": "Best of all, we never charge students. Instead, institutions with a duty of care—the University of Oulu, Nokia, and the Oulu 2026 Foundation—fund the service, generating 114,000 euros in annual revenue at an 84 percent gross margin. Ready for Oulu 2026: Kaleva Tasku makes Northern Finland safe, warm, and navigable for everyone."
    }
]

async def generate_scene_audio():
    os.makedirs("audio", exist_ok=True)
    voice = "en-US-ChristopherNeural"
    
    total_duration = 0.0
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    
    for scene in SCENES:
        out_path = f"audio/{scene['id']}.mp3"
        comm = edge_tts.Communicate(scene['text'], voice, rate="+6%")
        await comm.save(out_path)
        
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
