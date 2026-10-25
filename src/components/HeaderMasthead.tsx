import React from 'react';

interface HeaderMastheadProps {
  isPlayingAudio?: boolean;
  onToggleAudio?: () => void;
}

export const HeaderMasthead: React.FC<HeaderMastheadProps> = () => {
  return (
    <header className="w-full bg-white border-b-2 border-[#dedad2] shadow-xs sticky top-0 z-40">
      {/* Topmost Grey Line (без текста) */}
      <div className="h-1.5 bg-[#f0ece4] border-b border-[#e2ded4]" />

      {/* Main Brand Row (Exact kaleva.fi style: Black Serif Wordmark) */}
      <div className="max-w-4xl mx-auto px-4 py-2.5 flex items-center justify-between gap-4">
        {/* Kaleva Logo Wordmark */}
        <div className="flex items-center gap-3">
          <a href="https://www.kaleva.fi" target="_blank" rel="noreferrer" className="flex items-baseline gap-2 group">
            <span className="text-3xl sm:text-4xl font-serif font-black tracking-tight text-[#000000] uppercase hover:text-[#cf2e2e] transition-colors">
              Kaleva
            </span>
            <span className="text-[10px] font-mono font-black uppercase tracking-wider px-2 py-0.5 rounded bg-[#cf2e2e] text-white">
              Tasku
            </span>
          </a>
          <span className="hidden sm:inline-block text-[11px] text-[#5c5852] font-serif italic border-l border-slate-300 pl-3">
            Oululaisten arjen tulkki ja suora uutisvirta
          </span>
        </div>
      </div>
    </header>
  );
};
