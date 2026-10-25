export type Language = 'fi' | 'en' | 'selko' | 'sami';

export type Category = 'TRANSIT' | 'HOUSING' | 'EMERGENCY' | 'SPORTS' | 'CAMPUS' | 'AURORA';

export interface DigitalDiagram {
  isResolved?: boolean;
  problem: {
    icon: string; // Vector emoji or SVG identifier
    image?: string; // High-res situational photo URL
    caption?: string; // Photo caption or status overlay
    title: Record<Language, string>;
    detail: Record<Language, string>;
    badge: Record<Language, string>;
    color: string; // e.g. red/amber
  };
  arrowLabel: Record<Language, string>;
  solution: {
    icon: string; // Vector emoji or SVG identifier
    image?: string; // High-res practical solution photo URL
    caption?: string; // Photo caption or status overlay
    title: Record<Language, string>;
    detail: Record<Language, string>;
    badge: Record<Language, string>;
    color: string; // e.g. green/emerald
  };
}

export interface KeywordGlossary {
  term: string;
  finnishTerm: string;
  definition: Record<Language, string>;
  culturalContext: Record<Language, string>;
  statuteAnchor?: string;
  practicalTip: Record<Language, string>;
}

export interface StorySlide {
  id: string;
  category: Category;
  categoryLabel: Record<Language, string>;
  district: string;
  timeAgo: string;
  jsnStatus: string;
  credibilityScore: number;
  
  // Digital Diagram (Problem -> Arrow -> Solution), replacing photos
  diagram: DigitalDiagram;

  // Core Content (Headline is the clickable link)
  headline: Record<Language, string>;
  bullet1: Record<Language, string>;
  bullet2: Record<Language, string>;
  
  // Clickable Keyword ids available in this story
  keywords: string[];

  // Practical Everyday Solution (What to do?)
  solution: {
    badge: Record<Language, string>;
    text: Record<Language, string>;
    actionLabel: Record<Language, string>;
    actionType: 'MAP' | 'PHONE' | 'GUIDE' | 'VOUCHER' | 'VERIFY';
  };

  // Full traditional broadsheet article for deep reading
  traditionalDepth: {
    leadParagraph: Record<Language, string>;
    bodyText: Record<Language, string>;
    reporterName: string;
    section: string;
  };
}
