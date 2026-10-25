import React from 'react';
import { StorySlide, Language } from '../types';
import { X, Calendar, Feather, ShieldCheck, ArrowLeft, Share2, Printer } from 'lucide-react';

interface ClassicBroadsheetViewProps {
  story: StorySlide;
  language: Language;
  onClose: () => void;
}

export const ClassicBroadsheetView: React.FC<ClassicBroadsheetViewProps> = ({
  story,
  language,
  onClose,
}) => {
  const labels = {
    fi: {
      edition: 'Kalevan toimitus • Syväartikkeli',
      lead: 'Pääuutinen',
      ethics: 'Artikkeli noudattaa Julkisen sanan neuvoston (JSN) journalistisia ohjeita',
      back: 'Palaa Tasku-kortteihin',
      share: 'Jaa uutinen',
      print: 'Tulosta'
    },
    en: {
      edition: 'Kaleva Newsroom • Deep Article',
      lead: 'Lead Story',
      ethics: 'Audited under Council for Mass Media in Finland (JSN § 10) guidelines',
      back: 'Back to Story Cards',
      share: 'Share',
      print: 'Print'
    },
    selko: {
      edition: 'Kalevan helppo uutisartikkeli',
      lead: 'Tärkeä uutinen',
      ethics: 'Tämä uutinen on tarkistettu ja totta',
      back: 'Takaisin kortteihin',
      share: 'Jaa',
      print: 'Tulosta'
    },
    sami: {
      edition: 'Kaleva doaimmahus • Ođasartihkal',
      lead: 'Váldoođas',
      ethics: 'Artihkal čuovvu Julkisen sanan neuvosto (JSN) njuolggadusaid',
      back: 'Mázza ođđasiidda',
      share: 'Juoge',
      print: 'Prente'
    }
  }[language];

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-2 sm:p-6 bg-black/60 backdrop-blur-xs overflow-y-auto animate-in fade-in duration-150">
      <div 
        className="w-full max-w-3xl bg-white text-slate-950 rounded-3xl shadow-2xl border-2 border-[#dedad2] overflow-hidden my-auto flex flex-col font-sans"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Authentic Kaleva Header */}
        <div className="bg-[#f0ece4] border-b-2 border-[#dedad2] px-6 py-3.5 flex items-center justify-between">
          <div className="flex items-baseline gap-3">
            <span className="text-3xl font-serif font-black tracking-tight text-[#000000] uppercase">
              Kaleva
            </span>
            <span className="text-xs font-mono font-bold text-slate-500 hidden sm:inline">
              {labels.edition} • {story.district}
            </span>
          </div>

          <button
            onClick={onClose}
            className="p-1.5 rounded-full hover:bg-slate-200 text-slate-700 transition-colors cursor-pointer"
            title="Sulje"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Article Body */}
        <div className="p-6 sm:p-8 space-y-6 overflow-y-auto max-h-[75vh]">
          {/* Category & Headline */}
          <div className="space-y-2 border-b-2 border-slate-900 pb-4">
            <span className="inline-block text-xs font-black uppercase tracking-wider text-[#c8102e] font-mono">
              {story.categoryLabel[language]}
            </span>
            <h1 className="text-2xl sm:text-3xl font-serif font-extrabold text-slate-950 leading-tight">
              {story.headline[language]}
            </h1>
            <div className="flex flex-wrap items-center gap-3 text-xs text-slate-600 pt-2 font-medium">
              <span className="flex items-center gap-1 font-bold text-slate-900">
                <Feather className="w-3.5 h-3.5 text-[#c8102e]" />
                {story.traditionalDepth.reporterName}
              </span>
              <span>•</span>
              <span className="flex items-center gap-1">
                <Calendar className="w-3.5 h-3.5" />
                24.10.2026 klo 08:30
              </span>
              <span>•</span>
              <span className="flex items-center gap-1 text-emerald-800 font-mono font-bold bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">
                <ShieldCheck className="w-3.5 h-3.5" />
                {story.jsnStatus}
              </span>
            </div>
          </div>

          {/* Lead Paragraph with classic drop cap */}
          <div className="font-serif text-lg text-slate-900 leading-relaxed border-b border-slate-200 pb-4">
            <span className="float-left text-5xl font-serif font-black pr-2.5 text-[#002855] leading-none">
              {story.traditionalDepth.leadParagraph[language].charAt(0)}
            </span>
            {story.traditionalDepth.leadParagraph[language].slice(1)}
          </div>

          {/* In-depth Article Text */}
          <div className="font-serif text-slate-800 leading-relaxed text-base space-y-4">
            <p>{story.traditionalDepth.bodyText[language]}</p>
          </div>

          {/* JSN Ethics Statement */}
          <div className="p-3.5 rounded-xl bg-[#f0ece4] border border-[#dedad2] text-xs text-slate-800 space-y-1">
            <p className="font-bold flex items-center gap-1.5 text-slate-950">
              <ShieldCheck className="w-4 h-4 text-emerald-700" />
              {labels.ethics}
            </p>
            <p className="text-[11px] text-slate-600">
              Kaleva korjaa asiavirheet viipymättä verkossa ja mobiilissa Journalistin ohjeiden (JSN § 20) mukaisesti.
            </p>
          </div>
        </div>

        {/* Footer */}
        <div className="bg-[#f0ece4] px-6 py-3 border-t border-[#dedad2] flex items-center justify-between">
          <button
            onClick={onClose}
            className="px-4 py-2 rounded-xl bg-[#002855] hover:bg-[#001f42] text-white font-bold text-xs flex items-center gap-1.5 transition-all shadow-xs cursor-pointer"
          >
            <ArrowLeft className="w-4 h-4" />
            <span>{labels.back}</span>
          </button>
          <span className="text-[11px] text-slate-500 font-medium">
            Kaleva Media Oy © 1899–2026
          </span>
        </div>
      </div>
    </div>
  );
};
