import os
import base64
from playwright.sync_api import sync_playwright

def get_base64_image(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
            return f"data:image/png;base64,{encoded}"
    return ""

def create_presentation():
    chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    
    app_main_b64 = get_base64_image("screenshots/app_main.png")
    broadsheet_b64 = get_base64_image("screenshots/broadsheet_view.png")
    mobile_card_b64 = get_base64_image("screenshots/mobile_card_1.png")

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Cinzel:wght@700&family=Playfair+Display:ital,wght@0,700;1,400&display=swap');

  @page {{
    size: 1920px 1080px;
    margin: 0;
  }}

  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}

  body {{
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    background-color: #0b111e;
    color: #0f172a;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }}

  .slide {{
    width: 1920px;
    height: 1080px;
    position: relative;
    page-break-after: always;
    overflow: hidden;
    background: #f7f5f0;
    padding: 60px 80px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}

  /* Top Navigation Bar on Slides */
  .slide-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid #e2ded5;
    padding-bottom: 20px;
  }}

  .brand-group {{
    display: flex;
    align-items: center;
    gap: 16px;
  }}

  .kaleva-logo {{
    font-family: 'Cinzel', serif;
    font-size: 28px;
    font-weight: 700;
    letter-spacing: 3px;
    color: #002855;
  }}

  .badge-tag {{
    background: #002855;
    color: white;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1px;
    padding: 6px 14px;
    border-radius: 9999px;
    text-transform: uppercase;
  }}

  .badge-red {{
    background: #c8102e;
    color: white;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1px;
    padding: 6px 14px;
    border-radius: 9999px;
    text-transform: uppercase;
  }}

  .badge-outline {{
    border: 1.5px solid #002855;
    color: #002855;
    font-size: 13px;
    font-weight: 700;
    padding: 5px 12px;
    border-radius: 9999px;
  }}

  .header-meta {{
    font-size: 15px;
    font-weight: 600;
    color: #64748b;
  }}

  /* Slide Body */
  .slide-body {{
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    margin-top: 30px;
  }}

  .slide-title-block {{
    margin-bottom: 30px;
  }}

  .slide-title-block h1 {{
    font-size: 46px;
    font-weight: 800;
    color: #002855;
    line-height: 1.15;
    letter-spacing: -0.5px;
  }}

  .slide-title-block p {{
    font-size: 20px;
    color: #475569;
    font-weight: 500;
    margin-top: 8px;
  }}

  /* Slide Footer */
  .slide-footer {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1.5px solid #e2ded5;
    padding-top: 18px;
    font-size: 14px;
    color: #64748b;
    font-weight: 600;
  }}

  /* Grid Layouts */
  .grid-3 {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 28px;
  }}

  .grid-2 {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 36px;
  }}

  .grid-2-custom {{
    display: grid;
    grid-template-columns: 1.15fr 0.85fr;
    gap: 40px;
    align-items: center;
  }}

  /* Card Styles */
  .card {{
    background: white;
    border: 2px solid #e2ded5;
    border-radius: 20px;
    padding: 32px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.03);
  }}

  .card-highlight {{
    background: #ffffff;
    border: 2px solid #002855;
    border-radius: 20px;
    padding: 32px;
    position: relative;
    box-shadow: 0 10px 24px rgba(0,40,85,0.08);
  }}

  .card-danger {{
    background: #fff8f8;
    border: 2px solid #fecaca;
    border-radius: 20px;
    padding: 32px;
  }}

  .card-success {{
    background: #f0fdf4;
    border: 2px solid #bbf7d0;
    border-radius: 20px;
    padding: 32px;
  }}

  .card-icon {{
    font-size: 36px;
    margin-bottom: 16px;
    display: inline-block;
  }}

  .card-title {{
    font-size: 22px;
    font-weight: 700;
    color: #002855;
    margin-bottom: 12px;
  }}

  .card-text {{
    font-size: 16px;
    color: #334155;
    line-height: 1.6;
    font-weight: 400;
  }}

  /* Slide 1 Cover Specifics */
  .cover-slide {{
    background: linear-gradient(135deg, #001833 0%, #002855 60%, #003875 100%);
    color: white;
  }}

  .cover-slide .slide-header {{
    border-bottom: 1.5px solid rgba(255,255,255,0.15);
  }}

  .cover-slide .slide-footer {{
    border-top: 1.5px solid rgba(255,255,255,0.15);
    color: #94a3b8;
  }}

  .cover-slide .kaleva-logo {{
    color: white;
  }}

  .cover-title {{
    font-size: 72px;
    font-weight: 800;
    letter-spacing: -1.5px;
    line-height: 1.1;
    color: #ffffff;
    margin-bottom: 20px;
  }}

  .cover-subtitle {{
    font-size: 28px;
    font-weight: 500;
    color: #cbd5e1;
    max-width: 1200px;
    line-height: 1.4;
    margin-bottom: 40px;
  }}

  .pill-container {{
    display: flex;
    gap: 16px;
    margin-bottom: 50px;
  }}

  .cover-pill {{
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(8px);
    border: 1px solid rgba(255,255,255,0.2);
    padding: 10px 22px;
    border-radius: 9999px;
    font-size: 16px;
    font-weight: 600;
    color: white;
  }}

  .metric-box {{
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 18px;
    padding: 24px;
    text-align: center;
  }}

  .metric-val {{
    font-size: 42px;
    font-weight: 800;
    color: #38bdf8;
    margin-bottom: 6px;
  }}

  .metric-lbl {{
    font-size: 14px;
    font-weight: 600;
    color: #cbd5e1;
    text-transform: uppercase;
    letter-spacing: 1px;
  }}

  /* Table styling */
  table.matrix {{
    width: 100%;
    border-collapse: collapse;
    background: white;
    border-radius: 16px;
    overflow: hidden;
    border: 1.5px solid #dedad2;
  }}

  table.matrix th {{
    background: #002855;
    color: white;
    font-size: 16px;
    font-weight: 700;
    padding: 16px 20px;
    text-align: left;
  }}

  table.matrix td {{
    padding: 16px 20px;
    font-size: 15px;
    border-bottom: 1px solid #f1f0ea;
    color: #1e293b;
    vertical-align: middle;
  }}

  table.matrix tr:last-child td {{
    border-bottom: none;
  }}

  .tag-danger {{
    background: #fee2e2;
    color: #991b1b;
    padding: 4px 10px;
    border-radius: 6px;
    font-weight: 700;
    font-size: 13px;
  }}

  .tag-success {{
    background: #dcfce7;
    color: #166534;
    padding: 4px 10px;
    border-radius: 6px;
    font-weight: 700;
    font-size: 13px;
  }}

  .screenshot-frame {{
    border: 4px solid #002855;
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 16px 36px rgba(0,0,0,0.15);
    background: white;
  }}

  .screenshot-frame img {{
    width: 100%;
    height: auto;
    display: block;
  }}
</style>
</head>
<body>

<!-- SLIDE 1: COVER -->
<div class="slide cover-slide">
  <div class="slide-header">
    <div class="brand-group">
      <div class="kaleva-logo">KALEVA</div>
      <div class="badge-red">TASKU</div>
    </div>
    <div class="header-meta" style="color: #cbd5e1;">JunctionX Oulu 2026 • Challenge 2</div>
  </div>

  <div class="slide-body">
    <div class="badge-tag" style="align-self: flex-start; margin-bottom: 20px; background: #38bdf8; color: #001833;">
      News For Everyone: Agentic Multilingual Newsroom
    </div>
    <h1 class="cover-title">Kaleva Tasku: Visuaalinen Uutispalvelu ja Arjen Tulkki</h1>
    <p class="cover-subtitle">
      A community-driven, agentic civic newsroom that bridges 125 years of Kaleva's trusted journalism with zero-translation situational ergonomics for Oulu's international population.
    </p>

    <div class="pill-container">
      <div class="cover-pill">🤖 Autonomous 3-Agent Editorial Pipeline</div>
      <div class="cover-pill">📐 Zero-Translation Situation Diagrams</div>
      <div class="cover-pill">⚖️ 100% JSN Code of Ethics Verified</div>
      <div class="cover-pill">❄️ Arctic Ergonomics (Korva Audio)</div>
    </div>

    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; max-width: 1200px;">
      <div class="metric-box">
        <div class="metric-val">5 000+</div>
        <div class="metric-lbl">Target Expats & Students</div>
      </div>
      <div class="metric-box">
        <div class="metric-val">&lt; 2 sec</div>
        <div class="metric-lbl">Comprehension Time</div>
      </div>
      <div class="metric-box">
        <div class="metric-val">100%</div>
        <div class="metric-lbl">Human-in-the-Loop JSN</div>
      </div>
      <div class="metric-box">
        <div class="metric-val">€114k</div>
        <div class="metric-lbl">Yearly B2B Institutional ARR</div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div>Project Team: Oksana & Vinod</div>
    <div>Kaleva Media • News For Everyone Track</div>
  </div>
</div>

<!-- SLIDE 2: THE PROBLEM -->
<div class="slide">
  <div class="slide-header">
    <div class="brand-group">
      <div class="kaleva-logo">KALEVA</div>
      <div class="badge-tag">The Arctic Information Desert</div>
    </div>
    <div class="header-meta">Challenge 2: The Core Strategic Problem</div>
  </div>

  <div class="slide-body">
    <div class="slide-title-block">
      <h1>Oulu's International Community is Cut Off in Crises</h1>
      <p>5,000+ university students, Nokia ICT engineers, and seasonal workers live in an information vacuum.</p>
    </div>

    <div class="grid-3">
      <div class="card-danger">
        <div class="card-icon">❄️ 🚨</div>
        <h3 class="card-title" style="color: #991b1b;">1. Panic & Misinformation</h3>
        <p class="card-text">
          When transit freezes at −25°C or sirens blare at Valkea mall, non-Finnish speakers cannot read local news. They default to anonymous WhatsApp groups and Jodel, where unfounded panic, scams, and dangerous rumors spread unchecked.
        </p>
      </div>

      <div class="card-danger">
        <div class="card-icon">🌐 ❌</div>
        <h3 class="card-title" style="color: #991b1b;">2. Raw Translation Fails</h3>
        <p class="card-text">
          Standard tools like Google Translate translate literal words but fail on Finnish civic reality. Words like <em>Pääkallokeli</em>, <em>Baana</em>, <em>PSOAS</em>, or <em>Kela</em> carry critical legal, safety, and cultural meanings that raw machine translation distorts.
        </p>
      </div>

      <div class="card-danger">
        <div class="card-icon">🗞️ 📉</div>
        <h3 class="card-title" style="color: #991b1b;">3. Media Churn & Disconnect</h3>
        <p class="card-text">
          Traditional Nordic broadsheet subscriptions do not fit Gen Z and international demographics. Without accessible onboarding, newcomers remain isolated, and regional publishers lose an entire generation of future readers.
        </p>
      </div>
    </div>

    <div class="card" style="margin-top: 30px; background: #e0f2fe; border-color: #7dd3fc;">
      <div style="display: flex; align-items: center; gap: 20px;">
        <span style="font-size: 32px;">💡</span>
        <div style="font-size: 17px; color: #0369a1; font-weight: 600; line-height: 1.5;">
          <strong>The Solution Mandate:</strong> We must deliver verified, life-critical civic facts in seconds without requiring language fluency, while strictly upholding the 125-year editorial integrity of Kaleva.
        </div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div>Kaleva Tasku • Executive Presentation</div>
    <div>Slide 2 of 7</div>
  </div>
</div>

<!-- SLIDE 3: PRODUCT OVERVIEW & DUAL ENGINE -->
<div class="slide">
  <div class="slide-header">
    <div class="brand-group">
      <div class="kaleva-logo">KALEVA</div>
      <div class="badge-tag">Dual-Engine Architecture</div>
    </div>
    <div class="header-meta">Product Innovation</div>
  </div>

  <div class="slide-body">
    <div class="slide-title-block">
      <h1>The Dual-Engine Solution: Tasku + Broadsheet 1899</h1>
      <p>Instant visual ergonomics for mobile readers, seamless depth for traditional journalism.</p>
    </div>

    <div class="grid-2-custom">
      <div style="display: flex; flex-direction: column; gap: 20px;">
        <div class="card-highlight">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <h3 class="card-title">Engine 1: Mobile Tasku View</h3>
            <span class="badge-red">Zero-Translation UX</span>
          </div>
          <p class="card-text">
            Swipeable news cards designed for fast situational awareness. Features visual edge pictograms, a digital situation diagram, highlighted civic keywords, and an immediate <em>"What to do"</em> action button.
          </p>
        </div>

        <div class="card-highlight" style="border-color: #475569;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <h3 class="card-title">Engine 2: Classic Broadsheet 1899</h3>
            <span class="badge-outline">Editorial Authority</span>
          </div>
          <p class="card-text">
            One click on any headline expands the story into an authentic multi-column newspaper view with deep editorial reporting, journalist bylines, and official JSN ethics accreditation. We never dumb down journalism.
          </p>
        </div>

        <div class="card-success">
          <h4 style="font-size: 18px; font-weight: 700; color: #166534; margin-bottom: 6px;">Arctic Ergonomics: The Korva Audio Stream</h4>
          <p class="card-text" style="color: #14532d; font-size: 15px;">
            At −20°C at an Oulu bus stop, bare fingers freeze in 40 seconds. A single click streams a high-clarity 30-second audio summary directly into wireless earbuds, complete with real-time teleprompter captions.
          </p>
        </div>
      </div>

      <div style="text-align: center;">
        <div class="screenshot-frame" style="max-height: 520px; overflow: hidden; display: flex; align-items: center; justify-content: center;">
          <img src="{app_main_b64}" alt="Kaleva Tasku Live Screenshot" style="width: 100%; object-fit: cover;">
        </div>
        <p style="font-size: 13px; color: #64748b; margin-top: 10px; font-weight: 600;">
          Working React Prototype Running in Oulu (Vite + TypeScript + Tailwind)
        </p>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div>Kaleva Tasku • Executive Presentation</div>
    <div>Slide 3 of 7</div>
  </div>
</div>

<!-- SLIDE 4: THE 4 CORE PRODUCT INNOVATIONS -->
<div class="slide">
  <div class="slide-header">
    <div class="brand-group">
      <div class="kaleva-logo">KALEVA</div>
      <div class="badge-tag">Zero-Translation UX</div>
    </div>
    <div class="header-meta">User Experience Pillars</div>
  </div>

  <div class="slide-body">
    <div class="slide-title-block">
      <h1>Four Breakthroughs for Multilingual Civic Safety</h1>
      <p>Moving from passive text translation to active situational empowerment.</p>
    </div>

    <div class="grid-2" style="gap: 24px;">
      <div class="card">
        <div style="display: flex; align-items: center; gap: 14px; margin-bottom: 12px;">
          <span style="font-size: 32px;">📐</span>
          <h3 class="card-title" style="margin-bottom: 0;">1. Digital Situation Diagrams</h3>
        </div>
        <p class="card-text">
          Zero generic stock photography. Each card features an SVG situation diagram mapping the exact problem on the left (e.g., Highway 4 snow collision 🚗💥), an arrow, and the immediate bypass route on the right (Kaakkuri interchange ➔ 45 min clear).
        </p>
      </div>

      <div class="card">
        <div style="display: flex; align-items: center; gap: 14px; margin-bottom: 12px;">
          <span style="font-size: 32px;">📖</span>
          <h3 class="card-title" style="margin-bottom: 0;">2. Interactive Civic Glossary</h3>
        </div>
        <p class="card-text">
          Finnish institutions and winter concepts (<code>PSOAS</code>, <code>Kela</code>, <code>Baana</code>, <code>Pelastuslaitos</code>) are highlighted. Clicking opens a bottom drawer explaining the plain-language definition, cultural rationale, statutory law anchor, and advice.
        </p>
      </div>

      <div class="card">
        <div style="display: flex; align-items: center; gap: 14px; margin-bottom: 12px;">
          <span style="font-size: 32px;">⚡</span>
          <h3 class="card-title" style="margin-bottom: 0;">3. Actionable Everyday Solutions</h3>
        </div>
        <p class="card-text">
          News should resolve anxiety, not cause it. Every card terminates in an actionable solution button: open live OSL bus tracking, download the international tenant rights legal guide, or register for student-free Kärpät hockey tickets.
        </p>
      </div>

      <div class="card">
        <div style="display: flex; align-items: center; gap: 14px; margin-bottom: 12px;">
          <span style="font-size: 32px;">🛡️</span>
          <h3 class="card-title" style="margin-bottom: 0;">4. AI Incompetence Boundary</h3>
        </div>
        <p class="card-text">
          If user queries touch criminal threat, domestic abuse, or passport confiscation, the agent halts AI text generation immediately. It surfaces emergency legal hotlines (Police 112, Crime Victim Emergency 116 006, Occupational Safety). Zero hallucinations on life safety.
        </p>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div>Kaleva Tasku • Executive Presentation</div>
    <div>Slide 4 of 7</div>
  </div>
</div>

<!-- SLIDE 5: AGENTIC NEWSROOM & JSN ETHICS -->
<div class="slide">
  <div class="slide-header">
    <div class="brand-group">
      <div class="kaleva-logo">KALEVA</div>
      <div class="badge-tag">Agentic Architecture</div>
    </div>
    <div class="header-meta">Editorial Ethics & Automation</div>
  </div>

  <div class="slide-body">
    <div class="slide-title-block">
      <h1>The 3-Agent Editorial Pipeline + Human Cockpit</h1>
      <p>Automating verification and cultural translation without bypassing the Council for Mass Media (JSN).</p>
    </div>

    <div class="grid-3" style="gap: 24px; margin-bottom: 24px;">
      <div class="card">
        <span class="badge-tag" style="margin-bottom: 12px; display: inline-block;">Agent 1: Radar</span>
        <h3 class="card-title">Tutkija (Investigator)</h3>
        <p class="card-text">
          Monitors civic live feeds (api.ouka.fi, Fintraffic, Kaleva RSS, community tips). Automatically strips personal data (GDPR) and geo-tags events to Oulu districts (Tuira, Linnanmaa, Kaukovainio).
        </p>
      </div>

      <div class="card-highlight">
        <span class="badge-red" style="margin-bottom: 12px; display: inline-block;">Agent 2: Ethics Auditor</span>
        <h3 class="card-title">JSN Auditor (Math of Trust)</h3>
        <p class="card-text">
          Evaluates facts with open, mathematical verification:
          <br>• <strong>+40%</strong>: Match with official 112 / rescue DB
          <br>• <strong>+35%</strong>: Corroborated by 3 geotagged witnesses
          <br>• <strong>−15%</strong>: Penalty for unverified anonymous source
        </p>
      </div>

      <div class="card">
        <span class="badge-tag" style="margin-bottom: 12px; display: inline-block;">Agent 3: Decoder</span>
        <h3 class="card-title">Toimittaja & Cultural Decoder</h3>
        <p class="card-text">
          Explains Finnish institutional norms. E.g., clarifies that 3 fire trucks responding to Valkea mall for burned bakery smoke is standard Finnish building protocol, not a security crisis.
        </p>
      </div>
    </div>

    <div class="card" style="background: #f8fafc; border: 2px dashed #002855; display: flex; justify-content: space-between; align-items: center; padding: 20px 32px;">
      <div>
        <h4 style="font-size: 20px; font-weight: 800; color: #002855;">Human-in-the-Loop Editorial Cockpit</h4>
        <p style="font-size: 15px; color: #475569; margin-top: 4px;">
          No story is published autonomously. Kaleva's editor retains final oversight with a 1-click verification queue complying with JSN § 10 & § 20.
        </p>
      </div>
      <div class="badge-tag" style="background: #166534; font-size: 14px; padding: 10px 20px;">
        ✓ JSN § 10 Truth Accredited
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div>Kaleva Tasku • Executive Presentation</div>
    <div>Slide 5 of 7</div>
  </div>
</div>

<!-- SLIDE 6: BUSINESS MODEL -->
<div class="slide">
  <div class="slide-header">
    <div class="brand-group">
      <div class="kaleva-logo">KALEVA</div>
      <div class="badge-tag">Financial Viability</div>
    </div>
    <div class="header-meta">Commercial Sustainability</div>
  </div>

  <div class="slide-body">
    <div class="slide-title-block">
      <h1>B2B Institutional SaaS: €114,000 Annual Revenue</h1>
      <p>We do not burden low-income students. Institutions that depend on international safety pay the license.</p>
    </div>

    <div class="grid-2" style="gap: 36px; align-items: start;">
      <div>
        <table class="matrix">
          <thead>
            <tr>
              <th>Institutional Partner</th>
              <th>Strategic Incentive</th>
              <th>Annual ARR</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>University of Oulu & OAMK</strong></td>
              <td>Prevents international student dropout, isolation & safety crises</td>
              <td><span class="tag-success">€35 000</span></td>
            </tr>
            <tr>
              <td><strong>Nokia & ICT Corporates</strong></td>
              <td>Turnkey expat civic onboarding integrated into corporate Slack</td>
              <td><span class="tag-success">€25 000</span></td>
            </tr>
            <tr>
              <td><strong>Oulu 2026 Foundation</strong></td>
              <td>Civic safety & cultural guide for 300 000 European visitors</td>
              <td><span class="tag-success">€40 000</span></td>
            </tr>
            <tr>
              <td><strong>Lapland Tourism Consortia</strong></td>
              <td>Seasonal worker protection in Levi and Ruka winter hubs</td>
              <td><span class="tag-success">€14 000</span></td>
            </tr>
            <tr style="background: #f8fafc; font-weight: 800;">
              <td>TOTAL PROJECTED REVENUE</td>
              <td>Annual Recurring Contracts</td>
              <td style="color: #002855; font-size: 18px;">€114 000</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div style="display: flex; flex-direction: column; gap: 20px;">
        <div class="card" style="border-left: 6px solid #166534;">
          <h4 style="font-size: 18px; font-weight: 700; color: #166534; margin-bottom: 8px;">Lean Operational Costs: €18 240 / year</h4>
          <p class="card-text" style="font-size: 15px;">
            • LLM inference & hosting APIs: €2 640 / yr<br>
            • Student fact-checker verification pool: €14 400 / yr<br>
            • Maintenance & data feed relays: €1 200 / yr
          </p>
        </div>

        <div class="card-highlight" style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); border-color: #166534;">
          <div style="font-size: 15px; font-weight: 700; color: #166534; text-transform: uppercase; letter-spacing: 1px;">
            Unit Economics & Breakeven
          </div>
          <div style="font-size: 38px; font-weight: 800; color: #14532d; margin: 8px 0;">
            84.0% Gross Margin
          </div>
          <p style="font-size: 15px; color: #166534; font-weight: 600;">
            A single institutional contract (e.g. University of Oulu) fully finances the entire operation from Day 1.
          </p>
        </div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div>Kaleva Tasku • Executive Presentation</div>
    <div>Slide 6 of 7</div>
  </div>
