# Kaleva Vox: Обзор проекта и презентация (на русском языке)

## 1. Вводный брифинг для напарника: Суть хакатона и проекта

### Что за челлендж и какая проблема?
Мы участвуем в треке **Challenge 2: «News for Everyone»** от главного медиа-холдинга Северной Финляндии — **Kaleva Media**.

**В чём реальная боль:**
В Оулу и Лапландии живут тысячи иностранцев: студенты универа Оулу, инженеры Nokia, сезонные рабочие на курортах (в Леви). 
* Они **не знают финского языка** и газету *Kaleva* не читают.
* Когда в городе что-то случается (забастовка автобусов, сирены в центре, мороз -25°C, проблемы с арендой жилья), иностранцы не знают, что делать. Они сидят в своих чатиках WhatsApp или анонимном приложении *Jodel*, ловят панику и верят фейкам.
* Обычный Google Translate не помогает: он тупо переводит слова, но **не объясняет финские реалии и законы**.

**Задача от Kaleva:** Сделать умную многоязычную систему, которая доносит проверенные новости до иностранцев, соблюдает жесткую финскую журналистскую этику (кодекс JSN) и окупается финансово.

---

### Что мы построили (проект «Kaleva Vox»)
Мы сделали не просто «сайт с ChatGPT», а **автономную мини-редакцию из трёх агентов с человеком во главе**:

1. **Агент «Радар» (Tutkija):**
   * В реальном времени мониторит входящие слухи от жителей, официальные открытые данные города Оулу (`api.ouka.fi`) и живой RSS-поток самой газеты Kaleva. 
   * Срезает любые личные данные (GDPR) и привязывает новость к району (Туйра, Линнанмаа, Леви).

2. **Агент «Этика» (JSN Auditor):**
   * Проверяет слух по финскому кодексу журналистики.
   * **Показывает открытую математику доверия** (жюри от этого кайфанет): 
     * *+40%* — совпало с базой спасателей/полиции;
     * *+35%* — подтвердили 3 свидетеля рядом;
     * *-15%* — штраф, если источник анонимный.
     * Итог: 60% $\rightarrow$ отправляет на ручную проверку редактору.

3. **Агент «Голос & Культурный декодер» (Toimittaja):**
   * Выдает 3 короткие пули на английском, финском, простом финском (Selkosuomi) и саамском.
   * **Главная киллер-фича — Культурный декодер:** объясняет разницу между паникой иностранца и финской реальностью.
     * *Пример:* Иностранец слышит 4 сирены у молла Valkea и думает, что это теракт. Декодер объясняет: в Финляндии по закону на подгоревший тост в кафе обязаны выехать 3 пожарные машины. Опасности нет.
     * *Пример:* Хозяин квартиры в Леви требует 1200€ наличными за ключи. Декодер сразу выдает: по закону Финляндии об аренде брать наличку незаконно, только через банковский счет.

4. **Пульт главного редактора (Cockpit):**
   * В системе всегда есть **человек (Human-in-the-loop)**. Ни одна новость не уходит в эфир без клика редактора.

---

### Чем мы добиваем конкурентов (козыри для жюри):

* **«AI Incompetence Boundary» (Защита от дурака):** 
  Если иностранец спрашивает что-то жесткое (например: *«Работодатель забрал мой паспорт, что делать?»* или угроза насилия) — наш ИИ **не строит из себя юриста**. Он мгновенно блокирует публикацию и выводит экстренные кнопки прямой связи: полиция 112, служба помощи жертвам преступлений (*Rikosuhripäivystys 116 006*) и инспекция труда.
* **«The Reverse Scoop» (Обратные эксклюзивы для финнов):** 
  Финские журналисты не сидят в чатах иностранных сезонных рабочих. Наша система находит проблемы иностранцев (например, в общежитиях отключили отопление) и одной кнопкой передает готовый сюжет финским репортерам Калевы на первую полосу.
* **Аудио-сводка «Korva» (для мороза):** 
  В -20°C на автобусной остановке пальцы отмерзают за 40 секунд. Мы сделали 30-секундную озвучку в наушник, а если звук заглушен — на экране сверху идет бегущая строка-телесуфлер.
