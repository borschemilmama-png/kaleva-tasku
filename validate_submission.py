# Submission Fields Validator & Generator

project_name = "Kaleva Tasku"

punchline = "A community-driven, agentic civic newsroom bridging 125 years of Kaleva's trusted journalism with zero-translation visual situation diagrams and 30s arctic audio for Oulu's international community."

description = """## 🎯 The Strategic Problem
Oulu is home to 5,000+ international residents: degree students at the University of Oulu and OAMK, high-tech engineers at Nokia and Oura, and seasonal workers in Lapland.
1. **The Arctic Information Desert:** When local emergencies strike—sub-zero (−25°C) transit halts, sirens at Kauppakeskus Valkea, or Baana cycling ice hazards—non-Finnish residents cannot read traditional Finnish broadsheets.
2. **Panic & Rumors in WhatsApp & Jodel:** Lacking trusted English channels, foreigners rely on anonymous forums where misinformation and panic spread within minutes.
3. **Failure of Raw Machine Translation:** Generic tools (Google Translate) translate literal words but fail on Finnish civic reality. Terms like *Pääkallokeli*, *Baana*, *PSOAS*, or *Kela* carry statutory legal, housing, and safety context that literal translation distorts.

---

## 💡 The Solution: Kaleva Tasku
**Kaleva Tasku** is a community-driven, agentic civic newsroom that bridges 125 years of Kaleva Media's trusted journalism with visual-first ergonomics for multilingual communities.

### 🔄 The Dual-Engine Model (Never Dumbing Down Journalism)
We do not alienate Kaleva's loyal subscribers. We run two synchronized engines:
* **Engine 1 — Tasku Mobile Micro-Cards:** Fast, swipeable card ergonomics with zero-translation situation diagrams for Gen Z, expats, and international students.
* **Engine 2 — Classic Broadsheet 1899:** One tap on any headline expands the story into an authentic multi-column newspaper layout with deep investigative reporting, verified journalist bylines, and official JSN ethics accreditation.

---

## 🚀 Key Product Innovations
1. **Monochromatic Line-Art Situation Diagrams:** No generic stock photography or distracting emojis. Each card features a high-clarity line-art diagram showing the incident on the left (e.g. Highway 4 snow collision), a vibrant salad-green arrow, and the immediate solution on the right (Kaakkuri interchange ➔ 45 min clear). Comprehension takes under 2 seconds.
2. **Arctic Ergonomics (Korva Audio Stream):** At −20°C at an Oulu bus stop, bare fingers freeze in 40 seconds. A single click on the grey `(30s)` badge streams a high-clarity 30-second audio summary directly into wireless earbuds so winter gloves stay on.
3. **Actionable Civic Solutions:** News must resolve anxiety, not induce it. Every card terminates in an actionable button: real-time Fintraffic detour alerts, OSL live bus tracking, Police 112 incident status, and Kivisydän underground warm garden access.
4. **Authentic Editorial Identity:** Clean top orange banner (`KALEVA TASKU • La 24.10.2026`) anchoring the content in Kaleva's trusted heritage.

---

## 🤖 3-Agent Editorial Pipeline + Human Cockpit
Our background agentic pipeline automates speed without violating the Council for Mass Media (JSN) guidelines:
* **Agent 1 — Ingest & Triage:** Monitors open civic feeds (`api.ouka.fi`, Fintraffic, Kaleva RSS), scrubs personal data (GDPR), and geo-clusters events by Oulu district.
* **Agent 2 — Ergonomic Synthesizer:** Condenses complex reporting into visual micro-cards, monochromatic situation diagrams, and 30s audio briefs.
* **Agent 3 — JSN Ethics Verifier:** Calculates an open verification trust score (+40% official rescue/police match, +35% corroborated by geotagged witnesses) conforming to JSN § 10 & § 20.
* **Human-in-the-Loop Cockpit:** No article publishes autonomously. Kaleva's desk editors maintain final sign-off with 1-click verification.

---

## 💼 Business Model: €114,000 Institutional ARR
We never charge low-income students. Institutions that depend on international safety fund the platform:
* **University of Oulu & OAMK:** €35,000/yr (Student retention, winter safety, duty-of-care).
* **Nokia & ICT Corporates:** €25,000/yr (Turnkey expat onboarding Slack/Teams integration).
* **Oulu 2026 Foundation & City:** €40,000/yr (European Capital of Culture 300,000 visitors).
* **Lapland Tourism Consortia:** €14,000/yr (Seasonal worker safety in Levi/Ruka corridor).
* **Lean Operating Costs:** €18,240/yr ➔ **84% Gross Margin**. Day 1 breakeven with client #1.
* **Zero Cannibalization:** Tasku funnels international readers into full €19/mo Kaleva digital subscriptions.

---

## 🛠️ Tech Stack & Readiness
* **Frontend:** React 18, TypeScript, TailwindCSS, Lucide Icons, Vite
* **Voice Engine:** Web Speech API (real-time spoken audio synthesis)
* **Status:** Production-ready prototype tested with real Oulu scenarios."""

print("Project Name length:", len(project_name), "/ 30")
print("Punchline length:", len(punchline), "/ 200")
print("Description length:", len(description), "/ 5000")

assert len(project_name) <= 30
assert len(punchline) <= 200
assert len(description) <= 5000
print("ALL LIMITS SATISFIED PERFECTLY!")
