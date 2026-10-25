import os

def create_video_html_scenes():
    os.makedirs("video_scenes", exist_ok=True)

    # Scene 1
    scene1_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=Cinzel:wght@700&display=swap');
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1920px; height: 1080px; overflow: hidden;
    background: radial-gradient(circle at 50% 30%, #001f3f 0%, #000c1a 100%);
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: white; padding: 70px 100px;
    display: flex; flex-direction: column; justify-content: space-between;
  }
  .header { display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid rgba(255,255,255,0.15); padding-bottom: 25px; }
  .logo { font-family: 'Cinzel', serif; font-size: 32px; letter-spacing: 4px; color: #38bdf8; font-weight: 700; }
  .badge { background: #c8102e; color: white; padding: 8px 18px; border-radius: 9999px; font-size: 14px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; }
  .title-area { margin-top: 30px; }
  .tagline { color: #38bdf8; font-size: 18px; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 12px; }
  h1 { font-size: 58px; font-weight: 800; line-height: 1.15; max-width: 1400px; }
  p.sub { font-size: 24px; color: #94a3b8; margin-top: 15px; max-width: 1200px; line-height: 1.4; }
  
  .cards-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 35px; margin: 40px 0; }
  .pain-card {
    background: rgba(255,255,255,0.05); border: 1.5px solid rgba(239, 68, 68, 0.4);
    border-radius: 24px; padding: 36px; backdrop-filter: blur(10px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
  }
  .card-icon { font-size: 44px; margin-bottom: 18px; }
  .card-title { font-size: 24px; font-weight: 700; color: #fca5a5; margin-bottom: 12px; }
  .card-desc { font-size: 18px; color: #cbd5e1; line-height: 1.5; }
  
  .footer-strip {
    background: rgba(0, 40, 85, 0.6); border: 1px solid rgba(56, 189, 248, 0.3);
    border-radius: 16px; padding: 18px 30px; display: flex; justify-content: space-between; align-items: center;
    font-size: 16px; color: #93c5fd; font-weight: 600;
  }
</style>
</head>
<body>
  <div class="header">
    <div style="display: flex; align-items: center; gap: 20px;">
      <div class="logo">KALEVA MEDIA</div>
      <div class="badge">JunctionX Oulu 2026</div>
    </div>
    <div style="font-size: 18px; color: #cbd5e1; font-weight: 600;">Challenge 2: News for Everyone</div>
  </div>

  <div class="title-area">
    <div class="tagline">The Arctic Information Desert</div>
    <h1>5,000+ International Residents Left in the Dark</h1>
    <p class="sub">Students, researchers, and Nokia engineers in Oulu are completely isolated from vital local news when Arctic crises strike.</p>
  </div>

  <div class="cards-grid">
    <div class="pain-card">
      <div class="card-icon">❄️ 🚌</div>
      <div class="card-title">1. Arctic Transit Crises</div>
      <div class="card-desc">At −25°C, transit delays threaten physical safety. Foreign residents cannot read Finnish alert broadsheets to know where to find shelter or replacement buses.</div>
    </div>

    <div class="pain-card">
      <div class="card-icon">📱 ⚠️</div>
      <div class="card-title">2. WhatsApp & Jodel Panic</div>
      <div class="card-desc">When emergency sirens echo in the city center, newcomers flock to anonymous message boards. Dangerous rumors and false alarms spread in minutes.</div>
    </div>

    <div class="pain-card">
      <div class="card-icon">🌐 ❌</div>
      <div class="card-title">3. Raw Translation Fails</div>
      <div class="card-desc">Google Translate provides word-for-word translation, but misses critical Finnish institutional context, statutory rental laws, and emergency protocols.</div>
    </div>
  </div>

  <div class="footer-strip">
    <div>⚠️ Critical Problem: Need real-time, verified situational awareness without requiring Finnish fluency.</div>
    <div style="color: #38bdf8; font-weight: 700;">Kaleva Tasku Solution ➔</div>
  </div>
</body>
</html>
"""

    # Scene 2
    scene2_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=Cinzel:wght@700&display=swap');
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1920px; height: 1080px; overflow: hidden;
    background: linear-gradient(135deg, #001833 0%, #002855 60%, #003a7a 100%);
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: white; padding: 70px 100px;
    display: flex; flex-direction: column; justify-content: space-between;
  }
  .header { display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid rgba(255,255,255,0.15); padding-bottom: 25px; }
  .logo { font-family: 'Cinzel', serif; font-size: 32px; letter-spacing: 4px; color: white; font-weight: 700; }
  .badge { background: #38bdf8; color: #001833; padding: 8px 18px; border-radius: 9999px; font-size: 14px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; }
  
  .title-area { margin-top: 20px; }
  .tagline { color: #38bdf8; font-size: 18px; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 10px; }
  h1 { font-size: 64px; font-weight: 800; line-height: 1.15; }
  p.sub { font-size: 24px; color: #cbd5e1; margin-top: 12px; max-width: 1300px; line-height: 1.4; }

  .dual-engine-box { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; margin: 35px 0; }
  .engine-card {
    background: rgba(255,255,255,0.07); border: 2px solid rgba(255,255,255,0.15);
    border-radius: 28px; padding: 40px; backdrop-filter: blur(12px);
    box-shadow: 0 15px 35px rgba(0,0,0,0.3); position: relative;
  }
  .engine-highlight {
    border-color: #38bdf8; background: rgba(56, 189, 248, 0.1);
  }
  .engine-tag {
    display: inline-block; padding: 6px 16px; border-radius: 9999px; font-size: 13px; font-weight: 800;
    text-transform: uppercase; letter-spacing: 1px; margin-bottom: 20px;
  }
  .tag-blue { background: #38bdf8; color: #001833; }
  .tag-gold { background: #f59e0b; color: #000; }
  .engine-title { font-size: 32px; font-weight: 800; margin-bottom: 14px; }
  .engine-desc { font-size: 18px; color: #e2e8f0; line-height: 1.6; }

  .footer-stats {
    display: flex; justify-content: space-around; background: rgba(0,0,0,0.3); border-radius: 20px;
    padding: 20px; border: 1px solid rgba(255,255,255,0.1);
  }
  .stat-item { text-align: center; }
  .stat-num { font-size: 36px; font-weight: 800; color: #38bdf8; }
  .stat-label { font-size: 14px; color: #94a3b8; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; }
</style>
</head>
<body>
  <div class="header">
    <div style="display: flex; align-items: center; gap: 20px;">
      <div class="logo">KALEVA</div>
      <div style="font-size: 26px; font-weight: 800; color: #f87171;">TASKU</div>
    </div>
    <div class="badge">The Innovation Solution</div>
  </div>

  <div class="title-area">
    <div class="tagline">The Dual-Engine Media Innovation</div>
    <h1>Kaleva Tasku: Visual News & Civic Decoder</h1>
    <p class="sub">Uniting 125 years of Nordic journalistic authority with zero-translation situational ergonomics for smartphones.</p>
  </div>

  <div class="dual-engine-box">
    <div class="engine-card engine-highlight">
      <span class="engine-tag tag-blue">Engine 1 • Mobile Generation</span>
      <h2 class="engine-title">📱 Tasku Pocket Cards</h2>
      <p class="engine-desc">
        Fast, swipeable mobile card deck built for Gen Z, expats, and students. Instant ISO situation pictograms, interactive civic glossary drawers, and direct 1-tap solution actions.
      </p>
    </div>

    <div class="engine-card">
      <span class="engine-tag tag-gold">Engine 2 • 125-Year Tradition</span>
      <h2 class="engine-title">🗞️ Broadsheet 1899</h2>
      <p class="engine-desc">
        One tap expands any card into the authentic multi-column newspaper layout with deep investigative reporting, verified journalist bylines, and the official JSN ethics accreditation stamp.
      </p>
    </div>
  </div>

  <div class="footer-stats">
    <div class="stat-item">
      <div class="stat-num">&lt; 2 Seconds</div>
      <div class="stat-label">Comprehension Time</div>
    </div>
    <div class="stat-item">
      <div class="stat-num">100% Verified</div>
      <div class="stat-label">Council for Mass Media (JSN)</div>
    </div>
    <div class="stat-item">
      <div class="stat-num">Dual-Engine</div>
      <div class="stat-label">Never Compromises Editorial Depth</div>
    </div>
  </div>
</body>
</html>
"""

    # Scene 4
    scene4_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=Cinzel:wght@700&display=swap');
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1920px; height: 1080px; overflow: hidden;
    background: #0f172a;
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: white; padding: 60px 100px;
    display: flex; flex-direction: column; justify-content: space-between;
  }
  .header { display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid rgba(255,255,255,0.15); padding-bottom: 20px; }
  .logo { font-family: 'Cinzel', serif; font-size: 30px; letter-spacing: 4px; color: #38bdf8; font-weight: 700; }
  .badge { background: #10b981; color: #064e3b; padding: 6px 16px; border-radius: 9999px; font-size: 13px; font-weight: 800; text-transform: uppercase; }

  .title-area { margin-top: 15px; }
  .tagline { color: #38bdf8; font-size: 16px; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; }
  h1 { font-size: 52px; font-weight: 800; line-height: 1.15; margin-top: 8px; }
  p.sub { font-size: 22px; color: #94a3b8; margin-top: 8px; }

  .pipeline { display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; margin: 30px 0; }
  .agent-card {
    background: #1e293b; border: 2px solid #334155; border-radius: 24px; padding: 32px;
    position: relative; box-shadow: 0 10px 25px rgba(0,0,0,0.3);
  }
  .agent-badge {
    background: #0284c7; color: white; padding: 4px 12px; border-radius: 9999px;
    font-size: 12px; font-weight: 800; text-transform: uppercase; margin-bottom: 16px; display: inline-block;
  }
  .agent-card h3 { font-size: 26px; font-weight: 800; margin-bottom: 12px; color: #f8fafc; }
  .agent-card p { font-size: 16px; color: #cbd5e1; line-height: 1.6; }
  .trust-math {
    background: #0f172a; border-radius: 12px; padding: 14px; margin-top: 14px; font-family: monospace; font-size: 14px; color: #38bdf8;
  }

  .cockpit-bar {
    background: linear-gradient(90deg, #064e3b 0%, #065f46 100%);
    border: 2px solid #10b981; border-radius: 20px; padding: 22px 36px;
    display: flex; justify-content: space-between; align-items: center;
  }
  .cockpit-title { font-size: 22px; font-weight: 800; color: #ecfdf5; }
  .cockpit-desc { font-size: 15px; color: #a7f3d0; margin-top: 4px; }
</style>
</head>
<body>
  <div class="header">
    <div style="display: flex; align-items: center; gap: 20px;">
      <div class="logo">KALEVA</div>
      <div style="font-size: 24px; font-weight: 800; color: #38bdf8;">VOX NEWSROOM</div>
    </div>
    <div class="badge">Autonomous 3-Agent Architecture</div>
  </div>

  <div class="title-area">
    <div class="tagline">Editorial Ethics & Verification</div>
    <h1>The 3-Agent Pipeline + Human Cockpit</h1>
    <p class="sub">Automating speed and verification while strictly upholding Finland's JSN Council for Mass Media ethics.</p>
  </div>

  <div class="pipeline">
    <div class="agent-card">
      <span class="agent-badge">Agent 1 • Radar</span>
      <h3>Tutkija (Investigator)</h3>
      <p>Monitors civic feeds (api.ouka.fi, Fintraffic, RSS, community tips). Automatically strips personal data for GDPR compliance and geo-tags events to Oulu districts.</p>
      <div class="trust-math">✓ GDPR Scrubbing<br>✓ Geo-District Clustering</div>
    </div>

    <div class="agent-card" style="border-color: #38bdf8;">
      <span class="agent-badge" style="background: #38bdf8; color: #001833;">Agent 2 • Ethics</span>
      <h3>JSN Auditor (Math of Trust)</h3>
      <p>Evaluates raw tips with open, mathematical verification rules before passing to the news desk:</p>
      <div class="trust-math">
        +40% Official 112/Rescue match<br>
        +35% 3 Geotagged witnesses<br>
        −15% Anonymous source penalty
      </div>
    </div>

    <div class="agent-card">
      <span class="agent-badge">Agent 3 • Voice</span>
      <h3>Cultural Decoder</h3>
      <p>Translates cultural context to eliminate panic. Explains why 3 fire trucks for burnt bakery smoke is standard Finnish building safety law, not an emergency crisis.</p>
      <div class="trust-math">✓ Selkosuomi & English<br>✓ Panic Mitigation</div>
    </div>
  </div>

  <div class="cockpit-bar">
    <div>
      <div class="cockpit-title">🛡️ Human-in-the-Loop Editorial Cockpit</div>
      <div class="cockpit-desc">No story publishes autonomously. Kaleva's editor maintains final sign-off with 1-click verification conforming to JSN § 10 & § 20.</div>
    </div>
    <div style="background: #ffffff; color: #064e3b; font-weight: 800; padding: 10px 22px; border-radius: 9999px; font-size: 14px;">
      100% JSN § 10 Verified
    </div>
  </div>
</body>
</html>
"""

    # Scene 5
    scene5_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=Cinzel:wght@700&display=swap');
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1920px; height: 1080px; overflow: hidden;
    background: radial-gradient(circle at 50% 30%, #002244 0%, #001122 100%);
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: white; padding: 60px 100px;
    display: flex; flex-direction: column; justify-content: space-between;
  }
  .header { display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid rgba(255,255,255,0.15); padding-bottom: 20px; }
  .logo { font-family: 'Cinzel', serif; font-size: 30px; letter-spacing: 4px; color: #38bdf8; font-weight: 700; }
  .badge { background: #38bdf8; color: #001833; padding: 6px 16px; border-radius: 9999px; font-size: 13px; font-weight: 800; text-transform: uppercase; }

  .title-area { margin-top: 15px; }
  .tagline { color: #38bdf8; font-size: 16px; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; }
  h1 { font-size: 52px; font-weight: 800; line-height: 1.15; margin-top: 8px; }
  p.sub { font-size: 22px; color: #cbd5e1; margin-top: 8px; }

  .grid-content { display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 40px; margin: 30px 0; align-items: center; }
  
  table.biz-table {
    width: 100%; border-collapse: collapse; background: rgba(255,255,255,0.06);
    border-radius: 20px; overflow: hidden; border: 1.5px solid rgba(255,255,255,0.15);
  }
  table.biz-table th { background: #002855; color: white; padding: 16px 20px; text-align: left; font-size: 16px; }
  table.biz-table td { padding: 16px 20px; border-bottom: 1px solid rgba(255,255,255,0.08); font-size: 16px; color: #e2e8f0; }
  .price { font-weight: 800; color: #38bdf8; }

  .metrics-column { display: flex; flex-direction: column; gap: 20px; }
  .metric-card {
    background: rgba(255,255,255,0.06); border: 2px solid rgba(56, 189, 248, 0.4);
    border-radius: 20px; padding: 26px; text-align: center;
  }
  .m-val { font-size: 46px; font-weight: 800; color: #38bdf8; }
  .m-lbl { font-size: 14px; text-transform: uppercase; letter-spacing: 1px; color: #94a3b8; font-weight: 700; margin-top: 4px; }

  .final-cta {
    background: #002855; border: 2px solid #38bdf8; border-radius: 20px;
    padding: 24px 36px; display: flex; justify-content: space-between; align-items: center;
  }
  .final-title { font-size: 26px; font-weight: 800; color: white; }
  .final-meta { font-size: 16px; color: #93c5fd; }
</style>
</head>
<body>
  <div class="header">
    <div style="display: flex; align-items: center; gap: 20px;">
      <div class="logo">KALEVA</div>
      <div style="font-size: 24px; font-weight: 800; color: #38bdf8;">TASKU</div>
    </div>
    <div class="badge">Commercial Sustainability & Arctic Voice</div>
  </div>

  <div class="title-area">
    <div class="tagline">B2B Institutional Model & Arctic Voice</div>
    <h1>Sustainable Impact for Oulu 2026</h1>
    <p class="sub">Students never pay. Institutions dependent on international safety license Kaleva Tasku.</p>
  </div>

  <div class="grid-content">
    <table class="biz-table">
      <thead>
        <tr>
          <th>Institutional Partner</th>
          <th>Annual ARR</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>University of Oulu & OAMK</strong> (Student Retention & Safety)</td>
          <td class="price">€35 000</td>
        </tr>
        <tr>
          <td><strong>Nokia & ICT Corporates</strong> (Slack/Teams Expat Onboarding)</td>
          <td class="price">€25 000</td>
        </tr>
        <tr>
          <td><strong>Oulu 2026 Foundation</strong> (European Capital of Culture 300k Visitors)</td>
          <td class="price">€40 000</td>
        </tr>
        <tr>
          <td><strong>Lapland Tourism Consortia</strong> (Seasonal Worker Protection)</td>
          <td class="price">€14 000</td>
        </tr>
        <tr style="background: rgba(56, 189, 248, 0.15); font-weight: 800;">
          <td>TOTAL ANNUAL REVENUE</td>
          <td style="color: #38bdf8; font-size: 20px;">€114 000 / yr</td>
        </tr>
      </tbody>
    </table>

    <div class="metrics-column">
      <div class="metric-card">
        <div class="m-val">€18 240</div>
        <div class="m-lbl">Lean Annual Operating Cost</div>
      </div>
      <div class="metric-card" style="border-color: #10b981; background: rgba(16, 185, 129, 0.1);">
        <div class="m-val" style="color: #34d399;">84.0%</div>
        <div class="m-lbl" style="color: #6ee7b7;">Gross Profit Margin</div>
      </div>
    </div>
  </div>

  <div class="final-cta">
    <div>
      <div class="final-title">Kaleva Tasku: Verified Civic News for Everyone</div>
      <div class="final-meta">JunctionX Oulu 2026 • Team: Oksana & Vinod • Ready for Oulu 2026</div>
    </div>
    <div style="background: #38bdf8; color: #001833; font-weight: 800; padding: 12px 28px; border-radius: 9999px; font-size: 16px;">
      Empowering the North ❄️
    </div>
  </div>
</body>
</html>
"""

    with open("video_scenes/scene1.html", "w", encoding="utf-8") as f:
        f.write(scene1_html)
    with open("video_scenes/scene2.html", "w", encoding="utf-8") as f:
        f.write(scene2_html)
    with open("video_scenes/scene4.html", "w", encoding="utf-8") as f:
        f.write(scene4_html)
    with open("video_scenes/scene5.html", "w", encoding="utf-8") as f:
        f.write(scene5_html)

    print("HTML scenes created successfully in video_scenes/")

if __name__ == '__main__':
    create_video_html_scenes()
