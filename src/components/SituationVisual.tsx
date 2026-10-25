import React from 'react';

interface SituationVisualProps {
  storyId?: string;
  type: 'problem' | 'solution';
  isResolved?: boolean;
  language?: string;
}

export const SituationVisual: React.FC<SituationVisualProps> = ({
  storyId,
  type,
  isResolved
}) => {
  // 1. STORY 1: VT4 KAAKKURI (HIGHWAY SPILLED CARGO & DETOUR)
  if (storyId === 'story-1-kaakkuri-vt4') {
    if (type === 'problem') {
      return (
        <div className="w-full h-[92px] sm:h-[100px] rounded-xl overflow-hidden border border-slate-200 bg-slate-50/90 p-2 flex flex-col justify-between select-none shadow-2xs text-slate-800">
          {/* Monochromatic Line Art: Blocked Highway with Spilled Truck Cargo */}
          <div className="relative w-full flex-1 flex items-center justify-center">
            <svg className="w-full h-11" viewBox="0 0 160 48" fill="none" stroke="currentColor" strokeLinecap="round" strokeLinejoin="round">
              {/* Road lane line */}
              <line x1="4" y1="42" x2="156" y2="42" strokeWidth="1.5" />
              <line x1="6" y1="42" x2="154" y2="42" strokeWidth="1.2" strokeDasharray="6 4" opacity="0.6" />

              {/* Truck Outline */}
              <rect x="8" y="16" width="46" height="22" rx="2" strokeWidth="1.6" />
              <path d="M54 22 H68 L76 30 V38 H54 V22 Z" strokeWidth="1.6" />
              <circle cx="20" cy="38" r="4" strokeWidth="1.5" />
              <circle cx="42" cy="38" r="4" strokeWidth="1.5" />
              <circle cx="64" cy="38" r="4" strokeWidth="1.5" />
              <line x1="22" y1="18" x2="22" y2="34" strokeWidth="1" strokeDasharray="2 2" />

              {/* Spilled Cargo Box Outlines */}
              <rect x="84" y="28" width="10" height="10" rx="1" strokeWidth="1.4" />
              <line x1="84" y1="28" x2="94" y2="38" strokeWidth="1" opacity="0.4" />
              <rect x="98" y="26" width="11" height="11" rx="1" strokeWidth="1.4" />
              <rect x="92" y="18" width="10" height="10" rx="1" strokeWidth="1.4" />

              {/* Traffic Cone Outlines */}
              <polygon points="122,20 116,42 128,42" strokeWidth="1.5" />
              <line x1="118" y1="34" x2="126" y2="34" strokeWidth="1.2" />
              <polygon points="138,20 132,42 144,42" strokeWidth="1.5" />
              <line x1="134" y1="34" x2="142" y2="34" strokeWidth="1.2" />

              {/* Lane blocked cross badge */}
              <circle cx="150" cy="14" r="6" strokeWidth="1.5" />
              <path d="M146 10 L154 18 M154 10 L146 18" strokeWidth="1.5" />
            </svg>
          </div>

          {/* Minimal Line-Art Status Badge */}
          <div className="border border-slate-200 bg-white/90 rounded-md px-2 py-0.5 flex items-center justify-between">
            <span className="text-[9px] font-mono font-bold text-slate-700 tracking-wider uppercase flex items-center gap-1.5">
              <span className="w-1.5 h-1.5 rounded-full bg-slate-700 inline-block" />
              VT4 Kaakkuri • Kaista suljettu
            </span>
            <span className="text-[9px] font-mono font-bold text-slate-500">2 km jono</span>
          </div>
        </div>
      );
    } else {
      // VT4 Detour Line Art
      return (
        <div className="w-full h-[92px] sm:h-[100px] rounded-xl overflow-hidden border border-slate-200 bg-slate-50/90 p-2 flex flex-col justify-between select-none shadow-2xs text-slate-800">
          <div className="relative w-full flex-1 flex items-center justify-center">
            <svg className="w-full h-11" viewBox="0 0 160 48" fill="none" stroke="currentColor" strokeLinecap="round" strokeLinejoin="round">
              {/* Straight Road with Blocked Cross */}
              <line x1="10" y1="38" x2="150" y2="38" strokeWidth="1.5" strokeDasharray="4 4" opacity="0.4" />
              <line x1="68" y1="33" x2="88" y2="43" strokeWidth="2" />
              <line x1="88" y1="33" x2="68" y2="43" strokeWidth="2" />

              {/* Sweeping Detour Route Arrow */}
              <path d="M25 38 C 45 38, 55 14, 85 14 L 140 14" strokeWidth="2" />
              <polyline points="135 9 142 14 135 19" strokeWidth="2" />

              {/* Moving Car Outline on Detour */}
              <rect x="74" y="9" width="22" height="10" rx="2" strokeWidth="1.5" />
              <path d="M78 9 L82 4 H90 L93 9" strokeWidth="1.4" />
              <circle cx="79" cy="19" r="2.5" strokeWidth="1.4" />
              <circle cx="91" cy="19" r="2.5" strokeWidth="1.4" />

              {/* Checkmark circle */}
              <circle cx="146" cy="34" r="6.5" strokeWidth="1.5" />
              <polyline points="143 34 146 37 150 31" strokeWidth="1.5" />
            </svg>
          </div>

          <div className="border border-slate-200 bg-white/90 rounded-md px-2 py-0.5 flex items-center justify-between">
            <span className="text-[9px] font-mono font-bold text-slate-700 tracking-wider uppercase flex items-center gap-1.5">
              <span className="w-1.5 h-1.5 rounded-full bg-slate-700 inline-block" />
              Kaakkurin ramppi • Reitti vapaa
            </span>
            <span className="text-[9px] font-mono font-bold text-slate-500">Säästä 20 min</span>
          </div>
        </div>
      );
    }
  }

  // 2. STORY 2: ROTUAARI NIGHT DISTURBANCE (RESOLVED)
  if (storyId === 'story-2-rotuaari-police') {
    if (type === 'problem') {
      return (
        <div className="w-full h-[92px] sm:h-[100px] rounded-xl overflow-hidden border border-slate-200 bg-slate-50/90 p-2 flex flex-col justify-between select-none shadow-2xs text-slate-800">
          <div className="relative w-full flex-1 flex items-center justify-center">
            <svg className="w-full h-11" viewBox="0 0 160 48" fill="none" stroke="currentColor" strokeLinecap="round" strokeLinejoin="round">
              {/* Street Lantern Outline */}
              <line x1="20" y1="8" x2="20" y2="44" strokeWidth="1.6" />
              <path d="M14 14 C14 8, 26 8, 26 14 Z" strokeWidth="1.4" />
              <polygon points="20,14 12,42 28,42" strokeWidth="1" opacity="0.3" strokeDasharray="2 2" />

              {/* Outline Police Cruiser */}
              <rect x="45" y="22" width="50" height="16" rx="2" strokeWidth="1.6" />
              <path d="M55 22 L62 12 H78 L85 22" strokeWidth="1.5" />
              <circle cx="58" cy="38" r="3.5" strokeWidth="1.5" />
              <circle cx="82" cy="38" r="3.5" strokeWidth="1.5" />
              <rect x="67" y="8" width="8" height="4" rx="1" strokeWidth="1.4" />

              {/* Police caution perimeter barrier */}
              <rect x="108" y="24" width="42" height="14" strokeWidth="1.5" strokeDasharray="5 3" />
              <line x1="114" y1="24" x2="114" y2="42" strokeWidth="1.5" />
              <line x1="144" y1="24" x2="144" y2="42" strokeWidth="1.5" />
              <line x1="108" y1="31" x2="150" y2="31" strokeWidth="1" />
            </svg>
          </div>

          <div className="border border-slate-200 bg-white/90 rounded-md px-2 py-0.5 flex items-center justify-between">
            <span className="text-[9px] font-mono font-bold text-slate-700 tracking-wider uppercase flex items-center gap-1.5">
              <span className="w-1.5 h-1.5 rounded-full bg-slate-700 inline-block" />
              Rotuaari • Poliisi paikalla
            </span>
            <span className="text-[9px] font-mono font-bold text-slate-500">Häiriötila</span>
          </div>
        </div>
      );
    } else {
      // Resolved Rotuaari Line Art
      return (
        <div className="w-full h-[92px] sm:h-[100px] rounded-xl overflow-hidden border border-slate-200 bg-slate-50/90 p-2 flex flex-col justify-between select-none shadow-2xs text-slate-800">
          <div className="relative w-full flex-1 flex items-center justify-center">
            <svg className="w-full h-11" viewBox="0 0 160 48" fill="none" stroke="currentColor" strokeLinecap="round" strokeLinejoin="round">
              {/* Street Facades Line Art */}
              <rect x="15" y="14" width="26" height="30" strokeWidth="1.4" />
              <rect x="47" y="20" width="30" height="24" strokeWidth="1.4" />
              <rect x="118" y="16" width="28" height="28" strokeWidth="1.4" />

              {/* Large Outline Security Shield with Checkmark */}
              <path d="M96 8 L110 13 V24 C110 34, 96 41, 96 41 C96 41, 82 34, 82 24 V13 Z" strokeWidth="1.8" />
              <polyline points="89 23 94 28 103 18" strokeWidth="2" />
            </svg>
          </div>

          <div className="border border-slate-200 bg-white/90 rounded-md px-2 py-0.5 flex items-center justify-between">
            <span className="text-[9px] font-mono font-bold text-slate-700 tracking-wider uppercase flex items-center gap-1.5">
              <span className="w-1.5 h-1.5 rounded-full bg-slate-700 inline-block" />
              Tilanne ratkaistu • Turvallinen
            </span>
            <span className="text-[9px] font-mono font-bold text-slate-500">Keskusta rauhallinen</span>
          </div>
        </div>
      );
    }
  }

  // 3. STORY 3: OULUNSALO CAR FIRE (RESOLVED)
  if (storyId === 'story-3-oulunsalo-fire') {
    if (type === 'problem') {
      return (
        <div className="w-full h-[92px] sm:h-[100px] rounded-xl overflow-hidden border border-slate-200 bg-slate-50/90 p-2 flex flex-col justify-between select-none shadow-2xs text-slate-800">
          <div className="relative w-full flex-1 flex items-center justify-center">
            <svg className="w-full h-11" viewBox="0 0 160 48" fill="none" stroke="currentColor" strokeLinecap="round" strokeLinejoin="round">
              {/* House outline */}
              <polygon points="28,12 8,26 48,26" strokeWidth="1.5" />
              <rect x="14" y="26" width="28" height="16" strokeWidth="1.5" />
              <rect x="23" y="32" width="10" height="10" strokeWidth="1.2" />

              {/* Car with open hood & flame lines */}
              <rect x="65" y="26" width="52" height="14" rx="2" strokeWidth="1.5" />
              <path d="M75 26 L84 16 H102 L108 26" strokeWidth="1.4" />
              <circle cx="78" cy="40" r="3.5" strokeWidth="1.5" />
              <circle cx="106" cy="40" r="3.5" strokeWidth="1.5" />

              {/* Raised hood */}
              <line x1="104" y1="26" x2="118" y2="16" strokeWidth="1.6" />

              {/* Flame & Smoke line contours */}
              <path d="M110 14 C108 8, 114 6, 112 2 C117 4, 119 9, 115 14 Z" strokeWidth="1.5" />
              <path d="M120 14 C118 10, 122 8, 121 4 C124 6, 125 11, 123 14 Z" strokeWidth="1.2" />
              <path d="M128 16 C126 12, 132 10, 130 6 C134 8, 135 13, 132 16 Z" strokeWidth="1.2" opacity="0.6" />
            </svg>
          </div>

          <div className="border border-slate-200 bg-white/90 rounded-md px-2 py-0.5 flex items-center justify-between">
            <span className="text-[9px] font-mono font-bold text-slate-700 tracking-wider uppercase flex items-center gap-1.5">
              <span className="w-1.5 h-1.5 rounded-full bg-slate-700 inline-block" />
              Oulunsalo • Autopalo pihalla
            </span>
            <span className="text-[9px] font-mono font-bold text-slate-500">Pelastustehtävä</span>
          </div>
        </div>
      );
    } else {
      // Extinguished with Snow Line Art
      return (
        <div className="w-full h-[92px] sm:h-[100px] rounded-xl overflow-hidden border border-slate-200 bg-slate-50/90 p-2 flex flex-col justify-between select-none shadow-2xs text-slate-800">
          <div className="relative w-full flex-1 flex items-center justify-center">
            <svg className="w-full h-11" viewBox="0 0 160 48" fill="none" stroke="currentColor" strokeLinecap="round" strokeLinejoin="round">
              {/* Car Safe with Snow Outline on Hood */}
              <rect x="20" y="26" width="52" height="14" rx="2" strokeWidth="1.5" />
              <path d="M30 26 L39 16 H57 L63 26" strokeWidth="1.4" />
              <circle cx="33" cy="40" r="3.5" strokeWidth="1.5" />
              <circle cx="61" cy="40" r="3.5" strokeWidth="1.5" />

              {/* Snow drift contour over engine */}
              <path d="M60 26 C62 20, 76 20, 78 26 Z" strokeWidth="1.5" strokeDasharray="3 2" />
              <path d="M66 18 C66 14, 70 12, 70 8" strokeWidth="1.2" strokeDasharray="2 2" />

              {/* Outline Safety Shield */}
              <path d="M115 8 L130 13 V24 C130 34, 115 41, 115 41 C115 41, 100 34, 100 24 V13 Z" strokeWidth="1.8" />
              <polyline points="107 23 113 29 123 18" strokeWidth="2" />
            </svg>
          </div>

          <div className="border border-slate-200 bg-white/90 rounded-md px-2 py-0.5 flex items-center justify-between">
            <span className="text-[9px] font-mono font-bold text-slate-700 tracking-wider uppercase flex items-center gap-1.5">
              <span className="w-1.5 h-1.5 rounded-full bg-slate-700 inline-block" />
              Sammutettu lumella • Vaara ohi
            </span>
            <span className="text-[9px] font-mono font-bold text-slate-500">Talo turvassa</span>
          </div>
        </div>
      );
    }
  }

  // 4. STORY 4: MUSTA JÄÄ & OULUN BAANA
  if (storyId === 'story-4-osl-liukkaus-baana') {
    if (type === 'problem') {
      return (
        <div className="w-full h-[92px] sm:h-[100px] rounded-xl overflow-hidden border border-slate-200 bg-slate-50/90 p-2 flex flex-col justify-between select-none shadow-2xs text-slate-800">
          <div className="relative w-full flex-1 flex items-center justify-center">
            <svg className="w-full h-11" viewBox="0 0 160 48" fill="none" stroke="currentColor" strokeLinecap="round" strokeLinejoin="round">
              {/* Ice Crystal Outline */}
              <line x1="25" y1="8" x2="25" y2="40" strokeWidth="1.6" />
              <line x1="9" y1="24" x2="41" y2="24" strokeWidth="1.6" />
              <line x1="14" y1="13" x2="36" y2="35" strokeWidth="1.3" />
              <line x1="14" y1="35" x2="36" y2="13" strokeWidth="1.3" />
              <polyline points="21 13 25 9 29 13" strokeWidth="1.3" />
              <polyline points="21 35 25 39 29 35" strokeWidth="1.3" />

              {/* City Bus Outline with Skid Tracks */}
              <rect x="60" y="16" width="76" height="22" rx="2" strokeWidth="1.6" />
              <rect x="66" y="20" width="16" height="8" rx="1" strokeWidth="1.2" />
              <rect x="88" y="20" width="16" height="8" rx="1" strokeWidth="1.2" />
              <rect x="110" y="20" width="16" height="8" rx="1" strokeWidth="1.2" />
              <circle cx="78" cy="38" r="4" strokeWidth="1.5" />
              <circle cx="122" cy="38" r="4" strokeWidth="1.5" />

              {/* Skid lines on icy asphalt */}
              <path d="M46 42 C60 40, 72 44, 86 42" strokeWidth="1.3" strokeDasharray="3 2" />
            </svg>
          </div>

          <div className="border border-slate-200 bg-white/90 rounded-md px-2 py-0.5 flex items-center justify-between">
            <span className="text-[9px] font-mono font-bold text-slate-700 tracking-wider uppercase flex items-center gap-1.5">
              <span className="w-1.5 h-1.5 rounded-full bg-slate-700 inline-block" />
              Musta jää ajoradoilla
            </span>
            <span className="text-[9px] font-mono font-bold text-slate-500">OSL +15 min</span>
          </div>
        </div>
      );
    } else {
      // Baana Cycling Superhighway Line Art
      return (
        <div className="w-full h-[92px] sm:h-[100px] rounded-xl overflow-hidden border border-slate-200 bg-slate-50/90 p-2 flex flex-col justify-between select-none shadow-2xs text-slate-800">
          <div className="relative w-full flex-1 flex items-center justify-center">
            <svg className="w-full h-11" viewBox="0 0 160 48" fill="none" stroke="currentColor" strokeLinecap="round" strokeLinejoin="round">
              {/* Baana Corridor Track Lines */}
              <line x1="8" y1="42" x2="152" y2="42" strokeWidth="1.5" />
              <line x1="8" y1="12" x2="152" y2="12" strokeWidth="1.5" strokeDasharray="4 4" opacity="0.4" />

              {/* Cyclist Outline */}
              <circle cx="68" cy="32" r="8" strokeWidth="1.6" />
              <circle cx="106" cy="32" r="8" strokeWidth="1.6" />
              <path d="M68 32 L80 32 L92 18 L80 18 Z" strokeWidth="1.6" />
              <line x1="92" y1="18" x2="106" y2="32" strokeWidth="1.6" />
              <line x1="80" y1="18" x2="78" y2="13" strokeWidth="1.6" />
              <circle cx="84" cy="9" r="3.5" strokeWidth="1.5" />
              <path d="M84 13 L89 20 L94 18" strokeWidth="1.5" />

              {/* Sweeping broom line marks */}
              <path d="M25 22 L35 32 M30 18 L40 28" strokeWidth="1.2" strokeDasharray="2 2" opacity="0.6" />
              <polyline points="135 24 140 29 148 20" strokeWidth="1.8" />
            </svg>
          </div>

          <div className="border border-slate-200 bg-white/90 rounded-md px-2 py-0.5 flex items-center justify-between">
            <span className="text-[9px] font-mono font-bold text-slate-700 tracking-wider uppercase flex items-center gap-1.5">
              <span className="w-1.5 h-1.5 rounded-full bg-slate-700 inline-block" />
              Oulun Baana • Sula asfaltti
            </span>
            <span className="text-[9px] font-mono font-bold text-slate-500">Suositus</span>
          </div>
        </div>
      );
    }
  }

  // 5. STORY 5: KIVISYDÄN KUUTTAREN PUUTARHA
  if (storyId === 'story-5-kivisydan-kuutar') {
    if (type === 'problem') {
      return (
        <div className="w-full h-[92px] sm:h-[100px] rounded-xl overflow-hidden border border-slate-200 bg-slate-50/90 p-2 flex flex-col justify-between select-none shadow-2xs text-slate-800">
          <div className="relative w-full flex-1 flex items-center justify-center">
            <svg className="w-full h-11" viewBox="0 0 160 48" fill="none" stroke="currentColor" strokeLinecap="round" strokeLinejoin="round">
              {/* City Skyline Outline */}
              <rect x="10" y="18" width="16" height="26" strokeWidth="1.4" />
              <rect x="30" y="10" width="18" height="34" strokeWidth="1.4" />
              <rect x="52" y="22" width="14" height="22" strokeWidth="1.4" />

              {/* Cold Wind Gust Lines */}
              <path d="M72 14 C90 10, 105 20, 125 16 M85 26 C105 22, 120 32, 140 28" strokeWidth="1.5" strokeLinecap="round" />

              {/* Outdoor Thermometer Outline */}
              <rect x="145" y="10" width="8" height="24" rx="4" strokeWidth="1.5" />
              <circle cx="149" cy="36" r="6" strokeWidth="1.5" />
              <line x1="149" y1="20" x2="149" y2="36" strokeWidth="2.5" />
            </svg>
          </div>

          <div className="border border-slate-200 bg-white/90 rounded-md px-2 py-0.5 flex items-center justify-between">
            <span className="text-[9px] font-mono font-bold text-slate-700 tracking-wider uppercase flex items-center gap-1.5">
              <span className="w-1.5 h-1.5 rounded-full bg-slate-700 inline-block" />
              Pakkastuuli ja pimeys ulkona
            </span>
            <span className="text-[9px] font-mono font-bold text-slate-500">−12°C</span>
          </div>
        </div>
      );
    } else {
      // Kuutar's Garden in Kivisydän Line Art
      return (
        <div className="w-full h-[92px] sm:h-[100px] rounded-xl overflow-hidden border border-slate-200 bg-slate-50/90 p-2 flex flex-col justify-between select-none shadow-2xs text-slate-800">
          <div className="relative w-full flex-1 flex items-center justify-center">
            <svg className="w-full h-11" viewBox="0 0 160 48" fill="none" stroke="currentColor" strokeLinecap="round" strokeLinejoin="round">
              {/* Cavern Arch Outline */}
              <path d="M10 44 C20 12, 70 12, 80 44" strokeWidth="1.6" strokeDasharray="3 2" />

              {/* Botanical Lotus Line Art */}
              <circle cx="45" cy="28" r="4" strokeWidth="1.4" />
              <path d="M45 16 C40 22, 40 34, 45 34 C50 34, 50 22, 45 16 Z" strokeWidth="1.4" />
              <path d="M33 28 C39 22, 51 22, 57 28 C51 34, 39 34, 33 28 Z" strokeWidth="1.4" />

              {/* Direct Elevator Tube Outline with +16°C */}
              <rect x="105" y="8" width="34" height="36" rx="2" strokeWidth="1.5" />
              <line x1="105" y1="20" x2="139" y2="20" strokeWidth="1" />
              <text x="122" y="32" fontFamily="monospace" fontSize="9" fontWeight="bold" textAnchor="middle" fill="currentColor" stroke="none">+16°C</text>
            </svg>
          </div>

          <div className="border border-slate-200 bg-white/90 rounded-md px-2 py-0.5 flex items-center justify-between">
            <span className="text-[9px] font-mono font-bold text-slate-700 tracking-wider uppercase flex items-center gap-1.5">
              <span className="w-1.5 h-1.5 rounded-full bg-slate-700 inline-block" />
              Kivisydän • Kuuttaren puutarha
            </span>
            <span className="text-[9px] font-mono font-bold text-slate-500">Hissi Rotuaarilta</span>
          </div>
        </div>
      );
    }
  }

  // DEFAULT / FALLBACK LINE ART
  if (isResolved || type === 'solution') {
    return (
      <div className="w-full h-[92px] sm:h-[100px] rounded-xl overflow-hidden border border-slate-200 bg-slate-50/90 p-2 flex flex-col justify-between select-none shadow-2xs text-slate-800">
        <div className="relative w-full flex-1 flex items-center justify-center gap-2">
          <div className="w-9 h-9 rounded-full border-2 border-slate-700 flex items-center justify-center text-lg text-slate-700">
            ✓
          </div>
          <span className="text-xs font-bold text-slate-700 font-sans">Tilanne ratkaistu</span>
        </div>
        <div className="border border-slate-200 bg-white/90 rounded px-2 py-0.5 text-center text-[9px] font-mono text-slate-600 uppercase">
          Toimintaohje kunnossa
        </div>
      </div>
    );
  }

  return (
    <div className="w-full h-[92px] sm:h-[100px] rounded-xl overflow-hidden border border-slate-200 bg-slate-50/90 p-2 flex flex-col justify-between select-none shadow-2xs text-slate-800">
      <div className="relative w-full flex-1 flex items-center justify-center gap-2">
        <div className="w-9 h-9 rounded-full border-2 border-slate-700 flex items-center justify-center text-base text-slate-700">
          !
        </div>
        <span className="text-xs font-bold text-slate-700 font-sans">Huomioi tilanne</span>
      </div>
      <div className="border border-slate-200 bg-white/90 rounded px-2 py-0.5 text-center text-[9px] font-mono text-slate-600 uppercase">
        Tilannepäivitys
      </div>
    </div>
  );
};