* **Культурный хоккей (Kärpät):** 
  Интегрировали официальный живой API хоккейной лиги (`Liiga.fi`). Новичкам объясняют не просто счет матча, а местный культ хоккея.
* **Бизнес-модель (€114 000 в год):** 
  Мы не просим бедных студентов платить за подписку. Платят институты:
  * **Университет Оулу (€35k/год)** — чтобы иностранные студенты не бросали учебу из-за изоляции.
  * **Nokia (€25k/год)** — корпоративная интеграция в Slack для иностранных айтишников.
  * **Оулу 2026 (€40k/год)** — культурная столица Европы (300 тысяч туристов).
  * **Расходы:** всего €18 240 в год на сервера и оплату студентам-проверяльщикам. **Один клиент окупает весь проект с первого дня.**

---

## 2. Executive 6-Slide Presentation Deck

### Presentation: Evolving Kaleva for the Next Generation
**Subtitle:** Harmonizing 120 Years of Broadsheet Heritage with Gen Z Ergonomics  
**Format:** 6 Slides | Executive Briefing

---

#### Slide 1: The Strategic Dilemma
**Headline:** Regional media does not have a relevance crisis — it has a packaging crisis.

* **The Paradox in Finland:**
  * Total news brand reach remains exceptionally high at 94% (KMT / Reuters Institute).
  * Print circulation dropped by ~40% over the past decade (e.g., Kaleva: 70k down to ~42k; Sunday print discontinued in 2023).
  * Gen Z (18–28) relies on smartphones and social channels (Jodel, TikTok), bypassing traditional paywalled front pages.
* **The Fatal Trap:**
  * Trying to "become TikTok" alienates high-paying loyal subscribers (80%+ of revenue).
  * Ignoring youth guarantees a terminal subscriber cliff within 10–15 years.
* **Strategic Objective:**
  * Expand audience reach and digital habit-formation among youth without diluting Kaleva's trusted journalistic authority.

---

#### Slide 2: Architecture: Why Segmented Apps Fail
**Headline:** Do not build three separate apps — build one Modular Content Architecture.

* **The "Three-Cohort" Pitfall:**
  * Splitting platforms into older, middle, and younger apps triples editorial overhead and creates a patronizing "youth ghetto" that Gen Z actively rejects.
* **The Proven Solution: Modular (Atomic) Journalism (BBC News Labs / Yle Model):**
  * Deconstruct a single story into dynamic, self-contained layers:
    * **Layer 1 (Top / Snackable):** 3-bullet factual TL;DR + 30-sec audio clip (for fast-moving youth).
    * **Layer 2 (Middle / Explainer):** "Why it matters right now" context block.
    * **Layer 3 (Deep / Core Journalism):** Full investigative reporting, legal nuances, and long-form analysis.
* **Key Takeaway:** One newsroom, one verified database, dynamic user-selected depth.

---

#### Slide 3: Research Foundations: How Gen Z Consumes Information
**Headline:** Designing for behavior grounded in Oxford Reuters Institute and Nordic media studies.

1. **Countering "News Avoidance":**
   * Youth tune out because traditional coverage produces anxiety and fatalism.
   * *Requirement:* Adopt Solutions Journalism — pair every local problem with concrete civic action and resource links.
2. **"Snacking & Monitoring" over Linear Reading:**
   * Young audiences scan environments for immediate utility (transit, campus safety, extreme weather).
   * *Requirement:* Crucial signals must be decodable in 5 seconds on screen or 15 seconds in headphones.
3. **The Explainer Imperative:**
   * Youth have not tracked municipal council dynamics for 20 years.
   * *Requirement:* Every local political report must define the baseline: "Who are the stakeholders, and how does this affect my daily life?"

---

#### Slide 4: Aesthetic Blueprint: "Editorial Brutalism with Nordic Minimalism"
**Headline:** Modernizing visual ergonomics without sacrificing broadsheet dignity.

* **Retain the Historic Anchor:**
  * Preserve Kaleva’s century-old classical serif masthead — the recognized symbol of verified civic truth.
