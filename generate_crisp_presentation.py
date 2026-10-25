import base64
import os
import subprocess

# 1. Load base64 of the latest screenshots
with open('card_screenshot_perfect.png', 'rb') as f:
    b64_card = base64.b64encode(f.read()).decode('utf-8')

with open('broadsheet_screenshot_perfect.png', 'rb') as f:
    b64_broadsheet = base64.b64encode(f.read()).decode('utf-8')

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Kaleva Tasku - Executive Pitch Deck</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Cinzel:wght@700&display=swap');

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
    background: #f8f6f0;
    padding: 52px 76px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}

  /* Top Navigation */
  .slide-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid #e2ded5;
    padding-bottom: 16px;
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
    padding: 5px 14px;
    border-radius: 9999px;
    text-transform: uppercase;
  }}

  .badge-red {{
    background: #c8102e;
    color: white;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1px;
    padding: 5px 14px;
    border-radius: 9999px;
    text-transform: uppercase;
  }}

  .badge-orange {{
    background: #ff8533;
    color: white;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1px;
    padding: 5px 14px;
    border-radius: 9999px;
    text-transform: uppercase;
  }}

  .badge-outline {{
    border: 1.5px solid #002855;
    color: #002855;
    font-size: 13px;
    font-weight: 700;
    padding: 4px 12px;
    border-radius: 9999px;
  }}

  .header-meta {{
    font-size: 15px;
    font-weight: 600;
    color: #64748b;
  }}

  /* Body */
  .slide-body {{
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    margin-top: 18px;
    margin-bottom: 14px;
  }}

  .slide-title-block {{
    margin-bottom: 22px;
  }}

  .slide-title-block h1 {{
    font-size: 42px;
    font-weight: 800;
    color: #002855;
    line-height: 1.15;
    letter-spacing: -0.5px;
  }}

  .slide-title-block p {{
    font-size: 19px;
    color: #475569;
    font-weight: 500;
    margin-top: 6px;
  }}

  /* Footer */
  .slide-footer {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1.5px solid #e2ded5;
    padding-top: 14px;
    font-size: 14px;
    color: #64748b;
    font-weight: 600;
  }}

  /* Cards */
  .card {{
    background: white;
    border: 2px solid #e2ded5;
    border-radius: 18px;
    padding: 24px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.03);
  }}

  .card-highlight {{
    background: #ffffff;
    border: 2px solid #002855;
    border-radius: 18px;
    padding: 24px;
    position: relative;
    box-shadow: 0 10px 24px rgba(0,40,85,0.07);
  }}

  .card-danger {{
    background: #fff8f8;
    border: 2px solid #fecaca;
    border-radius: 18px;
    padding: 24px;
  }}

  .card-success {{
    background: #f0fdf4;
    border: 2px solid #bbf7d0;
    border-radius: 18px;
    padding: 24px;
  }}

  .card-blue {{
    background: #f0f7ff;
    border: 2px solid #bae6fd;
    border-radius: 18px;
    padding: 24px;
  }}

  .card-icon {{
    font-size: 32px;
    margin-bottom: 10px;
    display: inline-block;
  }}

  .card-title {{
    font-size: 20px;
    font-weight: 700;
    color: #002855;
    margin-bottom: 8px;
  }}

  .card-text {{
    font-size: 15px;
    color: #334155;
    line-height: 1.55;
  }}

  /* Cover specifics */
  .cover-slide {{
    background: linear-gradient(135deg, #001833 0%, #002855 60%, #003a7a 100%);
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
    font-size: 64px;
    font-weight: 800;
    letter-spacing: -1.5px;
    line-height: 1.1;
    color: #ffffff;
    margin-bottom: 16px;
  }}

  .cover-subtitle {{
    font-size: 24px;
    font-weight: 500;
    color: #cbd5e1;
    max-width: 1300px;
    line-height: 1.4;
    margin-bottom: 34px;
  }}

  .metric-box {{
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.16);
    border-radius: 16px;
    padding: 22px;
    backdrop-filter: blur(10px);
  }}

  .metric-val {{
    font-size: 36px;
    font-weight: 800;
    color: #38bdf8;
    margin-bottom: 4px;
  }}

  .metric-lbl {{
    font-size: 13px;
    font-weight: 600;
    color: #cbd5e1;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}

  /* Table */
  table.matrix {{
    width: 100%;
    border-collapse: collapse;
    background: white;
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 4px 14px rgba(0,0,0,0.03);
    border: 1.5px solid #e2ded5;
  }}

  table.matrix th {{
    background: #002855;
    color: white;
    font-size: 15px;
    font-weight: 700;
    padding: 13px 18px;
    text-align: left;
  }}

  table.matrix td {{
    padding: 13px 18px;
    font-size: 14px;
    border-bottom: 1px solid #f1f0ea;
    color: #1e293b;
    vertical-align: middle;
  }}

  table.matrix tr:last-child td {{
    border-bottom: none;
  }}

  .tag-success {{
    background: #dcfce7;
    color: #166534;
    padding: 4px 10px;
    border-radius: 6px;
    font-weight: 700;
    font-size: 13px;
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
    <div class="header-meta" style="color: #cbd5e1;">JunctionX Oulu 2026 • Challenge 2: News for Everyone</div>
  </div>

  <div class="slide-body">
    <div class="badge-tag" style="align-self: flex-start; margin-bottom: 16px; background: #38bdf8; color: #001833;">
      Agentic Multilingual Newsroom & Civic Decoder
    </div>
    <h1 class="cover-title">Kaleva Tasku: Visuaalinen Uutispalvelu ja Arjen Tulkki</h1>
    <p class="cover-subtitle">
      Bridging 125 years of Kaleva's trusted journalism with zero-translation situational ergonomics and 30-second arctic audio for Northern Finland's international population.
    </p>

    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; max-width: 1400px;">
      <div class="metric-box">
        <div class="metric-val">&lt; 2 sec</div>
        <div class="metric-lbl">Comprehension Time</div>
      </div>
      <div class="metric-box">
        <div class="metric-val">100%</div>
        <div class="metric-lbl">JSN Ethics Human-in-the-Loop</div>
      </div>
      <div class="metric-box">
        <div class="metric-val">€114 000</div>
        <div class="metric-lbl">B2B Institutional ARR</div>
      </div>
      <div class="metric-box">
        <div class="metric-val">84.0%</div>
        <div class="metric-lbl">Gross Operating Margin</div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div>Founding Team: Oksana & Vinod</div>
    <div>Kaleva Media • JunctionX Oulu 2026</div>
  </div>
</div>

<!-- SLIDE 2: THE PROBLEM -->
<div class="slide">
  <div class="slide-header">
    <div class="brand-group">
      <div class="kaleva-logo">KALEVA</div>
      <div class="badge-tag">The Arctic Information Gap</div>
    </div>
    <div class="header-meta">Challenge 2: The Core Strategic Problem</div>
  </div>

  <div class="slide-body">
    <div class="slide-title-block">
      <h1>Oulu's International Community is Cut Off in Crises</h1>
      <p>5,000+ university students, Nokia engineers, and seasonal workers live in an information vacuum.</p>
    </div>

    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 28px;">
      <div class="card-danger">
        <div class="card-icon">❄️ 🚨</div>
        <h3 class="card-title" style="color: #991b1b;">1. Hazard Isolation</h3>
        <p class="card-text">
          When transit halts at −25°C or police seal off central hubs, non-Finnish speakers cannot read regional broadsheets. Vital warnings never reach them.
        </p>
      </div>

      <div class="card-danger">
        <div class="card-icon">🌐 ❌</div>
        <h3 class="card-title" style="color: #991b1b;">2. Raw Translation Fails</h3>
        <p class="card-text">
          Google Translate translates words, not civic reality. Critical terms like <em>Baana</em>, <em>Pääkallokeli</em>, <em>PSOAS</em>, and <em>Kela</em> lose all life-safety and legal context.
        </p>
      </div>

      <div class="card-danger">
        <div class="card-icon">📱 ⚠️</div>
        <h3 class="card-title" style="color: #991b1b;">3. WhatsApp Panic & Churn</h3>
        <p class="card-text">
          Locked out by traditional paywalls, foreigners retreat to unverified WhatsApp groups and Jodel, where rumors and scams spread unchecked.
        </p>
      </div>
    </div>

    <div class="card" style="margin-top: 24px; background: #e0f2fe; border-color: #7dd3fc; padding: 18px 24px;">
      <div style="display: flex; align-items: center; gap: 18px;">
        <span style="font-size: 28px;">💡</span>
        <div style="font-size: 16px; color: #0369a1; font-weight: 700;">
          The Mandate: Deliver verified, life-critical civic facts in &lt; 2 seconds without language barriers, while upholding 125 years of Kaleva's editorial integrity.
        </div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div>Kaleva Tasku • Executive Presentation</div>
    <div>Slide 2 of 7</div>
  </div>
</div>

<!-- SLIDE 3: THE LATEST TASKU CARD MODEL -->
<div class="slide">
  <div class="slide-header">
    <div class="brand-group">
      <div class="kaleva-logo">KALEVA</div>
      <div class="badge-tag">The Product Model</div>
      <div class="badge-orange">Latest Production Build</div>
    </div>
    <div class="header-meta">Zero-Translation Situational Ergonomics</div>
  </div>

  <div class="slide-body">
    <div class="slide-title-block">
      <h1>The Tasku Card: Engineered for Arctic Speed</h1>
      <p>Every element is designed for immediate comprehension on sub-zero streets.</p>
    </div>

    <div style="display: grid; grid-template-columns: 0.95fr 1.05fr; gap: 36px; align-items: center;">
      <!-- Actual App Screenshot -->
      <div style="text-align: center;">
        <div style="border: 3px solid #002855; border-radius: 24px; overflow: hidden; box-shadow: 0 16px 36px rgba(0,40,85,0.15); display: inline-block; background: white;">
          <img src="data:image/png;base64,{b64_card}" style="max-height: 560px; width: auto; display: block;" alt="Latest Tasku Card" />
        </div>
        <div style="font-size: 13px; color: #64748b; font-weight: 600; margin-top: 8px;">
          Production Card: Monochromatic Line Art • Korva Audio (30s) • Orange Masthead
        </div>
      </div>

      <!-- Feature Callouts -->
      <div style="display: flex; flex-direction: column; gap: 14px;">
        <div class="card-highlight" style="border-left: 6px solid #ff8533; padding: 18px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <h4 style="font-size: 17px; font-weight: 800; color: #002855;">1. Orange Newsroom Masthead («La 24.10.2026»)</h4>
            <span class="badge-orange" style="font-size: 11px;">Verified Stamp</span>
          </div>
          <p class="card-text" style="font-size: 14px;">
            Anchors every card in 125 years of Kaleva's trusted heritage. Institutional trust that users and employers rely on.
          </p>
        </div>

        <div class="card-highlight" style="border-left: 6px solid #475569; padding: 18px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <h4 style="font-size: 17px; font-weight: 800; color: #002855;">2. Korva 30s Arctic Audio Pill («(30s)»)</h4>
            <span class="badge-tag" style="font-size: 11px;">Hands-Free Safety</span>
          </div>
          <p class="card-text" style="font-size: 14px;">
            At −20°C, bare fingers freeze in 40 seconds. A single tap streams a crisp 30-second audio brief directly to earbuds so gloves stay on.
          </p>
        </div>

        <div class="card-highlight" style="border-left: 6px solid #22c55e; padding: 18px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <h4 style="font-size: 17px; font-weight: 800; color: #002855;">3. Monochromatic Line-Art Diagram</h4>
            <span class="badge-tag" style="background: #166534; font-size: 11px;">Zero Translation</span>
          </div>
          <p class="card-text" style="font-size: 14px;">
            Häiriö (Incident) ➔ Salad-Green Arrow ➔ Toimintaohje (Solution). Clean vector art eliminates confusing emojis. Comprehension in &lt;2s.
          </p>
        </div>

        <div class="card-highlight" style="border-left: 6px solid #c8102e; padding: 18px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <h4 style="font-size: 17px; font-weight: 800; color: #002855;">4. Live Civic Action Relays</h4>
            <span class="badge-red" style="font-size: 11px;">Real-Time Action</span>
          </div>
          <p class="card-text" style="font-size: 14px;">
            1-click live buttons for Fintraffic Kaakkuri bypass, Police 112 incident clearance, and OSL Baana winter cycling route status.
          </p>
        </div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div>Kaleva Tasku • Executive Presentation</div>
    <div>Slide 3 of 7</div>
  </div>
</div>

<!-- SLIDE 4: THE DUAL-ENGINE ARCHITECTURE -->
<div class="slide">
  <div class="slide-header">
    <div class="brand-group">
      <div class="kaleva-logo">KALEVA</div>
      <div class="badge-tag">Dual-Engine Innovation</div>
    </div>
    <div class="header-meta">Editorial Authority & Reader Conversion</div>
  </div>

  <div class="slide-body">
    <div class="slide-title-block">
      <h1>The Dual-Engine: Tasku + Broadsheet 1899</h1>
      <p>Never dumbing down journalism: instant visual ergonomics for mobile, authentic depth on click.</p>
    </div>

    <div style="display: grid; grid-template-columns: 0.85fr 1.15fr; gap: 36px; align-items: center;">
      <!-- Engine 1 -->
      <div class="card" style="text-align: center; padding: 20px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
          <h3 style="font-size: 18px; font-weight: 800; color: #002855;">Engine 1: Mobile Tasku</h3>
          <span class="badge-orange">Zero-Translation UX</span>
        </div>
        <div style="border: 2px solid #002855; border-radius: 18px; overflow: hidden; max-height: 440px; display: inline-block; box-shadow: 0 8px 20px rgba(0,0,0,0.1);">
          <img src="data:image/png;base64,{b64_card}" style="max-height: 440px; width: auto; display: block;" alt="Engine 1" />
        </div>
        <div style="font-size: 13.5px; font-weight: 700; color: #002855; margin-top: 10px;">
          Rapid Situational Awareness (&lt;2s)
        </div>
        <p class="card-text" style="font-size: 13px; margin-top: 4px;">
          Decodes severe weather, road collisions, and transit delays for fast everyday survival.
        </p>
      </div>

      <!-- Engine 2 -->
      <div class="card" style="text-align: center; padding: 20px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
          <h3 style="font-size: 18px; font-weight: 800; color: #002855;">Engine 2: Broadsheet 1899</h3>
          <span class="badge-tag" style="background: #166534;">JSN § 10 Certified</span>
        </div>
        <div style="border: 2px solid #dedad2; border-radius: 18px; overflow: hidden; max-height: 440px; display: inline-block; box-shadow: 0 8px 20px rgba(0,0,0,0.1);">
          <img src="data:image/png;base64,{b64_broadsheet}" style="max-height: 440px; width: auto; display: block;" alt="Engine 2" />
        </div>
        <div style="font-size: 13.5px; font-weight: 700; color: #002855; margin-top: 10px;">
          Full Editorial Journalism
        </div>
        <p class="card-text" style="font-size: 13px; margin-top: 4px;">
          One tap on any headline opens authentic investigative journalism, bylines, and JSN ethics accreditation.
        </p>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div>Kaleva Tasku • Executive Presentation</div>
    <div>Slide 4 of 7</div>
  </div>
</div>

<!-- SLIDE 5: 3-AGENT EDITORIAL PIPELINE -->
<div class="slide">
  <div class="slide-header">
    <div class="brand-group">
      <div class="kaleva-logo">KALEVA</div>
      <div class="badge-tag">AI Newsroom Architecture</div>
    </div>
    <div class="header-meta">Technology & Editorial Sovereignty</div>
  </div>

  <div class="slide-body">
    <div class="slide-title-block">
      <h1>The 3-Agent Pipeline + Human Cockpit</h1>
      <p>Automated multi-agent synthesis guarded by human editors and Finnish JSN standards.</p>
    </div>

    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px;">
      <div class="card-highlight">
        <div class="card-icon">📡 📥</div>
        <h3 class="card-title">Agent 1: Ingest & Triage</h3>
        <p class="card-text">
          Monitors incoming Kaleva wires, police reports, and OSL transit feeds. Automatically scrubs personal data (GDPR) and clusters events by district.
        </p>
      </div>

      <div class="card-highlight">
        <div class="card-icon">🧠 📐</div>
        <h3 class="card-title">Agent 2: Ergonomic Synthesizer</h3>
        <p class="card-text">
          Distills complex reports into high-contrast line-art diagrams, plain language summaries, and 30-second Korva spoken audio scripts.
        </p>
      </div>

      <div class="card-highlight">
        <div class="card-icon">⚖️ 🛡️</div>
        <h3 class="card-title">Agent 3: JSN Ethics Auditor</h3>
        <p class="card-text">
          Calculates verification trust score (+40% police match, +35% geotagged witnesses). Enforces Finnish Council for Mass Media (§ 10 & § 20) compliance.
        </p>
      </div>
    </div>

    <div class="card-success" style="margin-top: 24px; padding: 20px 28px;">
      <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
          <span style="font-size: 13px; font-weight: 800; color: #166534; text-transform: uppercase; letter-spacing: 1px;">Human-in-the-Loop Cockpit</span>
          <div style="font-size: 17px; color: #14532d; font-weight: 700; margin-top: 4px;">
            Kaleva desk editors maintain full sovereignty: 1-click approval, real-time diff inspect, or instant recall. Zero unverified AI publishing.
          </div>
        </div>
        <span class="badge-tag" style="background: #166534;">100% Editorial Sovereignty</span>
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
    <div class="header-meta">B2B Institutional SaaS Model</div>
  </div>

  <div class="slide-body">
    <div class="slide-title-block">
      <h1>B2B Institutional SaaS: €114,000 Annual Revenue</h1>
      <p>We do not burden low-income students. Institutions with a duty of care pay the license.</p>
    </div>

    <div style="display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 32px; align-items: start;">
      <table class="matrix">
        <thead>
          <tr>
            <th>Institutional Client</th>
            <th>Primary Value Driver</th>
            <th>Annual ARR</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>University of Oulu & OAMK</strong></td>
            <td>Student retention & sub-zero duty-of-care alerts</td>
            <td><span class="tag-success">€35 000</span></td>
          </tr>
          <tr>
            <td><strong>Nokia & Oulu ICT Tech Hub</strong></td>
            <td>Corporate expat onboarding via Slack/Teams bot</td>
            <td><span class="tag-success">€25 000</span></td>
          </tr>
          <tr>
            <td><strong>City of Oulu & Oulu 2026</strong></td>
            <td>Capital of Culture civic guide for 300,000 visitors</td>
            <td><span class="tag-success">€40 000</span></td>
          </tr>
          <tr>
            <td><strong>Lapland Tourism Consortia</strong></td>
            <td>Seasonal worker winter safety in Levi & Ruka</td>
            <td><span class="tag-success">€14 000</span></td>
          </tr>
          <tr style="background: #f8fafc; font-weight: 800;">
            <td>TOTAL ANNUAL CONTRACTS</td>
            <td>Prepaid Institutional B2B ARR</td>
            <td style="color: #002855; font-size: 18px;">€114 000</td>
          </tr>
        </tbody>
      </table>

      <div style="display: flex; flex-direction: column; gap: 16px;">
        <div class="card" style="border-left: 6px solid #166534; padding: 20px;">
          <h4 style="font-size: 16px; font-weight: 700; color: #166534; margin-bottom: 6px;">Lean Annual Costs: €18 240 / yr</h4>
          <p class="card-text" style="font-size: 13.5px;">
            • LLM APIs (Gemini Flash / OpenAI): €2 640<br>
            • JSN Student Fact-Checker Pool: €14 400<br>
            • Hosting & Audio CDN Relays: €1 200
          </p>
        </div>

        <div class="card-success" style="padding: 20px;">
          <div style="font-size: 13px; font-weight: 800; color: #166534; text-transform: uppercase; letter-spacing: 1px;">
            Unit Economics & Breakeven
          </div>
          <div style="font-size: 38px; font-weight: 800; color: #14532d; margin: 4px 0;">
            84.0% Gross Margin
          </div>
          <p style="font-size: 13.5px; color: #166534; font-weight: 600;">
            A single contract (University of Oulu @ €35k) achieves full operational breakeven with €16,760 net profit on Day 1.
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

<!-- SLIDE 7: OULU 2026 ROADMAP -->
<div class="slide">
  <div class="slide-header">
    <div class="brand-group">
      <div class="kaleva-logo">KALEVA</div>
      <div class="badge-tag">Oulu 2026 Vision</div>
    </div>
    <div class="header-meta">JunctionX Oulu 2026 Finale</div>
  </div>

  <div class="slide-body">
    <div class="slide-title-block">
      <h1>Ready for Oulu 2026: Connecting Everyone</h1>
      <p>Production-ready code grounded in northern culture and scalable across the Nordics.</p>
    </div>

    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-bottom: 24px;">
      <div class="card-highlight">
        <span class="badge-orange" style="margin-bottom: 10px; display: inline-block;">Phase 1: 2026</span>
        <h3 class="card-title">Oulu 2026 Deployment</h3>
        <p class="card-text">
          Official civic safety & cultural companion for the European Capital of Culture kickoff. Guarantees no international visitor or student is left in the dark.
        </p>
      </div>

      <div class="card-highlight">
        <span class="badge-tag" style="margin-bottom: 10px; display: inline-block;">Phase 2: 2027</span>
        <h3 class="card-title">Northern Finland Expansion</h3>
        <p class="card-text">
          Expansion into Lapland, Rovaniemi, and Kainuu. Scaling seasonal worker safety and winter tourism guidance to €245,000 ARR.
        </p>
      </div>

      <div class="card-highlight">
        <span class="badge-outline" style="margin-bottom: 10px; display: inline-block;">Phase 3: 2028</span>
        <h3 class="card-title">Pan-Nordic Syndication</h3>
        <p class="card-text">
          White-labeling the Tasku Civic Engine to other regional Nordic publishers (Keskisuomalainen, TS-Yhtymä), scaling to €560,000 ARR.
        </p>
      </div>
    </div>

    <div class="card" style="background: #002855; color: white; border: none; padding: 24px 36px; text-align: center;">
      <h3 style="font-size: 24px; font-weight: 800; margin-bottom: 6px; color: #ffffff;">
        «News for Everyone» isn't just about language — it's about civic safety and belonging.
      </h3>
      <p style="font-size: 16px; color: #93c5fd; font-weight: 500;">
        Kaleva Tasku makes Northern Finland's cold winters warm, safe, and navigable for all residents.
      </p>
    </div>
  </div>

  <div class="slide-footer">
    <div>Project Team: Oksana & Vinod</div>
    <div>Kaleva Media • News For Everyone Track</div>
  </div>
</div>

</body>
</html>
"""

with open('presentation.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Created crisp presentation.html!")

# Render to PDF
chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html_abs = os.path.abspath('presentation.html')
pdf_abs = os.path.abspath('Kaleva_Tasku_Presentation.pdf')

cmd = [
    chrome_path,
    '--headless=new',
    '--disable-gpu',
    '--no-pdf-header-footer',
    '--run-all-compositor-stages-before-draw',
    '--virtual-time-budget=5000',
    f'--print-to-pdf={pdf_abs}',
    f'file:///{html_abs.replace(os.sep, "/")}'
]
res = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
if os.path.exists(pdf_abs):
    print(f"SUCCESS: Kaleva_Tasku_Presentation.pdf created with size {os.path.getsize(pdf_abs)} bytes")
else:
    print("ERROR rendering PDF:", res.stderr)