</div>

<!-- SLIDE 7: TEAM & ROADMAP -->
<div class="slide">
  <div class="slide-header">
    <div class="brand-group">
      <div class="kaleva-logo">KALEVA</div>
      <div class="badge-tag">Team & Roadmap</div>
    </div>
    <div class="header-meta">JunctionX Oulu 2026 Finale</div>
  </div>

  <div class="slide-body">
    <div class="slide-title-block">
      <h1>Ready for Oulu 2026: Connecting Everyone</h1>
      <p>Built with production-ready technology and grounded in northern culture.</p>
    </div>

    <div class="grid-3" style="gap: 28px; margin-bottom: 30px;">
      <div class="card">
        <h3 class="card-title">Team: Oksana & Vinod</h3>
        <p class="card-text">
          Multidisciplinary execution combining Nordic UX design, full-stack React/TypeScript engineering, and agentic media architecture.
        </p>
      </div>

      <div class="card">
        <h3 class="card-title">Production Tech Stack</h3>
        <p class="card-text">
          • Frontend: React 18, TypeScript, TailwindCSS<br>
          • Arctic Voice: Web Speech & Edge Speech API<br>
          • Newsroom Backend: Multi-agent verification pipeline<br>
          • Open Data: api.ouka.fi & Fintraffic relays
        </p>
      </div>

      <div class="card-highlight">
        <h3 class="card-title">Oulu 2026 Pilot</h3>
        <p class="card-text">
          Ready for deployment alongside the European Capital of Culture kickoff. Ensuring no student, worker, or traveler in the North is left in the dark.
        </p>
      </div>
    </div>

    <div class="card" style="background: #002855; color: white; border: none; padding: 28px 40px; text-align: center;">
      <h3 style="font-size: 26px; font-weight: 800; margin-bottom: 8px; color: #ffffff;">
        «News for Everyone» isn't just about language — it's about belonging.
      </h3>
      <p style="font-size: 17px; color: #93c5fd; font-weight: 500;">
        Kaleva Tasku makes Oulu's cold winters warm, safe, and navigable for all residents.
      </p>
    </div>
  </div>

  <div class="slide-footer">
    <div>Kaleva Tasku • JunctionX Oulu 2026</div>
    <div>Slide 7 of 7</div>
  </div>
</div>

</body>
</html>
"""

    with open("presentation.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("Generated presentation.html. Converting to PDF via Playwright Chrome...")

    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=chrome_path)
        page = browser.new_page(viewport={'width': 1920, 'height': 1080})
        page.goto(f"file:///{os.path.abspath('presentation.html')}")
        page.wait_for_timeout(1500)
        
        pdf_path = "Kaleva_Tasku_Presentation.pdf"
        page.pdf(
            path=pdf_path,
            width="1920px",
            height="1080px",
            print_background=True,
            display_header_footer=False,
            margin={'top': '0px', 'bottom': '0px', 'left': '0px', 'right': '0px'}
        )
        browser.close()
        print(f"Successfully generated {pdf_path} (Size: {os.path.getsize(pdf_path) / 1024:.1f} KB)")

if __name__ == '__main__':
    create_presentation()
