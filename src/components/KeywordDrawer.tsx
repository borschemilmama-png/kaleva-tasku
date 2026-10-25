import React from 'react';
import { KeywordGlossary, Language } from '../types';
import { X, BookOpen, Compass, Scale, Lightbulb } from 'lucide-react';

interface KeywordDrawerProps {
  keyword: KeywordGlossary | null;
  language: Language;
  onClose: () => void;
}

export const KeywordDrawer: React.FC<KeywordDrawerProps> = ({ keyword, language, onClose }) => {
  if (!keyword) return null;

  const labels = {
    fi: {
      badge: 'Suomalaisen arjen sanasto',
      close: 'Sulje',
      whatIs: 'Mitä tämä tarkoittaa:',
      culture: 'Kulttuurinen tausta Oulussa:',
      statute: 'Lakisääteinen perusta:',
      tip: 'Käytännön neuvo lukijalle:',
      understood: 'Selvä, kiitos!'
    },
    en: {
      badge: 'Finnish Civic Lexicon',
      close: 'Close',
      whatIs: 'What it means:',
      culture: 'Cultural Context in Oulu:',
      statute: 'Statutory Anchor:',
      tip: 'Practical Expat Tip:',
      understood: 'Got It, Thanks!'
    },
    selko: {
      badge: 'Helppo selitys sanalle',
      close: 'Sulje',
      whatIs: 'Tämä tarkoittaa:',
      culture: 'Tieto Oulusta:',
      statute: 'Suomen laki:',
      tip: 'Neuvo sinulle:',
      understood: 'Selvä!'
    },
    sami: {
      badge: 'Oulu árgabeaivvi sánit',
      close: 'Gidde',
      whatIs: 'Mii dán mearkkaša:',
      culture: 'Kultuvrralaš duogáš Oulus:',
      statute: 'Lágalaš vuođđu:',
      tip: 'Ávkkálaš rávva dutnje:',
      understood: 'Čielggas, giitu!'
    }
  }[language];

  return (
    <div className="fixed inset-0 z-50 flex items-end sm:items-center justify-center p-0 sm:p-4 bg-black/60 backdrop-blur-xs animate-in fade-in duration-150">
      <div 
        className="w-full max-w-lg bg-white border-t sm:border-2 border-slate-300 rounded-t-3xl sm:rounded-3xl shadow-2xl p-5 sm:p-6 text-slate-900 overflow-hidden max-h-[85vh] flex flex-col animate-in slide-in-from-bottom-6 duration-200"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div className="flex items-center justify-between pb-3 border-b border-slate-200">
          <div className="flex items-center gap-2">
            <span className="p-1.5 rounded-lg bg-[#f0ece4] text-[#c25700] border border-[#dedad2]">
              <BookOpen className="w-4 h-4" />
            </span>
            <span className="text-xs font-mono uppercase tracking-wider text-[#c25700] font-black">
              {labels.badge}
            </span>
          </div>

          <button
            onClick={onClose}
            className="p-1 rounded-full text-slate-400 hover:text-slate-700 hover:bg-slate-100 transition-colors cursor-pointer"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Term Title */}
        <div className="py-3 border-b border-slate-100">
          <h3 className="text-2xl font-serif font-black text-[#002855] tracking-tight">
            {keyword.term}
          </h3>
          <p className="text-xs font-mono text-slate-500 mt-0.5">
            {keyword.finnishTerm}
          </p>
        </div>

        {/* Scrollable Content */}
        <div className="flex-1 overflow-y-auto py-4 space-y-3.5 text-xs pr-1">
          {/* Definition */}
          <div className="p-3.5 rounded-2xl bg-[#f8fafc] border border-slate-200 space-y-1">
            <span className="font-bold text-slate-700 flex items-center gap-1.5 text-[11px] uppercase tracking-wider">
              <Compass className="w-3.5 h-3.5 text-[#002855]" />
              {labels.whatIs}
            </span>
            <p className="text-slate-900 text-sm leading-relaxed font-medium">
              {keyword.definition[language]}
            </p>
          </div>

          {/* Cultural Context */}
          <div className="p-3.5 rounded-2xl bg-[#fef9e7] border border-amber-200 space-y-1">
            <span className="font-bold text-amber-900 flex items-center gap-1.5 text-[11px] uppercase tracking-wider">
              <Lightbulb className="w-3.5 h-3.5 text-[#c25700]" />
              {labels.culture}
            </span>
            <p className="text-amber-950 text-xs leading-relaxed">
              {keyword.culturalContext[language]}
            </p>
          </div>

          {/* Practical Tip */}
          <div className="p-3.5 rounded-2xl bg-[#edf7ed] border border-emerald-300 text-emerald-950 space-y-1">
            <span className="font-bold text-emerald-900 flex items-center gap-1.5 text-[11px] uppercase tracking-wider">
              👉 {labels.tip}
            </span>
            <p className="text-xs leading-relaxed text-emerald-900 font-medium">
              {keyword.practicalTip[language]}
            </p>
          </div>

          {/* Legal Statute Anchor */}
          {keyword.statuteAnchor && (
            <div className="flex items-center gap-2 p-2.5 rounded-xl bg-slate-50 border border-slate-200 text-[11px] font-mono text-slate-600">
              <Scale className="w-3.5 h-3.5 text-slate-500 shrink-0" />
              <span className="font-bold text-slate-800">{labels.statute}:</span>
              <span className="text-[#002855] truncate font-semibold">{keyword.statuteAnchor}</span>
            </div>
          )}
        </div>

        {/* Footer */}
        <div className="pt-3 border-t border-slate-200 flex justify-end">
          <button
            onClick={onClose}
            className="w-full sm:w-auto px-6 py-2.5 rounded-xl bg-[#002855] hover:bg-[#001f42] text-white font-bold text-xs shadow-md transition-all active:scale-95 cursor-pointer"
          >
            {labels.understood}
          </button>
        </div>
      </div>
    </div>
  );
};
