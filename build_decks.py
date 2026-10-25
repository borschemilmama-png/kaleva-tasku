import base64
import os
import subprocess

# 1. Load base64 of perfect screenshots
with open('card_screenshot_perfect.png', 'rb') as f:
    b64_card = base64.b64encode(f.read()).decode('utf-8')

with open('broadsheet_screenshot_perfect.png', 'rb') as f:
    b64_broadsheet = base64.b64encode(f.read()).decode('utf-8')

print("Loaded base64 screenshots: card len =", len(b64_card), ", broadsheet len =", len(b64_broadsheet))

# -------------------------------------------------------------
# 2. BUILD business_model_presentation.html (8 SLIDES)
# -------------------------------------------------------------
bm_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Kaleva Tasku - Business Model & Commercialization Strategy</title>
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
    padding: 50px 70px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}

  /* Header */
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

  /* Slide Body */
  .slide-body {{
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    margin-top: 20px;
    margin-bottom: 16px;
  }}

  .slide-title-block {{
    margin-bottom: 20px;
  }}

  .slide-title-block h1 {{
    font-size: 40px;
    font-weight: 800;
    color: #002855;
    line-height: 1.15;
    letter-spacing: -0.5px;
  }}

  .slide-title-block p {{
    font-size: 18px;
    color: #475569;
    font-weight: 500;
    margin-top: 5px;
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

  /* Layouts */
  .grid-2 {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 32px;
  }}

  .grid-3 {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 22px;
  }}

  .grid-4 {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
  }}

  /* Cards */
  .card {{
    background: white;
    border: 2px solid #e2ded5;
    border-radius: 16px;
    padding: 24px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.03);
  }}

  .card-highlight {{
    background: #ffffff;
    border: 2px solid #002855;
    border-radius: 16px;
    padding: 24px;
    position: relative;
    box-shadow: 0 10px 24px rgba(0,40,85,0.07);
  }}

  .card-success {{
    background: #f0fdf4;
    border: 2px solid #bbf7d0;
    border-radius: 16px;
    padding: 24px;
  }}

  .card-danger {{
    background: #fff8f8;
    border: 2px solid #fecaca;
    border-radius: 16px;
    padding: 24px;
  }}

  .card-blue {{
    background: #f0f7ff;
    border: 2px solid #bae6fd;
    border-radius: 16px;
    padding: 24px;
  }}

  .card-title {{
    font-size: 19px;
    font-weight: 700;
    color: #002855;
    margin-bottom: 8px;
  }}

  .card-text {{
    font-size: 14.5px;
    color: #334155;
    line-height: 1.55;
    font-weight: 400;
  }}

  /* Cover Slide */
  .cover-slide {{
    background: linear-gradient(135deg, #001833 0%, #002855 60%, #003b7a 100%);
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
    font-size: 60px;
    font-weight: 800;
    letter-spacing: -1.5px;
    line-height: 1.1;
    color: #ffffff;
    margin-bottom: 16px;
  }}

  .cover-subtitle {{
    font-size: 22px;
    font-weight: 500;
    color: #cbd5e1;
    max-width: 1300px;
    line-height: 1.4;
    margin-bottom: 32px;
  }}

  .metric-box {{
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.16);
    border-radius: 14px;
    padding: 20px;
    backdrop-filter: blur(10px);
  }}

  .metric-val {{
    font-size: 34px;
    font-weight: 800;
    color: #38bdf8;
    margin-bottom: 4px;
  }}

  .metric-lbl {{
    font-size: 12px;
    font-weight: 600;
    color: #cbd5e1;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}

  /* Table styling */
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
    font-size: 14.5px;
    font-weight: 700;
    padding: 13px 16px;
    text-align: left;
  }}

  table.matrix td {{
    padding: 13px 16px;
    font-size: 13.5px;
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

  /* Screenshot frame */
  .device-mockup {{
    border: 3px solid #002855;
    border-radius: 24px;
    overflow: hidden;
    box-shadow: 0 16px 36px rgba(0,40,85,0.15);
    background: white;
    display: inline-block;
  }}

  .device-mockup img {{
    display: block;
    max-height: 570px;
    width: auto;
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
      <div class="badge-orange">BUSINESS MODEL DECK</div>
    </div>
    <div class="header-meta" style="color: #cbd5e1;">JunctionX Oulu 2026 • Challenge 2</div>
  </div>

  <div class="slide-body">
    <div class="badge-tag" style="align-self: flex-start; margin-bottom: 16px; background: #38bdf8; color: #001833;">
      Institutional B2B SaaS & Civic Licensing Strategy
    </div>
    <h1 class="cover-title">Monetizing Multilingual Civic Journalism in the North</h1>
    <p class="cover-subtitle">
      Why direct consumer paywalls fail for international newcomers, how B2B civic licensing captures €114,000 ARR with 84% gross margins, and why the latest Tasku card architecture creates a zero-cannibalization growth engine for Kaleva Media.
    </p>

    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; max-width: 1400px;">
      <div class="metric-box">
        <div class="metric-val">€114 000</div>
        <div class="metric-lbl">Year 1 Contracted ARR</div>
      </div>
      <div class="metric-box">
        <div class="metric-val">84.0%</div>
        <div class="metric-lbl">Gross Operating Margin</div>
      </div>
      <div class="metric-box">
        <div class="metric-val">Day 1</div>
        <div class="metric-lbl">Breakeven on 1 Contract</div>
      </div>
      <div class="metric-box">
        <div class="metric-val">0%</div>
        <div class="metric-lbl">Core Subscription Cannibalization</div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div>Founding Team: Oksana & Vinod</div>
    <div>Kaleva Media Commercial Strategy • Executive Briefing</div>
  </div>
</div>

<!-- SLIDE 2: THE APPLICATION MODEL AS A B2B REVENUE ENGINE -->
<div class="slide">
  <div class="slide-header">
    <div class="brand-group">
      <div class="kaleva-logo">KALEVA</div>
      <div class="badge-tag">The App Model</div>
      <div class="badge-orange">Direct Feature Monetization</div>
    </div>
    <div class="header-meta">Deconstructing the Tasku Card Architecture</div>
  </div>

  <div class="slide-body">
    <div class="slide-title-block">
      <h1>The Product Model: Turning Ergonomics into Revenue</h1>
      <p>Every element of the latest Kaleva Tasku card is engineered to solve a specific institutional pain point.</p>
    </div>

    <div style="display: grid; grid-template-columns: 0.95fr 1.05fr; gap: 36px; align-items: center;">
      <!-- Real Captured App Card -->
      <div style="text-align: center;">
        <div class="device-mockup">
          <img src="data:image/png;base64,{b64_card}" alt="Latest Kaleva Tasku Card" />
        </div>
        <div style="font-size: 13px; color: #64748b; font-weight: 600; margin-top: 8px;">
          Latest Production Model: Monochromatic Line Art + Korva Audio (30s) + Orange Masthead
        </div>
      </div>

      <!-- Feature-to-Revenue Mapping -->
      <div style="display: flex; flex-direction: column; gap: 14px;">
        <div class="card-highlight" style="border-left: 6px solid #ff8533; padding: 18px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <h4 style="font-size: 17px; font-weight: 800; color: #002855;">1. Orange Masthead & Date («KALEVA TASKU • La 24.10.2026»)</h4>
            <span class="badge-orange" style="font-size: 11px;">Brand Equity</span>
          </div>
          <p class="card-text" style="font-size: 13.5px;">
            <strong>Commercial Value:</strong> Institutional co-branding anchor. Guarantees 125 years of newsroom authenticity, making the card trusted by universities and corporate HR over anonymous social feeds.
          </p>
        </div>

        <div class="card-highlight" style="border-left: 6px solid #475569; padding: 18px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <h4 style="font-size: 17px; font-weight: 800; color: #002855;">2. Korva 30s Arctic Audio Pill («(30s)» in Gray Fill)</h4>
            <span class="badge-tag" style="font-size: 11px;">Safety / Accessibility</span>
          </div>
          <p class="card-text" style="font-size: 13.5px;">
            <strong>Buyer:</strong> University of Oulu & OAMK (€35,000/yr). In −25°C winter, students cannot use touchscreens without frostbite risk. One tap streams instant 30s spoken briefings to earbuds.
          </p>
        </div>

        <div class="card-highlight" style="border-left: 6px solid #22c55e; padding: 18px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <h4 style="font-size: 17px; font-weight: 800; color: #002855;">3. Monochromatic Line Art Diagram (Problem ➔ Green Arrow ➔ Solution)</h4>
            <span class="badge-tag" style="background: #166534; font-size: 11px;">Civic Infrastructure</span>
          </div>
          <p class="card-text" style="font-size: 13.5px;">
            <strong>Buyer:</strong> City of Oulu, OSL Transit & Fintraffic (€40,000/yr). Eliminates chaotic emojis. High-contrast vector drawings decode bypasses and disruptions in &lt;2 seconds with zero language barriers.
          </p>
        </div>

        <div class="card-highlight" style="border-left: 6px solid #c8102e; padding: 18px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <h4 style="font-size: 17px; font-weight: 800; color: #002855;">4. Clickable Headline ➔ Broadsheet 1899 Deep Journalism</h4>
            <span class="badge-red" style="font-size: 11px;">Publisher Upsell</span>
          </div>
          <p class="card-text" style="font-size: 13.5px;">
            <strong>Value to Kaleva Media:</strong> Zero subscription cannibalization. Acts as top-of-funnel acquisition, converting free international readers into full €19/mo Kaleva subscribers as they integrate.
          </p>
        </div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div>Kaleva Tasku • Commercial Presentation</div>
    <div>Slide 2 of 8</div>
  </div>
</div>

<!-- SLIDE 3: THE MARKET PARADOX -->
<div class="slide">
  <div class="slide-header">
    <div class="brand-group">
      <div class="kaleva-logo">KALEVA</div>
      <div class="badge-tag">Market Realities</div>
    </div>
    <div class="header-meta">Why the Payer Must Shift from Consumer to Institution</div>
  </div>

  <div class="slide-body">
    <div class="slide-title-block">
      <h1>The Consumer Paywall Trap vs. The B2B Civic Solution</h1>
      <p>Direct consumer paywalls do not work for international residents. Here is why the payer must change.</p>
    </div>

    <div class="grid-2">
      <div class="card-danger">
        <div style="font-size: 28px; margin-bottom: 8px;">🚫 💳</div>
        <h3 class="card-title" style="color: #991b1b;">Why B2C Direct Subscriptions Fail</h3>
        <ul style="margin-left: 20px; line-height: 1.7; color: #7f1d1d; font-size: 14.5px; margin-top: 8px;">
          <li><strong>High Price Sensitivity:</strong> Exchange students, researchers, and seasonal workers will not pay €15–20/month for regional news in a language they do not speak.</li>
          <li><strong>Transient Residency:</strong> 60% of international students leave within 2–4 years. High churn destroys traditional consumer LTV/CAC ratios.</li>
          <li><strong>Default to Misinformation:</strong> When locked behind paywalls, foreigners retreat to unverified Telegram groups and Jodel, amplifying rumors during crises.</li>
          <li><strong>Zero Current Revenue:</strong> Today, Kaleva Media captures virtually €0 from Oulu's 5,000+ international population.</li>
        </ul>
      </div>

      <div class="card-success">
        <div style="font-size: 28px; margin-bottom: 8px;">🏛️ 🤝</div>
        <h3 class="card-title" style="color: #166534;">The Institutional B2B Solution</h3>
        <ul style="margin-left: 20px; line-height: 1.7; color: #14532d; font-size: 14.5px; margin-top: 8px;">
          <li><strong>Duty of Care Liability:</strong> Universities and ICT employers bear direct legal and operational costs when expats miss sub-zero transit halts, fire alerts, or campus notices.</li>
          <li><strong>Budget Alignment:</strong> Institutions already hold active budgets for "International Talent Retention", "Orientation Week", and "Occupational Safety".</li>
          <li><strong>B2B Enterprise License:</strong> Institutions purchase bulk civic access; end-users (students, employees) receive Tasku 100% free with campus/corporate SSO.</li>
          <li><strong>Immediate Monetization:</strong> Closes high-ticket, annual prepaid contracts rather than chasing micro-payments.</li>
        </ul>
      </div>
    </div>

    <div class="card" style="margin-top: 20px; background: #eff6ff; border-color: #93c5fd; padding: 18px 24px;">
      <div style="display: flex; align-items: center; gap: 16px;">
        <span style="font-size: 26px;">💡</span>
        <div style="font-size: 15.5px; color: #1e40af; font-weight: 600;">
          <strong>Strategic Takeaway:</strong> We do not ask a €800/month scholarship student to pay for civic news. We bill the university that spends €15,000 recruiting and retaining that student.
        </div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div>Kaleva Tasku • Commercial Presentation</div>
    <div>Slide 3 of 8</div>
  </div>
</div>

<!-- SLIDE 4: REVENUE MATRIX -->
<div class="slide">
  <div class="slide-header">
    <div class="brand-group">
      <div class="kaleva-logo">KALEVA</div>
      <div class="badge-tag">Customer Segments</div>
    </div>
    <div class="header-meta">The €114,000 Year 1 Revenue Engine</div>
  </div>

  <div class="slide-body">
    <div class="slide-title-block">
      <h1>The Four Institutional Revenue Pillars</h1>
      <p>Diversified B2B recurring contracts backed by institutional pain points and concrete ROI.</p>
    </div>

    <table class="matrix">
      <thead>
        <tr>
          <th style="width: 24%;">Institutional Buyer</th>
          <th style="width: 22%;">Target Population</th>
          <th style="width: 40%;">Core Value Driver & Institutional ROI</th>
          <th style="width: 14%;">Annual ARR</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <strong>University of Oulu & OAMK</strong><br>
            <span style="font-size: 12px; color: #64748b;">Higher Education</span>
          </td>
          <td>5,000+ international students, PhD researchers, and faculty</td>
          <td>
            <strong>Retention & Safety:</strong> Eliminates student isolation and winter depression; prevents costly dropouts (€12k funding penalty per student); guarantees emergency duty-of-care communication.
          </td>
          <td><span class="tag-success">€35 000</span></td>
        </tr>
        <tr>
          <td>
            <strong>Nokia & Oulu ICT Corporates</strong><br>
            <span style="font-size: 12px; color: #64748b;">Enterprise Tech</span>
          </td>
          <td>1,500+ expat software engineers & global transferees</td>
          <td>
            <strong>Turnkey Expat Onboarding:</strong> Integrated into corporate Slack/Teams; reduces HR burden answering basic civic/transit queries; increases family stay rates.
          </td>
          <td><span class="tag-success">€25 000</span></td>
        </tr>
        <tr>
          <td>
            <strong>Oulu 2026 Foundation & City</strong><br>
            <span style="font-size: 12px; color: #64748b;">Municipal Authority</span>
          </td>
          <td>300,000+ anticipated international tourists & cultural visitors</td>
          <td>
            <strong>Official Civic & Cultural Guide:</strong> Real-time event navigation, transit disruption alerts, sub-zero safety warnings, preventing public safety congestion.
          </td>
          <td><span class="tag-success">€40 000</span></td>
        </tr>
        <tr>
          <td>
            <strong>Lapland Tourism & Seasonal Consortia</strong><br>
            <span style="font-size: 12px; color: #64748b;">Hospitality & Logistics</span>
          </td>
          <td>2,000+ winter resort seasonal staff & airport transit passengers</td>
          <td>
            <strong>Arctic Safety Orientation:</strong> Extreme cold advisories, Baana cycling safety, bus schedules, healthcare access in Levi/Ruka/Oulu corridor.
          </td>
          <td><span class="tag-success">€14 000</span></td>
        </tr>
        <tr style="background: #f8fafc; font-weight: 800;">
          <td colspan="3" style="font-size: 15px; color: #002855; text-align: right; padding-right: 24px;">
            TOTAL YEAR 1 PROJECTED ANNUAL RECURRING REVENUE (ARR)
          </td>
          <td style="color: #002855; font-size: 19px; font-weight: 800;">€114 000</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="slide-footer">
    <div>Kaleva Tasku • Commercial Presentation</div>
    <div>Slide 4 of 8</div>
  </div>
</div>

<!-- SLIDE 5: THE DUAL-ENGINE ARCHITECTURE -->
<div class="slide">
  <div class="slide-header">
    <div class="brand-group">
      <div class="kaleva-logo">KALEVA</div>
      <div class="badge-tag">The Dual-Engine Funnel</div>
    </div>
    <div class="header-meta">Zero Cannibalization & Lifetime Value Architecture</div>
  </div>

  <div class="slide-body">
    <div class="slide-title-block">
      <h1>The Dual-Engine Solution: Tasku + Broadsheet 1899</h1>
      <p>How mobile situational ergonomics and classic journalism combine to create a reader acquisition pipeline.</p>
    </div>

    <div style="display: grid; grid-template-columns: 0.85fr 1.15fr; gap: 36px; align-items: center;">
      <!-- Engine 1: Tasku Card -->
      <div class="card" style="text-align: center; padding: 20px;">
        <span class="badge-orange" style="margin-bottom: 12px; display: inline-block;">Engine 1: Mobile Tasku</span>
        <div style="border: 2px solid #002855; border-radius: 18px; overflow: hidden; max-height: 440px; display: inline-block; box-shadow: 0 8px 20px rgba(0,0,0,0.1);">
          <img src="data:image/png;base64,{b64_card}" style="max-height: 440px; width: auto; display: block;" alt="Engine 1 Tasku" />
        </div>
        <div style="font-size: 13px; font-weight: 700; color: #002855; margin-top: 10px;">
          Fast Situational Awareness (&lt;2s)
        </div>
        <p class="card-text" style="font-size: 12.5px; margin-top: 4px;">
          Universal visual comprehension for severe winter events, accidents, and civic navigation without translation delay.
        </p>
      </div>

      <!-- Engine 2: Broadsheet 1899 -->
      <div class="card" style="text-align: center; padding: 20px;">
        <span class="badge-outline" style="margin-bottom: 12px; display: inline-block;">Engine 2: Broadsheet 1899</span>
        <div style="border: 2px solid #dedad2; border-radius: 18px; overflow: hidden; max-height: 440px; display: inline-block; box-shadow: 0 8px 20px rgba(0,0,0,0.1);">
          <img src="data:image/png;base64,{b64_broadsheet}" style="max-height: 440px; width: auto; display: block;" alt="Engine 2 Broadsheet" />
        </div>
        <div style="font-size: 13px; font-weight: 700; color: #002855; margin-top: 10px;">
          Editorial Authority & JSN § 10 Ethics
        </div>
        <p class="card-text" style="font-size: 12.5px; margin-top: 4px;">
          One click on any headline expands the story into an authentic multi-column newspaper article, creating a direct conversion path into full Kaleva subscriptions.
        </p>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div>Kaleva Tasku • Commercial Presentation</div>
    <div>Slide 5 of 8</div>
  </div>
</div>

<!-- SLIDE 6: UNIT ECONOMICS & PROFITABILITY -->
<div class="slide">
  <div class="slide-header">
    <div class="brand-group">
      <div class="kaleva-logo">KALEVA</div>
      <div class="badge-tag">Financial Architecture</div>
    </div>
    <div class="header-meta">Cost Structure & Gross Margin Analysis</div>
  </div>

  <div class="slide-body">
    <div class="slide-title-block">
      <h1>Unit Economics: 84.0% Gross Operating Margin</h1>
      <p>A lean, automated multi-agent backbone keeps fixed costs minimal and margins software-grade.</p>
    </div>

    <div class="grid-2" style="align-items: start;">
      <div class="card">
        <h3 class="card-title" style="margin-bottom: 14px;">Annual Cost of Goods Sold (COGS)</h3>
        <table style="width: 100%; border-collapse: collapse; font-size: 13.5px;">
          <tr style="border-bottom: 1px solid #e2ded5;">
            <td style="padding: 10px 0;"><strong>Multi-Agent LLM Inference:</strong><br><span style="color: #64748b;">Gemini Flash / OpenAI batch triage & line art diagram generation (20 stories/day)</span></td>
            <td style="text-align: right; font-weight: 700; color: #002855;">€2 640</td>
          </tr>
          <tr style="border-bottom: 1px solid #e2ded5;">
            <td style="padding: 10px 0;"><strong>Human-in-the-Loop Verification Pool:</strong><br><span style="color: #64748b;">Part-time journalism student verification pool (60 hrs/mo @ €20/hr)</span></td>
            <td style="text-align: right; font-weight: 700; color: #002855;">€14 400</td>
          </tr>
          <tr style="border-bottom: 1px solid #e2ded5;">
            <td style="padding: 10px 0;"><strong>Cloud Infrastructure & Audio CDN:</strong><br><span style="color: #64748b;">Edge hosting, WebSocket audio relays, Fintraffic/OSL data relays</span></td>
            <td style="text-align: right; font-weight: 700; color: #002855;">€1 200</td>
          </tr>
          <tr style="font-weight: 800; font-size: 15px;">
            <td style="padding: 12px 0; color: #002855;">TOTAL OPERATIONAL EXPENDITURE</td>
            <td style="text-align: right; color: #c8102e;">€18 240 / yr</td>
          </tr>
        </table>
      </div>

      <div style="display: flex; flex-direction: column; gap: 18px;">
        <div class="card-success">
          <div style="font-size: 13.5px; font-weight: 800; color: #166534; text-transform: uppercase; letter-spacing: 1px;">
            Profitability & Breakeven Point
          </div>
          <div style="font-size: 42px; font-weight: 800; color: #14532d; margin: 6px 0;">
            €95 760 <span style="font-size: 18px; font-weight: 600;">Net Profit (84%)</span>
          </div>
          <p style="font-size: 14.5px; color: #166534; line-height: 1.5;">
            Because operational overhead is capped at <strong>€18,240/yr</strong>, closing <strong>a single contract</strong> (e.g. University of Oulu @ €35,000) achieves full operational breakeven on Day 1 with €16,760 in net profit.
          </p>
        </div>

        <div class="card-blue">
          <h4 style="font-size: 15.5px; font-weight: 700; color: #0369a1; margin-bottom: 4px;">Zero Reliance on Venture Capital</h4>
          <p class="card-text" style="color: #0c4a6e; font-size: 13.5px;">
            Unlike consumer media apps burning millions on customer acquisition, Tasku is self-funding from Month 1 through institutional pre-orders.
          </p>
        </div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div>Kaleva Tasku • Commercial Presentation</div>
    <div>Slide 6 of 8</div>
  </div>
</div>

<!-- SLIDE 7: 3-YEAR FINANCIAL PROJECTIONS -->
<div class="slide">
  <div class="slide-header">
    <div class="brand-group">
      <div class="kaleva-logo">KALEVA</div>
      <div class="badge-tag">Growth Roadmap</div>
    </div>
    <div class="header-meta">Financial Projections & Scalability</div>
  </div>

  <div class="slide-body">
    <div class="slide-title-block">
      <h1>3-Year Scaling Roadmap: From Oulu to Pan-Nordic Licensing</h1>
      <p>Expanding from an Oulu-based pilot to a white-label civic engine across Nordic publishers.</p>
    </div>

    <table class="matrix" style="margin-bottom: 20px;">
      <thead>
        <tr>
          <th>Metric / Financial Milestone</th>
          <th>Year 1 (Oulu Foundation)</th>
          <th>Year 2 (Northern Finland)</th>
          <th>Year 3 (Pan-Nordic Licensing)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Geographic Scope</strong></td>
          <td>Oulu Metropolitan Area</td>
          <td>Lapland, Rovaniemi, Kemi, Kainuu</td>
          <td>Tampere, Turku, Norrbotten (Sweden)</td>
        </tr>
        <tr>
          <td><strong>Active Institutional Clients</strong></td>
          <td>4 (Uni Oulu, Nokia, City, Tourism)</td>
          <td>11 institutional partners</td>
          <td>28 partners & 3 publisher syndicates</td>
        </tr>
        <tr>
          <td><strong>Monthly Active Users (MAU)</strong></td>
          <td>8,500 users</td>
          <td>24,000 users</td>
          <td>65,000 users</td>
        </tr>
        <tr>
          <td><strong>Annual Recurring Revenue (ARR)</strong></td>
          <td><span class="tag-success" style="font-size: 14.5px;">€114 000</span></td>
          <td><span class="tag-success" style="font-size: 14.5px;">€245 000</span></td>
          <td><span class="tag-success" style="font-size: 14.5px;">€560 000</span></td>
        </tr>
        <tr>
          <td><strong>Annual Operating Costs (COGS + OpEx)</strong></td>
          <td>€18 240</td>
          <td>€38 500</td>
          <td>€86 000</td>
        </tr>
        <tr style="background: #f0fdf4; font-weight: 800;">
          <td style="color: #166534; font-size: 14.5px;">NET OPERATING PROFIT (EBITDA)</td>
          <td style="color: #166534; font-size: 15.5px;">€95 760 (84%)</td>
          <td style="color: #166534; font-size: 15.5px;">€206 500 (84%)</td>
          <td style="color: #166534; font-size: 15.5px;">€474 000 (85%)</td>
        </tr>
      </tbody>
    </table>

    <div class="card" style="background: #f8fafc; border-color: #cbd5e1; padding: 18px;">
      <div style="font-size: 13.5px; color: #334155; line-height: 1.6;">
        <strong>The Scale Advantage:</strong> In Year 3, the "Tasku Civic Engine" is packaged as a white-label SaaS solution syndicated to other regional Nordic publishers (e.g., Keskisuomalainen, TS-Yhtymä, Norr Media), transforming Kaleva Media from a regional publisher into a media-tech platform provider.
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div>Kaleva Tasku • Commercial Presentation</div>
    <div>Slide 7 of 8</div>
  </div>
</div>

<!-- SLIDE 8: RISK MATRIX & MITIGATION -->
<div class="slide">
  <div class="slide-header">
    <div class="brand-group">
      <div class="kaleva-logo">KALEVA</div>
      <div class="badge-tag">Risk Governance</div>
    </div>
    <div class="header-meta">Adversarial Scrutiny & Mitigation</div>
  </div>

  <div class="slide-body">
    <div class="slide-title-block">
      <h1>Critical Risk Analysis & Defensive Moats</h1>
      <p>Addressing every operational vulnerability, legal constraint, and market objection head-on.</p>
    </div>

    <div class="grid-2">
      <div class="card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
          <h3 class="card-title" style="color: #c8102e; font-size: 17.5px;">1. AI Hallucination & JSN Liability</h3>
          <span class="badge-red" style="font-size: 11px; padding: 3px 8px;">Legal / Editorial</span>
        </div>
        <p class="card-text" style="font-size: 13.5px;">
          <strong>Risk:</strong> AI misinterprets bus delays or police warnings, damaging Kaleva’s 125-year reputation.<br>
          <strong>Mitigation:</strong> Deterministic JSN ethics validation agent scores every card before publish. Human editorial cockpit retains one-click sign-off. LLM temperature set to 0.0 for strict fact extraction.
        </p>
      </div>

      <div class="card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
          <h3 class="card-title" style="color: #c8102e; font-size: 17.5px;">2. Finnish Public Procurement Delays</h3>
          <span class="badge-orange" style="font-size: 11px; padding: 3px 8px;">Sales Cycle</span>
        </div>
        <p class="card-text" style="font-size: 13.5px;">
          <strong>Risk:</strong> Municipal and university procurement tenders take 6–9 months.<br>
          <strong>Mitigation:</strong> First-year contracts (€25k–€40k) fall below the national Finnish public procurement threshold (€60k), allowing direct pilot acquisition without formal competitive tenders.
        </p>
      </div>

      <div class="card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
          <h3 class="card-title" style="color: #c8102e; font-size: 17.5px;">3. Competition from Free LLMs & Google</h3>
          <span class="badge-tag" style="font-size: 11px; padding: 3px 8px;">Market Moat</span>
        </div>
        <p class="card-text" style="font-size: 13.5px;">
          <strong>Risk:</strong> Users paste Kaleva articles into ChatGPT or use Google Translate.<br>
          <strong>Mitigation:</strong> Raw machine translation fails on Finnish civic reality (e.g. <em>Pääkallokeli</em>, <em>PSOAS</em>). Zero-translation visual edge pictograms and 30s Korva audio cannot be replicated by web translation.
        </p>
      </div>

      <div class="card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
          <h3 class="card-title" style="color: #c8102e; font-size: 17.5px;">4. Seasonal Student Churn</h3>
          <span class="badge-tag" style="background: #475569; font-size: 11px; padding: 3px 8px;">Retention</span>
        </div>
        <p class="card-text" style="font-size: 13.5px;">
          <strong>Risk:</strong> Students graduate and leave, causing user engagement to fluctuate.<br>
          <strong>Mitigation:</strong> B2B licenses are institutional and prepaid annually. Every autumn, a fresh cohort of 1,500+ new international students automatically inherits active access during orientation week.
        </p>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div>Kaleva Tasku • Commercial Presentation</div>
    <div>Slide 8 of 8</div>
  </div>
</div>

</body>
</html>
"""

with open('business_model_presentation.html', 'w', encoding='utf-8') as f:
    f.write(bm_html)
print("Updated business_model_presentation.html successfully!")

# -------------------------------------------------------------
# 3. UPDATE presentation.html (7 SLIDES WITH LATEST SCREENSHOTS)
# -------------------------------------------------------------
# Read original presentation.html and update Slide 3 with both latest screenshots!
with open('presentation.html', 'r', encoding='utf-8') as f:
    orig_pres = f.read()

# Replace the old image block on Slide 3
import re
# Look for <div class="screenshot-frame" ... <img src="data:image/png;base64,... /> </div>
new_slide3_content = f"""<div style="display: grid; grid-template-columns: 0.88fr 1.12fr; gap: 32px; align-items: center;">
      <div style="display: flex; flex-direction: column; gap: 16px;">
        <div class="card-highlight">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <h3 class="card-title">Engine 1: Mobile Tasku View</h3>
            <span class="badge-red">Zero-Translation UX</span>
          </div>
          <p class="card-text">
            Visual situation micro-cards designed for sub-zero Oulu conditions. Features the orange newsroom masthead («KALEVA TASKU • La 24.10.2026»), monochromatic line-art diagrams (Problem ➔ Salad-Green Arrow ➔ Solution), and one-touch civic actions.
          </p>
        </div>

        <div class="card-highlight" style="border-color: #475569;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <h3 class="card-title">Engine 2: Classic Broadsheet 1899</h3>
            <span class="badge-outline">Editorial Authority</span>
          </div>
          <p class="card-text">
            One click on the headline expands into an authentic multi-column newspaper view with deep editorial reporting, journalist bylines, and official JSN § 10 ethics accreditation. We never dumb down journalism.
          </p>
        </div>

        <div class="card-success">
          <h4 style="font-size: 16px; font-weight: 700; color: #166534; margin-bottom: 4px;">Arctic Ergonomics: Korva Audio Stream (30s)</h4>
          <p class="card-text" style="color: #14532d; font-size: 14px;">
            At −20°C at an Oulu bus stop, bare fingers freeze in 40 seconds. A single click on the grey «(30s)» badge streams a high-clarity 30-second audio summary directly into earbuds so gloves stay on.
          </p>
        </div>
      </div>

      <!-- Real Dual-Engine Screenshots -->
      <div style="display: grid; grid-template-columns: 0.85fr 1.15fr; gap: 16px; align-items: center;">
        <div style="text-align: center;">
          <div style="border: 2px solid #002855; border-radius: 18px; overflow: hidden; box-shadow: 0 10px 24px rgba(0,40,85,0.15);">
            <img src="data:image/png;base64,{b64_card}" style="width: 100%; height: auto; display: block;" alt="Engine 1 Tasku" />
          </div>
          <div style="font-size: 12px; font-weight: 700; color: #002855; margin-top: 6px;">Engine 1: Tasku Card</div>
        </div>

        <div style="text-align: center;">
          <div style="border: 2px solid #dedad2; border-radius: 18px; overflow: hidden; box-shadow: 0 10px 24px rgba(0,0,0,0.1);">
            <img src="data:image/png;base64,{b64_broadsheet}" style="width: 100%; height: auto; display: block;" alt="Engine 2 Broadsheet" />
          </div>
          <div style="font-size: 12px; font-weight: 700; color: #002855; margin-top: 6px;">Engine 2: Broadsheet 1899</div>
        </div>
      </div>
    </div>"""

# Replace the entire grid-2-custom on Slide 3
orig_pres_updated = re.sub(
    r'<div class="grid-2-custom">[\s\S]*?</div>\s*</div>\s*</div>\s*<div class="slide-footer">\s*<div>Kaleva Tasku • Executive Presentation</div>\s*<div>Slide 3 of 7</div>',
    new_slide3_content + '\n  </div>\n\n  <div class="slide-footer">\n    <div>Kaleva Tasku • Executive Presentation</div>\n    <div>Slide 3 of 7</div>',
    orig_pres
)

with open('presentation.html', 'w', encoding='utf-8') as f:
    f.write(orig_pres_updated)
print("Updated presentation.html with dual-engine screenshots successfully!")
