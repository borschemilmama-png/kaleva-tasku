import React, { useState, useRef } from 'react';
import { ChevronLeft, ChevronRight, Wifi, Battery } from 'lucide-react';

interface PhoneShellProps {
  children: React.ReactNode;
  currentIndex: number;
  totalStories: number;
  onNext: () => void;
  onPrev: () => void;
}

export const PhoneShell: React.FC<PhoneShellProps> = ({
  children,
  currentIndex,
  totalStories,
  onNext,
  onPrev,
}) => {
  const [touchStartX, setTouchStartX] = useState<number | null>(null);
  const [touchDeltaX, setTouchDeltaX] = useState<number>(0);
  const isDragging = useRef<boolean>(false);

  // Swipe handling
  const handleTouchStart = (e: React.TouchEvent | React.MouseEvent) => {
    const clientX = 'touches' in e ? e.touches[0].clientX : e.clientX;
    setTouchStartX(clientX);
    isDragging.current = true;
  };

  const handleTouchMove = (e: React.TouchEvent | React.MouseEvent) => {
    if (!isDragging.current || touchStartX === null) return;
    const clientX = 'touches' in e ? e.touches[0].clientX : e.clientX;
    setTouchDeltaX(clientX - touchStartX);
  };

  const handleTouchEnd = () => {
    if (touchDeltaX > 50) {
      onPrev();
    } else if (touchDeltaX < -50) {
      onNext();
    }
    setTouchStartX(null);
    setTouchDeltaX(0);
    isDragging.current = false;
  };

  return (
    <div className="flex flex-col items-center w-full max-w-sm sm:max-w-md">
      {/* Smartphone Chassis */}
      <div 
        className="relative w-full h-[760px] sm:h-[800px] bg-white rounded-[44px] p-2.5 shadow-[0_20px_50px_rgba(0,0,0,0.15)] border-[5px] border-[#2d2d2d] ring-1 ring-slate-300 flex flex-col overflow-hidden"
        onTouchStart={handleTouchStart}
        onTouchMove={handleTouchMove}
        onTouchEnd={handleTouchEnd}
        onMouseDown={handleTouchStart}
        onMouseMove={handleTouchMove}
        onMouseUp={handleTouchEnd}
      >
        {/* Dynamic Island: Both circle sensors are neutral grey */}
        <div className="absolute top-3 left-1/2 -translate-x-1/2 z-40">
          <div className="w-24 h-5 bg-black rounded-full flex items-center justify-between px-3">
            <span className="w-2 h-2 rounded-full bg-slate-700" />
            <span className="w-2 h-2 rounded-full bg-slate-700" />
          </div>
        </div>

        {/* Smartphone Status Bar: Clean Clock & Signal/Battery */}
        <div className="pt-1.5 px-4 pb-1 flex items-center justify-between text-[11px] font-semibold text-slate-800 select-none z-30 shrink-0 border-b border-slate-100">
          <div className="flex items-center">
            <span className="font-bold">09:41</span>
          </div>
          
          <div className="flex items-center gap-1.5 text-slate-600">
            <Wifi className="w-3.5 h-3.5" />
            <Battery className="w-4 h-4 text-slate-800" />
          </div>
        </div>

        {/* Stories Progress Bar: Rich vibrant orange indicator for active page */}
        <div className="pt-1.5 px-3 flex gap-1 z-30 shrink-0">
          {Array.from({ length: totalStories }).map((_, idx) => (
            <div
              key={idx}
              className={`h-1.5 rounded-full flex-1 transition-all duration-300 ${
                idx === currentIndex
                  ? 'bg-[#ff5500] shadow-sm'
                  : idx < currentIndex
                  ? 'bg-slate-800'
                  : 'bg-slate-200'
              }`}
            />
          ))}
        </div>

        {/* Card Screen Viewport */}
        <div 
          className="flex-1 mt-1.5 mb-1 relative overflow-hidden rounded-[28px] transition-transform duration-200 bg-white"
          style={{
            transform: `translateX(${touchDeltaX * 0.4}px)`,
          }}
        >
          {children}
        </div>

        {/* Bottom Navigation Controls: Larger page numbers and navigation labels, NO grey home bar underneath */}
        <div className="py-2.5 px-4 flex items-center justify-between text-slate-800 select-none z-30 shrink-0 border-t border-slate-100">
          <button
            type="button"
            onClick={onPrev}
            disabled={currentIndex === 0}
            className={`flex items-center gap-1 px-3 py-1.5 rounded-full transition-all ${
              currentIndex === 0
                ? 'opacity-25 cursor-not-allowed'
                : 'hover:bg-slate-100 text-slate-900 font-bold active:scale-95 cursor-pointer'
            }`}
          >
            <ChevronLeft className="w-4.5 h-4.5" />
            <span className="text-xs sm:text-sm font-bold">Edellinen</span>
          </button>

          <div className="text-xs sm:text-sm font-mono font-bold text-slate-800 bg-slate-100 px-3.5 py-1 rounded-full border border-slate-200">
            {currentIndex + 1} / {totalStories}
          </div>

          <button
            type="button"
            onClick={onNext}
            disabled={currentIndex === totalStories - 1}
            className={`flex items-center gap-1 px-3 py-1.5 rounded-full transition-all ${
              currentIndex === totalStories - 1
                ? 'opacity-25 cursor-not-allowed'
                : 'hover:bg-slate-100 text-slate-900 font-bold active:scale-95 cursor-pointer'
            }`}
          >
            <span className="text-xs sm:text-sm font-bold">Seuraava</span>
            <ChevronRight className="w-4.5 h-4.5" />
          </button>
        </div>
      </div>
    </div>
  );
};
