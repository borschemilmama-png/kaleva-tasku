import React, { useState, useEffect } from 'react';
import { STORY_SLIDES, KEYWORDS_DB } from './data/mockStories';
import { StorySlide, Language, KeywordGlossary } from './types';
import { HeaderMasthead } from './components/HeaderMasthead';
import { PhoneShell } from './components/PhoneShell';
import { StoryCard } from './components/StoryCard';
import { KeywordDrawer } from './components/KeywordDrawer';
import { ClassicBroadsheetView } from './components/ClassicBroadsheetView';
import { CheckCircle2, X } from 'lucide-react';

export default function App() {
  const [currentIndex, setCurrentIndex] = useState<number>(0);
  const language: Language = 'fi'; // Strictly Finnish as requested, designed to be completely intuitive without translation
  const [activeKeyword, setActiveKeyword] = useState<KeywordGlossary | null>(null);
  const [selectedBroadsheetStory, setSelectedBroadsheetStory] = useState<StorySlide | null>(null);
  const [isPlayingAudio, setIsPlayingAudio] = useState<boolean>(false);
  const [actionAlert, setActionAlert] = useState<{ title: string; message: string; badge: string } | null>(null);

  const currentStory = STORY_SLIDES[currentIndex];

  // Keyboard navigation (Arrow keys)
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (activeKeyword || selectedBroadsheetStory || actionAlert) return;
      if (e.key === 'ArrowRight' || e.key === ' ') {
        handleNext();
      } else if (e.key === 'ArrowLeft') {
        handlePrev();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [currentIndex, activeKeyword, selectedBroadsheetStory, actionAlert]);

  // Audio synthesis using browser native Web Speech API in Finnish
  const handleToggleAudio = () => {
    if (isPlayingAudio) {
      if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
      }
      setIsPlayingAudio(false);
    } else {
      setIsPlayingAudio(true);
      if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
        const textToSpeak = `${currentStory.headline.fi}. ${currentStory.bullet1.fi}. ${currentStory.solution.text.fi}`;
        const utterance = new SpeechSynthesisUtterance(textToSpeak);
        utterance.lang = 'fi-FI';
        utterance.rate = 1.05;
        utterance.onend = () => setIsPlayingAudio(false);
        utterance.onerror = () => setIsPlayingAudio(false);
        window.speechSynthesis.speak(utterance);
      } else {
        setTimeout(() => setIsPlayingAudio(false), 8000);
      }
    }
  };

  const handleNext = () => {
    if (currentIndex < STORY_SLIDES.length - 1) {
      setCurrentIndex((prev) => prev + 1);
      if (isPlayingAudio && 'speechSynthesis' in window) {
        window.speechSynthesis.cancel();
        setIsPlayingAudio(false);
      }
    }
  };

  const handlePrev = () => {
    if (currentIndex > 0) {
      setCurrentIndex((prev) => prev - 1);
      if (isPlayingAudio && 'speechSynthesis' in window) {
        window.speechSynthesis.cancel();
        setIsPlayingAudio(false);
      }
    }
  };

  const handleActionClick = (story: StorySlide) => {
    const alerts: Record<string, { title: string; message: string; badge: string }> = {
      'story-1-kaakkuri-vt4': {
        title: '🚗 Fintraffic: Kaakkurin kiertotie avattu',
        message: 'Valtatie 4 etelän kaistalta suositellaan poistumaan Kaakkurin liittymästä Kaakkurintielle. Raivaustyöt kestävät noin 45 minuuttia.',
        badge: 'Fintraffic Reaaliaika'
      },
      'story-2-rotuaari-keskusta': {
        title: '👮 Oulun poliisilaitoksen tilannetieto',
        message: 'Rotuaarin ja Kauppakeskus Valkean alue on täysin rauhoitettu. Kuusi häiriöön osallistunutta on otettu kiinni. Liikkuminen on turvallista.',
        badge: 'Poliisi 112'
      },
      'story-3-oulunsalo-autopalo': {
        title: '🧯 Pelastuslaitoksen toimintaohje',
        message: 'Alkusammutus onnistui lumella ja sammuttimella. Muista talvella: tarkista aina auton lohkolämmitysjohto ja pidä jauhesammutin saatavilla.',
        badge: 'Pohjois-Pohjanmaan Pelastuslaitos'
      },
      'story-4-osl-liukkaus-baana': {
        title: '🚌 OSL Live GPS & Baana-pyörätie',
        message: 'Runkolinjat 1, 2 ja 3 kulkevat 10–15 minuutin viiveellä. Pääpyörätie Baana Linnanmaalle on harjasuolattu ja asfalttipintainen.',
        badge: 'OSL & Oulun Katuosasto'
      },
      'story-5-kivisydan-kuutar': {
        title: '🌸 Kivisydän: Kuuttaren puutarha -opas',
        message: 'Astu Rotuaarin tai kauppakeskus Valkean lasihissiin ja laskeudu suoraan maan alle lämpimään (+16°C). Näyttely on esteetön ja avoinna päivittäin.',
        badge: 'Kivisydän & Oulu2026'
      }
    };

    setActionAlert(alerts[story.id] || {
      title: 'Toiminto suoritettu',
      message: story.solution.text.fi,
      badge: 'Kaleva'
    });
  };

  return (
    <div className="min-h-screen bg-[#f0ece4] text-[#000000] flex flex-col font-sans selection:bg-[#cf2e2e] selection:text-white">
      {/* Top Authentic Kaleva.fi Masthead without language selector */}
      <HeaderMasthead
        isPlayingAudio={isPlayingAudio}
        onToggleAudio={handleToggleAudio}
      />

      {/* Main Content Area */}
      <main className="flex-1 max-w-4xl w-full mx-auto px-4 py-4 sm:py-6 flex flex-col items-center justify-center">
        {/* Smartphone Shell running Kaleva Tasku */}
        <PhoneShell
          currentIndex={currentIndex}
          totalStories={STORY_SLIDES.length}
          onNext={handleNext}
          onPrev={handlePrev}
        >
          <StoryCard
            story={currentStory}
            language={language}
            onOpenBroadsheet={(st) => setSelectedBroadsheetStory(st)}
            isPlayingAudio={isPlayingAudio}
            onToggleAudio={handleToggleAudio}
          />
        </PhoneShell>

        {/* Quick Story Selector Carousel Pills (Exact Kaleva Colors) */}
        <div className="mt-5 flex flex-wrap justify-center gap-2 max-w-xl px-2">
          {STORY_SLIDES.map((slide, idx) => (
            <button
              key={slide.id}
              onClick={() => {
                setCurrentIndex(idx);
                if (isPlayingAudio && 'speechSynthesis' in window) {
                  window.speechSynthesis.cancel();
                  setIsPlayingAudio(false);
                }
              }}
              className={`px-3 py-1.5 rounded-full text-xs font-bold flex items-center gap-1.5 transition-all cursor-pointer border ${
                idx === currentIndex
                  ? 'bg-[#002855] text-white border-[#002855] shadow-sm scale-105'
                : 'bg-white hover:bg-[#e6e1d6] text-slate-700 border-[#dedad2]'
              }`}
            >
              <span>{slide.diagram.problem.icon.split('')[0]}</span>
              <span className="truncate max-w-[130px]">
                {slide.categoryLabel[language]}
              </span>
            </button>
          ))}
        </div>

        <p className="mt-3 text-xs text-slate-500 font-sans text-center">
          💡 Pyyhkäise korttia tai käytä nuolinäppäimiä ← → • Avaa toimituksen koko juttu klikkaamalla otsikkoa
        </p>
      </main>

      {/* Interactive Keyword Drawer Modal (Opens on highlighted baseline terms) */}
      <KeywordDrawer
        keyword={activeKeyword}
        language={language}
        onClose={() => setActiveKeyword(null)}
      />

      {/* Classic Broadsheet Modal (Opens when user clicks the headline!) */}
      {selectedBroadsheetStory && (
        <ClassicBroadsheetView
          story={selectedBroadsheetStory}
          language={language}
          onClose={() => setSelectedBroadsheetStory(null)}
        />
      )}

      {/* Practical Solution Action Alert Modal */}
      {actionAlert && (
        <div 
          className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-xs animate-in fade-in duration-150"
          onClick={() => setActionAlert(null)}
        >
          <div 
            className="w-full max-w-md bg-white border-2 border-slate-300 rounded-3xl p-6 shadow-2xl text-slate-900 space-y-4 animate-in zoom-in-95 duration-150"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="flex items-center justify-between border-b border-slate-200 pb-3">
              <span className="text-[10px] font-mono uppercase px-2.5 py-1 rounded-full bg-[#edf7ed] text-[#1a7a40] font-black border border-emerald-300">
                {actionAlert.badge}
              </span>
              <button
                onClick={() => setActionAlert(null)}
                className="p-1 rounded-full text-slate-400 hover:text-slate-700 cursor-pointer"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            <div className="space-y-2">
              <h3 className="text-lg font-bold text-slate-950 flex items-center gap-2">
                <CheckCircle2 className="w-5 h-5 text-[#1a7a40] shrink-0" />
                {actionAlert.title}
              </h3>
              <p className="text-sm text-slate-700 leading-relaxed font-medium">
                {actionAlert.message}
              </p>
            </div>

            <div className="pt-2 flex justify-end">
              <button
                onClick={() => setActionAlert(null)}
                className="w-full py-2.5 rounded-xl bg-[#002855] hover:bg-[#001f42] text-white font-bold text-xs transition-all cursor-pointer shadow-sm"
              >
                Selvä, kiitos!
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Bottom Footer (Clean kaleva.fi style) */}
      <footer className="w-full bg-[#f0ece4] border-t-2 border-[#dedad2] py-4 px-6 text-center text-xs text-[#5c5852] font-sans">
        <p className="font-bold text-slate-800">Kaleva Tasku • Pohjoisen puolesta vuodesta 1899</p>
        <p className="text-[11px] text-slate-500 mt-0.5">
          Oulun paikallisuutiset, visuaalinen arjen tulkkaus ja JSN-valvottu luotettavuus
        </p>
      </footer>
    </div>
  );
}
