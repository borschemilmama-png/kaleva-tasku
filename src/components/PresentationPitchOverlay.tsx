import React, { useState } from 'react';
import { Language } from '../types';
import { Trophy, ChevronDown, ChevronUp } from 'lucide-react';

interface PresentationPitchOverlayProps {
  language: Language;
}

export const PresentationPitchOverlay: React.FC<PresentationPitchOverlayProps> = ({ language }) => {
  const [isOpen, setIsOpen] = useState(false);

  const contentMap: Record<Language, {
    badge: string;
    title: string;
    sub: string;
    pillar1Title: string;
    pillar1Desc: string;
    pillar2Title: string;
    pillar2Desc: string;
    pillar3Title: string;
    pillar3Desc: string;
    pillar4Title: string;
    pillar4Desc: string;
    toggleOpen: string;
    toggleClose: string;
  }> = {
    fi: {
      badge: 'JunctionX Oulu 2026 Kilpailukonsepti',
      title: 'Kaleva Tasku: Visuaalinen uutispalvelu ja arjen tulkki',
      sub: 'Yhdistää 125 vuotta Kalevan journalistista luotettavuutta nuorison ja kansainvälisten asukkaiden tarpeisiin',
      pillar1Title: '1. Piirretty digitaalinen tilannekuva',
      pillar1Desc: 'Ei epäoleellisia kuvituskuvia. Digitaalinen kuva esittää häiriön ja nuoli osoittaa suoraan piirrettyyn ratkaisuun.',
      pillar2Title: '2. Klikattavat otsikot & avainsanat',
      pillar2Desc: 'Otsikko avaa heti syvällisen jutun. Sanat kuten PSOAS ja Kela avaavat arjen selityksen ja lakitaustan.',
      pillar3Title: '3. Arjen ratkaisu joka kortissa',
      pillar3Desc: 'Konkreettinen toimintaohje lukijalle: vaihtoehtoinen bussi tai vuokralaisen opas.',
      pillar4Title: '4. Kalevan aito tyyli & JSN-ohjeet',
      pillar4Desc: 'Noudattaa täysin Kalevan oikeaa visuaalista ilmettä (valkoinen, musta teksti, JSN § 10).',
      toggleOpen: 'Avaa tuomareiden esittely',
      toggleClose: 'Sulje esittely'
    },
    en: {
      badge: 'JunctionX Oulu 2026 Concept',
      title: 'Kaleva Tasku: Visual Story & Civic Decoder',
      sub: 'Connecting 125 years of news authority with digital situation diagrams',
      pillar1Title: '1. Digital Situation Diagram',
      pillar1Desc: 'Zero stock photos. Clear diagram shows the problem and arrow points to drawn solution.',
      pillar2Title: '2. Clickable Headline & Keywords',
      pillar2Desc: 'Headline clicks straight to full broadsheet. Key terms link to statutory context.',
      pillar3Title: '3. Actionable Everyday Solution',
      pillar3Desc: 'Alternative bus routes, tenant rights guides, or event calendars on every card.',
      pillar4Title: '4. Authentic Kaleva Identity',
      pillar4Desc: 'Strict adherence to kaleva.fi brand identity, white layout, and JSN ethics rules.',
      toggleOpen: 'Open Hackathon Pitch Explainer',
      toggleClose: 'Collapse Pitch Explainer'
    },
    selko: {
      badge: 'Uusi idea uutisille',
      title: 'Kaleva Tasku: Helpot uutiset puhelimessa',
      sub: 'Uutiset helposti kuvilla ja lyhyellä tekstillä',
      pillar1Title: '1. Helpot piirrokset',
      pillar1Desc: 'Näet kuvasta heti mitä tapahtui ja minne mennä.',
      pillar2Title: '2. Klikattavat sanat',
      pillar2Desc: 'Klikkaa vaikeaa sanaa ja saat helpon selityksen.',
      pillar3Title: '3. Mitä tehdä',
      pillar3Desc: 'Saat heti neuvon miten toimia arjessa.',
      pillar4Title: '4. Luotettava Kaleva',
      pillar4Desc: 'Kaikki uutiset ovat tarkistettuja ja totta.',
      toggleOpen: 'Lue lisää ideasta',
      toggleClose: 'Sulje'
    },
    sami: {
      badge: 'Ođđa idea ođđasiidda',
      title: 'Kaleva Tasku: Álkes ođđasat telefonis',
      sub: 'Ođđasat govaiguin ja oanehis teavsttain',
      pillar1Title: '1. Govva mii čájeha dili',
      pillar1Desc: 'Oainnát govas dakkaviđe mii dáhpáhuvai ja njuolggu čujuha čoavdáldahkii.',
      pillar2Title: '2. Klikkaválas bajilčállagat',
      pillar2Desc: 'Klikke sáni ja oaččut lágalaš čielggadusa.',
      pillar3Title: '3. Maid galgá dahkat',
      pillar3Desc: 'Oaččut dakkaviđe rávvaga mo doaimmat.',
      pillar4Title: '4. Luohtehahtti Kaleva',
      pillar4Desc: 'Buot ođđasat leat dárkkistuvvon ja duohta.',
      toggleOpen: 'Lue lisää ideasta',
      toggleClose: 'Sulje'
    }
  };

  const content = contentMap[language] || contentMap.fi;

  return (
    <div className="w-full max-w-4xl mx-auto px-4 mt-3 mb-1">
      <div className="bg-white border-2 border-[#dedad2] rounded-2xl p-4 shadow-sm text-slate-900">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div className="space-y-1">
            <div className="flex items-center gap-2">
              <span className="p-1 rounded bg-[#c8102e] text-white text-[10px] font-black uppercase font-mono tracking-wider flex items-center gap-1">
                <Trophy className="w-3 h-3" />
                {content.badge}
              </span>
              <span className="text-[11px] text-[#c25700] font-bold font-mono">
                Team Oksana & Vinod
              </span>
            </div>
            <h2 className="text-base sm:text-lg font-bold text-[#002855] tracking-tight">
              {content.title}
            </h2>
            <p className="text-xs text-slate-600">
              {content.sub}
            </p>
          </div>

          <button
            onClick={() => setIsOpen(!isOpen)}
            className="px-4 py-2 rounded-xl bg-[#f0ece4] hover:bg-[#e6e1d6] text-[#002855] font-bold text-xs flex items-center gap-2 transition-all self-start sm:self-auto shrink-0 border border-[#dedad2] cursor-pointer"
          >
            <span>{isOpen ? content.toggleClose : content.toggleOpen}</span>
            {isOpen ? <ChevronDown className="w-4 h-4" /> : <ChevronDown className="w-4 h-4 rotate-180" />}
          </button>
        </div>

        {isOpen && (
          <div className="mt-4 pt-4 border-t border-slate-200 grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
            <div className="p-3 rounded-xl bg-slate-50 border border-slate-200">
              <h4 className="font-bold text-[#002855] mb-1">{content.pillar1Title}</h4>
              <p className="text-slate-600">{content.pillar1Desc}</p>
            </div>
            <div className="p-3 rounded-xl bg-slate-50 border border-slate-200">
              <h4 className="font-bold text-[#002855] mb-1">{content.pillar2Title}</h4>
              <p className="text-slate-600">{content.pillar2Desc}</p>
            </div>
            <div className="p-3 rounded-xl bg-slate-50 border border-slate-200">
              <h4 className="font-bold text-[#002855] mb-1">{content.pillar3Title}</h4>
              <p className="text-slate-600">{content.pillar3Desc}</p>
            </div>
            <div className="p-3 rounded-xl bg-slate-50 border border-slate-200">
              <h4 className="font-bold text-[#002855] mb-1">{content.pillar4Title}</h4>
              <p className="text-slate-600">{content.pillar4Desc}</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};
