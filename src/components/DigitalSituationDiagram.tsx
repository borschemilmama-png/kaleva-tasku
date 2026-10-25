import React from 'react';
import { DigitalDiagram, Language } from '../types';
import { SituationVisual } from './SituationVisual';
import { Headphones, Volume2 } from 'lucide-react';

interface DigitalSituationDiagramProps {
  diagram: DigitalDiagram;
  language: Language;
  storyId?: string;
  isPlayingAudio?: boolean;
  onToggleAudio?: () => void;
}

export const DigitalSituationDiagram: React.FC<DigitalSituationDiagramProps> = ({
  diagram,
  language,
  storyId,
  isPlayingAudio,
  onToggleAudio
}) => {
  return (
    <div className="w-full flex-1 flex flex-col justify-center gap-1 sm:gap-1.5">
      {/* 1. Problem / Situation: Text 1/3 on the left, Picture 2/3 on the right */}
      <div className="w-full shrink-0 space-y-1.5">
        <div className="flex items-center">
          <span className="text-xs sm:text-[12.5px] font-mono font-bold uppercase tracking-wider flex items-center gap-2 text-slate-700">
            <span className="w-2.5 h-2.5 rounded-full bg-[#ff5500] shrink-0 inline-block" />
            <span>TILANNE</span>
          </span>
        </div>
        
        <div className="grid grid-cols-3 gap-3 items-center">
          {/* Left Column: 1/3 of the space for all text */}
          <div className="col-span-1 space-y-1.5 pr-1">
            <h3 className="text-sm sm:text-base font-black text-slate-950 leading-snug tracking-tight font-sans">
              {diagram.problem.title[language]}
            </h3>
            <p className="text-xs sm:text-[13px] text-slate-600 leading-snug font-medium">
              {diagram.problem.detail[language]}
            </p>
          </div>

          {/* Right Column: 2/3 of the space for ONE larger unified picture */}
          <div className="col-span-2 w-full flex items-center justify-center">
            <SituationVisual storyId={storyId} type="problem" language={language} />
          </div>
        </div>
      </div>

      {/* 2. Arrow: EXACTLY MIDWAY, SHORTER & SALAD GREEN (#22c55e) */}
      <div className="flex items-center justify-center pt-2 sm:pt-2.5 pb-0.5 shrink-0">
        <svg 
          className="w-6 h-6 sm:w-7 sm:h-7 text-[#22c55e] select-none" 
          viewBox="0 0 24 24" 
          fill="none" 
          stroke="currentColor" 
          strokeWidth="4.5" 
          strokeLinecap="round" 
          strokeLinejoin="round" 
        >
          <line x1="12" y1="5" x2="12" y2="19" />
          <polyline points="16 14 12 19 8 14" />
        </svg>
      </div>

      {/* 3. Solution / Action: Text 1/3 on the left, Picture 2/3 on the right */}
      <div className="w-full shrink-0 space-y-1.5">
        <div className="flex items-center">
          <span className="text-xs sm:text-[12.5px] font-mono font-bold uppercase tracking-wider flex items-center gap-2 text-slate-700">
            <span className="w-2.5 h-2.5 rounded-full bg-[#ff5500] shrink-0 inline-block" />
            <span>TOIMINTAOHJE</span>
          </span>
        </div>

        <div className="grid grid-cols-3 gap-3 items-center">
          {diagram.isResolved ? (
            <>
              {/* Left Column: 1/3 for resolved text */}
              <div className="col-span-1 pr-1">
                <p className="text-sm sm:text-base font-black text-slate-950 leading-snug tracking-tight font-sans">
                  Tilanne on ratkaistu, lisätoimenpiteitä ei vaadita.
                </p>
              </div>

              {/* Right Column: 2/3 for resolved picture */}
              <div className="col-span-2 w-full flex items-center justify-center">
                <SituationVisual storyId={storyId} type="solution" isResolved={true} language={language} />
              </div>
            </>
          ) : (
            <>
              {/* Left Column: 1/3 for solution text */}
              <div className="col-span-1 space-y-1.5 pr-1">
                <h3 className="text-sm sm:text-base font-black text-slate-950 leading-snug tracking-tight font-sans">
                  {diagram.solution.title[language]}
                </h3>
                <p className="text-xs sm:text-[13px] text-slate-600 leading-snug font-medium">
                  {diagram.solution.detail[language]}
                </p>
              </div>

              {/* Right Column: 2/3 for solution picture */}
              <div className="col-span-2 w-full flex items-center justify-center">
                <SituationVisual storyId={storyId} type="solution" isResolved={false} language={language} />
              </div>
            </>
          )}
        </div>
      </div>
    </div>
  );
};
