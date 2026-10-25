import React from 'react';
import { StorySlide, Language } from '../types';
import { DigitalSituationDiagram } from './DigitalSituationDiagram';
import { MapPin, ArrowUpRight, Headphones, Volume2 } from 'lucide-react';

interface StoryCardProps {
  story: StorySlide;
  language: Language;
  onOpenBroadsheet: (story: StorySlide) => void;
  isPlayingAudio?: boolean;
  onToggleAudio?: () => void;
}

export const StoryCard: React.FC<StoryCardProps> = ({
  story,
  language,
  onOpenBroadsheet,
  isPlayingAudio,
  onToggleAudio,
}) => {
  return (
    <div className="w-full h-full flex flex-col bg-white text-slate-900 rounded-[32px] border-2 border-slate-200 shadow-xl overflow-hidden relative select-none">
      {/* Main Card Viewport */}
      <div className="flex-1 flex flex-col px-4 sm:px-5 pt-3 sm:pt-3.5 pb-1 sm:pb-1.5 overflow-hidden">
        {/* СТРОЧКА KALEVA TASKU (слева KALEVA TASKU, справа Lauantai 24.10.2026) */}
        <div className="w-full h-9 sm:h-9.5 rounded-xl bg-[#ff8533] px-3 sm:px-3.5 flex items-center justify-between mb-2 shrink-0 shadow-xs">
          {/* Левая часть: KALEVA + TASKU с минимальным отступом */}
          <div className="flex items-center gap-1">
            <span className="font-serif font-black text-base sm:text-lg tracking-[0.14em] text-white uppercase select-none leading-none">
              KALEVA
            </span>
            <span className="bg-black text-white text-[9px] sm:text-[10px] font-mono font-black uppercase tracking-wider px-1.5 py-0.5 rounded leading-none select-none translate-y-[2.5px]">
              TASKU
            </span>
          </div>

          {/* Правая часть: La 24.10.2026 (белый шрифт, на треть меньше KALEVA, выровнен по правому краю) */}
          <span className="text-white text-[11px] sm:text-xs font-semibold tracking-tight font-sans select-none">
            La 24.10.2026
          </span>
        </div>

        {/* СТРОЧКА С КАТЕГОРИЕЙ, АДРЕСОМ И ПРОЦЕНТОМ ДОВЕРИЯ: Сдвинута максимально вниз впритык к названию-ссылке */}
        <div className="flex items-center justify-between text-xs shrink-0 mb-1">
          <div className="flex items-center gap-2 min-w-0">
            <span className="px-2 py-0.5 rounded-md bg-[#cf2e2e] text-white text-[10px] font-black uppercase tracking-wider shrink-0 shadow-xs">
              {story.categoryLabel[language]}
            </span>
            <span className="flex items-center gap-1 text-[11px] text-slate-600 font-semibold truncate">
              <MapPin className="w-3.5 h-3.5 text-slate-500 shrink-0" />
              <span className="truncate">{story.district}</span>
            </span>
          </div>

          {/* Значок слушать в серой заливке и текст (30с) вместо зеленой строчки с 99% JSN */}
          <div className="flex items-center gap-2 shrink-0">
            <button
              type="button"
              onClick={onToggleAudio}
              className={`flex items-center gap-1.5 text-[11px] font-mono font-bold px-2 py-0.5 rounded-md border transition-all cursor-pointer shadow-2xs active:scale-95 ${
                isPlayingAudio
                  ? 'bg-slate-200 border-slate-400 text-[#002855]'
                  : 'bg-slate-100 hover:bg-slate-200 border-slate-300 text-slate-700'
              }`}
              title="Kuuntele (30s)"
            >
              {isPlayingAudio ? (
                <>
                  <Volume2 className="w-3.5 h-3.5 text-[#002855] shrink-0" />
                  <span>(30s)</span>
                </>
              ) : (
                <>
                  <Headphones className="w-3.5 h-3.5 text-slate-600 shrink-0" />
                  <span>(30s)</span>
                </>
              )}
            </button>
          </div>
        </div>

        {/* 1. НАЗВАНИЕ-ССЫЛКА (сдвинута на 2 пункта вниз) */}
        <div className="shrink-0 mt-2">
          <button
            type="button"
            onClick={() => onOpenBroadsheet(story)}
            className="text-left w-full group cursor-pointer block"
            title="Klikkaa avataksesi koko toimituksen juttu"
          >
            <h2 className="text-xl sm:text-2xl font-extrabold text-[#002855] group-hover:text-[#cf2e2e] transition-colors leading-tight tracking-tight flex items-start gap-2 font-sans">
              <span className="flex-1">{story.headline[language]}</span>
              <ArrowUpRight className="w-6 h-6 text-slate-400 group-hover:text-[#cf2e2e] group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-all shrink-0 mt-0.5" />
            </h2>
          </button>
        </div>

        {/* 2 & 3. РАЗДЕЛ С ПРОИСШЕСТВИЕМ + КНОПКА СЛУШАТЬ 30 СЕК + РАЗДЕЛ С РЕШЕНИЕМ */}
        <div className="mt-3 sm:mt-3.5 flex-1 flex flex-col justify-center pb-1">
          <DigitalSituationDiagram 
            diagram={story.diagram} 
            language={language} 
            storyId={story.id} 
            isPlayingAudio={isPlayingAudio}
            onToggleAudio={onToggleAudio}
          />
        </div>
      </div>
    </div>
  );
};