* **Ergonomic Card-Based Design:**
  * Replace dense walls of gray text with high-contrast, modular cards using clean sans-serif typography (Inter / Neue Haas Grotesk).
  * Native OLED Dark Mode designed for Northern Ostrobothnia's dark winter daylight hours.
* **Tactile Micro-Interactions:**
  * Fluid swipe gestures and haptic feedback on saves and shares.
  * Zero condescension: no cartoonish emojis, childish illustrations, or artificial slang. Gen Z demands clean, high-utility tools.

---

#### Slide 5: Four High-Impact Product Innovations
**Headline:** Translating media theory into tangible, competitive features.

1. **Zero-Screen Audio Engine (Korva):**
   * Instant 30-second localized voice briefings streamed to AirPods. Solves Oulu's sub-zero winter friction (operating screens with thick gloves at −15°C).
2. **Community Rumor Radar with Visible Fact-Checking:**
   * Live status board for local rumors (Unverified ➔ Investigating ➔ Corroborated). Gen Z trusts evidence transparency over editorial declarations.
3. **One-Tap Language Accessibility:**
   * Instant toggle between Finnish, English, and Easy Finnish (Selkosuomi). Bridges the gap for Oulu's 5,000+ international students and tech engineers.
4. **Student SSO Onboarding Funnel:**
   * Free access to real-time civic utility; subsidized digital tiers via University of Oulu / Oamk logins. Build habitual brand trust during studies; monetize at graduation.

---

#### Slide 6: Strategic Roadmap: The Evolution of Kaleva
**Headline:** From a passive chronicler of yesterday to a real-time navigator of Oulu.

* **The Dual-Engine Value Proposition:**
  * **Top of Funnel (Free Utility Layer):** Real-time alerts, rumor verification, transit updates, and audio micro-briefings capture daily attention across all demographics.
  * **Core Engine (Premium Investigation Layer):** In-depth local investigative reporting, cultural analysis, and weekend slow-journalism print editions sustain direct subscription revenue.
* **The Bottom Line:**
  * Kaleva does not need to compromise its high journalistic standards to win Gen Z. By delivering verified truth at mobile speed, Kaleva secures its civic and financial relevance for the next century.

---

## 3. Версия главного редактора Kaleva (Аутентичный стиль редакции)

* **Tervehdys Oulusta!** Подлинный визуальный и смысловой дух газеты Kaleva (*Pohjoisen puolesta vuodesta 1899*):
  * **Аутентичная стилистика Broadsheet:** классическая газетная сетка, фирменный антиквенный логотип Kaleva, благородные разделительные линейки, датировки (Oulu, Technopolis Peltola), фирменный бордово-кирпичный оттенок (*Kaleva Punainen*) и редакционные штампы-плашки.
  * **Тон главного редактора:** строгий, принципиальный, без заигрывания со сленгом, с пониманием арктического быта Оулу (−18°C, велосипед по зимней Баане, варежки на остановке в Туйре) и технологий.

### Структура 6 слайдов редактора:
1. **Pääkirjoitus / Manifesti — Totuus ei vanhene:** Доверие 94% населения, падение тиража бумаги до 42 000, перенос журналистского стержня в карман и наушники.
2. **Toimituksen arkkitehtuuri — Modulaarinen journalismi:** Отказ от деления на 3 отдельных приложения, переход к 3-уровневой модульной структуре BBC/Yle.
3. **Pohjoinen todellisuus: Pakkanen ja KORVA-äänimoottori:** Суровый климат Оулу: 30-секундный голосовой брифинг KORVA в наушники перед посадкой в автобус.
4. **Huhututka: Kuinka lyömme Jodelin ja Telegramin:** Прозрачная цепочка проверки фактов: vinkkilinja + Fintraffic + OSL + 112.
5. **Kansainvälinen Oulu: 5 000 unohdettua lukijaa Linnanmaalla:** Тоггл Suomi / English / Selkosuomi для 5000+ иностранных студентов и инженеров Nokia/Oura + доступ Haka-SSO.
6. **Kahden moottorin Kaleva: Arjen uutisapu ja arvovalta:** Бесплатный утилитарный слой для молодежи + премиальная подписка на расследования.
