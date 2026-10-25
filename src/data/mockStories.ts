import { StorySlide, KeywordGlossary, Language } from '../types';

export const KEYWORDS_DB: Record<string, KeywordGlossary> = {
  'kaakkurin-ramppi': {
    term: 'Kaakkurin ramppi',
    finnishTerm: 'Kaakkurin liittymä (VT4 / Pohjantie)',
    definition: {
      fi: 'Valtatien 4 eritasoliittymä Oulun eteläpuolella Kaakkurin suuralueella, jota kautta kulkee vilkas työmatkaliikenne.',
      en: 'Major highway interchange on Route 4 south of Oulu connecting the Kaakkuri district and commercial areas.',
      selko: 'Iso tienhaara valtatiellä 4 Oulun eteläpuolella. Siitä ajetaan Kaakkuriin.',
      sami: 'Stuorra luoddaearru Oulu lulábealde mas lea ollu johtolat.'
    },
    culturalContext: {
      fi: 'Kaakkurin ramppi on tunnettu aamuruuhkistaan. Onnettomuuden sattuessa liikenne puuroutuu nopeasti molempiin suuntiin.',
      en: 'Known for heavy morning commuter traffic. Any disruption quickly causes multi-kilometer bottlenecks.',
      selko: 'Aamuisin tiellä on paljon autoja ja helposti ruuhkaa.',
      sami: 'Iđđediid dás leat ollu biillat ja johtolat sáhttá bisánit.'
    },
    statuteAnchor: 'Väylävirasto & Fintraffic Liikennetilanne',
    practicalTip: {
      fi: 'Kierrä onnettomuuspaikka Kaakkurintietä tai Iinatin kautta Limingantulliin.',
      en: 'Bypass the bottleneck via Kaakkurintie local streets or Iinatti to Limingantulli.',
      selko: 'Aja pienten katujen kautta, niin pääset nopeammin perille.',
      sami: 'Vuolggán unnit luottaid mielde, de beasat johtilabbot.'
    }
  },
  'pohjantie': {
    term: 'Valtatie 4',
    finnishTerm: 'Pohjantie (Valtatie 4 Oulun kohdalla)',
    definition: {
      fi: 'Oulun läpi kulkeva nelikaistainen moottoritie, joka on koko Pohjois-Suomen tärkein maantie- ja rahtiliikenteen väylä.',
      en: 'The 4-lane motorway artery slicing through Oulu, carrying the heaviest freight and commuter traffic in Northern Finland.',
      selko: 'Oulun iso moottoritie. Sitä pitkin ajavat sekä rekat että henkilöautot.',
      sami: 'Oulu stuorra mohtorluodda mas mannet ollu rekat ja biillat.'
    },
    culturalContext: {
      fi: 'Pohjantiellä sattuvat kolarit ja esteet vaikuttavat välittömästi koko kaupungin liikenteen sujuvuuteen.',
      en: 'Any incident on Pohjantie instantly affects surrounding city streets as drivers seek detours.',
      selko: 'Jos Pohjantiellä on kolari, koko Oulun liikenne hidastuu.',
      sami: 'Jus Pohjantie-luoddas lea lihkohisvuohta, de olles gávpoga johtolat njoazula.'
    },
    statuteAnchor: 'Tieliikennelaki (729/2018) § 15',
    practicalTip: {
      fi: 'Pidä aina riittävä turvaväli raskaaseen kalustoon talvikeleillä.',
      en: 'Keep generous following distance from heavy trucks, especially in winter.',
      selko: 'Jätä tarpeeksi tilaa edellä ajavaan autoon.',
      sami: 'Atte doarvái saji ovddabealde vuoddji biilii.'
    }
  },
  'rotuaari': {
    term: 'Rotuaari',
    finnishTerm: 'Rotuaari (Oulun kävelykatu)',
    definition: {
      fi: 'Oulun keskustan lämmitetty kävelykatuosuus Kirkkokadulla, kaupungin keskeinen kohtaamispaikka ja kaupallinen sydän.',
      en: 'Oulu’s heated pedestrian high-street along Kirkkokatu, the central meeting point and social core of downtown.',
      selko: 'Oulun keskustan kävelykatu. Katu on lämmitetty, joten lumi sulaa siitä pois.',
      sami: 'Oulu guovddáža vázzinluodda mii lea liggejuvvon dálvet.'
    },
    culturalContext: {
      fi: 'Rotuaarilla ja sen maamerkillä, Rotuaarin pallolla, tavataan ystäviä. Kadun alla kiertää lämpöputkisto, joten se pysyy sulana talvellakin.',
      en: 'Famous for the Rotuaari Ball landmark. Geothermal/waste heat keeps the pavement free of ice and snow all winter.',
      selko: 'Rotuaarin pallolla tavataan usein kavereita. Katu ei ole liukas.',
      sami: 'Olbmot deaivvadit Rotuaari-spáppas. Geaidnu ii leat jikŋon.'
    },
    statuteAnchor: 'Oulun kaupungin keskustavisio & Järjestyslaki (612/2003)',
    practicalTip: {
      fi: 'Rotuaarilla ja Valkeassa on aina järjestyksenvalvojia ja valvontakameroita turvaamassa asiointia.',
      en: 'Rotuaari and Valkea have active security patrols and CCTV surveillance for pedestrian safety.',
      selko: 'Keskustassa on aina vartijoita, jotka auttavat tarvittaessa.',
      sami: 'Guovddážis leat álo fáktát geat veahkehit dárbbu mielde.'
    }
  },
  'poliisipartio': {
    term: 'Poliisipartio',
    finnishTerm: 'Poliisipartio (Oulun poliisilaitos)',
    definition: {
      fi: 'Oulun poliisin hälytyspartio, joka valvoo yleistä järjestystä ja turvallisuutta sekä puuttuu nopeasti häiriöihin.',
      en: 'Oulu Police Department mobile patrol unit responding to emergencies and maintaining civic order.',
      selko: 'Poliisiauto ja kaksi poliisia, jotka valvovat järjestystä ja auttavat ihmisiä.',
      sami: 'Bolesat geat vuodjet biillain ja dorvvastit olbmuid.'
    },
    culturalContext: {
      fi: 'Suomalainen poliisi nauttii yli 90 prosentin kansalaisturvaa ja luottamusta. Poliisilta voi aina kysyä neuvoa matalalla kynnyksellä.',
      en: 'Finnish police enjoy 90%+ public trust. You can approach any officer without fear for directions or help.',
      selko: 'Poliisi auttaa aina. Voit kysyä neuvoa poliisilta turvallisesti.',
      sami: 'Bolesii sáhttá álo luohttit ja jearrat veahki.'
    },
    statuteAnchor: 'Poliisilaki (872/2011) & Hätänumero 112',
    practicalTip: {
      fi: 'Hätätilanteessa soita 112. Voit ladata puhelimeen 112 Suomi -sovelluksen tarkan sijainnin välittämiseksi.',
      en: 'For emergencies call 112. The 112 Suomi app automatically transmits your exact GPS location.',
      selko: 'Hätänumero on 112. Se on ilmainen puhelu.',
      sami: 'Heahtenummar lea 112. Dasa lea nuvttá riŋget.'
    }
  },
  'alkusammutus': {
    term: 'Alkusammutus',
    finnishTerm: 'Alkusammutus (Käsisammutin, sammutuspeite tai lumi)',
    definition: {
      fi: 'Tulipalon sammuttaminen sen ensihetkinä käytettävissä olevilla välineillä ennen kuin palo ehtii levitä.',
      en: 'First-response firefighting using handheld extinguishers, fire blankets, or snow before fire crews arrive.',
      selko: 'Palon sammuttaminen heti alussa sammuttimella, peitteellä tai lumella.',
      sami: 'Dola jáddadeapmi dakkaviđe jáddadanspeittagiin dahje muohttagiin.'
    },
    culturalContext: {
      fi: 'Pohjoisessa lumi on erinomainen hätäsammutuskeino pihoilla auton moottoritilassa tai roskiksissa kytevälle palolle.',
      en: 'In northern climates, clean snow is an effective emergency smothering agent for engine compartment fires.',
      selko: 'Lumikola tai lumilapio auttaa tukahduttamaan pienen tulipalon ulkona.',
      sami: 'Muohta jáddada unna dola olgun hui bures.'
    },
    statuteAnchor: 'Pelastuslaki (379/2011) § 14 & SPEK Alkusammutuskoulutus',
    practicalTip: {
      fi: 'Jos moottorista nousee savua, älä avaa konepeltiä kokonaan, jotta happi ei leimauta tulta. Suihkuta sammutetta raosta.',
      en: 'If a car engine smokes, do NOT pop the hood fully open — oxygen feeds flames. Spray through the narrow gap.',
      selko: 'Älä avaa auton peltiä auki asti, ettei tuli saa ilmaa. Heitä lunta raosta.',
      sami: 'Ale raba biilla heandaga ollásit, ammes buollá eanet.'
    }
  },
  'musta-jää': {
    term: 'Musta jää',
    finnishTerm: 'Musta jää (Peililiukas asfaltti)',
    definition: {
      fi: 'Näkymätön, ohut ja läpinäkyvä jääkerros tienpinnalla, joka näyttää vain märältä asfaltilta mutta on peililiukas.',
      en: 'Transparent thin ice coating on asphalt. Looks like wet road but offers near zero tire friction.',
      selko: 'Näkymätön ja todella liukas jää asfaltilla. Tie näyttää märältä, mutta on jäässä.',
      sami: 'Čáhppes jiekŋa mii ii oidno bures, muhto lea hui njuolggus.'
    },
    culturalContext: {
      fi: 'Musta jää syntyy usein silloin, kun ilman lämpötila laskee nollan alapuolelle kostean sään jälkeen. Se yllättää autoilijat ja pyöräilijät.',
      en: 'Forms rapidly when temperatures hover near 0°C with damp air. Locals test footing before trusting asphalt.',
      selko: 'Jää syntyy usein aamulla ja illalla, kun lämpötila laskee pakkaselle.',
      sami: 'Jiekŋa šaddá go lea buolaš ja áibmu lea njuoskkas.'
    },
    statuteAnchor: 'Liikenneturva: Talviliikennevaroitus Luokka 1',
    practicalTip: {
      fi: 'Käytä kengissä liukuesteitä ja autossa nastarenkaita. Polkupyörään suositellaan nastarenkaita marraskuusta huhtikuuhun.',
      en: 'Wear shoe grips (liukuesteet) and equip bicycles with studded winter tires (nastarenkaat).',
      selko: 'Laita kenkiin liukuesteet ja pyörään talvirenkaat.',
      sami: 'Bija skuovaide njuolggandorvvu ja sihkkelii dálvegummiid.'
    }
  },
  'baana': {
    term: 'Baana',
    finnishTerm: 'Oulun Baana (Pyöräilyn pääväyläverkosto)',
    definition: {
      fi: 'Oulun huippuluokan pyöräilybaanaverkosto, jolla on talvisin ensiluokkainen harjasuolaus- ja aurauskunnossapito.',
      en: 'Oulu’s premier cycling arterial network, maintained with heated broom-sweeping and anti-icing salt brine.',
      selko: 'Oulun leveä pääpyörätie. Se puhdistetaan lumesta ja jäästä aina ensimmäisenä.',
      sami: 'Oulu buoremus sihkkelgeaidnu mii lea álo buhtis muohttagis ja jieŋas.'
    },
    culturalContext: {
      fi: 'Oulu on kansainvälisesti tunnettu maailman parhaana talvipyöräilykaupunkina. Baanoilla pyöräillään kouluun ja yliopistolle läpi talven.',
      en: 'Oulu is universally hailed as the world capital of winter cycling. University students commute daily at −20°C.',
      selko: 'Oulussa pyöräillään töihin ja yliopistolle myös talvipakkasella.',
      sami: 'Oulus olbmot sihkkeldallet skuvlii ja bargui dálvetge.'
    },
    statuteAnchor: 'Oulun kaupungin pyöräilyväylien hoitoluokka A1',
    practicalTip: {
      fi: 'Baana Linnanmaan yliopistolta keskustaan pidetään sulana ja asfalttipintaisena ilman liukkautta.',
      en: 'The Baana route between Linnanmaa campus and city center is kept bare asphalt without slippery pack-ice.',
      selko: 'Baanaa pitkin pääset nopeasti yliopistolle ilman liukastumista.',
      sami: 'Baanas beasat johtilit universitehtii almmá njuolggama haga.'
    }
  },
  'osl-bussit': {
    term: 'OSL-bussit',
    finnishTerm: 'Oulun seudun liikenne (OSL)',
    definition: {
      fi: 'Oulun seudun julkinen joukkoliikenneverkosto, jonka punavalkoiset bussit palvelevat koko kaupunkiseutua.',
      en: 'Oulu Region Transport Authority operating local bus transit with contactless ticketing and live GPS tracking.',
      selko: 'Oulun paikallisbussit. Bussit ovat punavalkoisia.',
      sami: 'Oulu guovllu linjábiillat mat leat rukses-vilggodat.'
    },
    culturalContext: {
      fi: 'Talvella bussit ovat turvallinen tapa liikkua, mutta peilijäisillä keleillä reitit saattavat myöhästyä 10–15 minuuttia.',
      en: 'Buses are the safest bad-weather backup. Real-time arrival maps prevent freezing at bus stops.',
      selko: 'Talvella bussi voi olla vähän myöhässä, mutta se on turvallinen kyyti.',
      sami: 'Dálvet bussi sáhttá leat veháš maŋŋonan, muhto dat lea dorvvolaš.'
    },
    statuteAnchor: 'Oulun kaupungin joukkoliikennelautakunta & Waltti-lippujärjestelmä',
    practicalTip: {
      fi: 'Maksat kertalipun helposti lähimaksulla suoraan pankkikortilla bussin etulaitteeseen (ei käteistä).',
      en: 'Tap your contactless credit/debit card on the bus reader for instant payment (cash is not accepted).',
      selko: 'Voit maksaa bussissa helposti pankkikortilla. Älä käytä käteistä.',
      sami: 'Mávsse linjábiillas njuolgga báŋkokorttain.'
    }
  },
  'kivisydan': {
    term: 'Kivisydän',
    finnishTerm: 'Kivisydän (Maanalainen pysäköintilaitos ja elämysluola)',
    definition: {
      fi: 'Oulun keskustan alle kallioon louhittu moderni pysäköintilaitos ja suojatila, josta on suorat hissit kauppakeskuksiin.',
      en: 'Massive subterranean granite facility beneath Oulu center with direct elevator links to pedestrian streets.',
      selko: 'Oulun keskustan alla oleva iso kallioluola ja parkkihalli. Sieltä pääsee hisseillä suoraan kauppoihin.',
      sami: 'Oulu guovddáža vuolde leahkki stuorra bákteroggi mas leat hissat gávppijdii.'
    },
    culturalContext: {
      fi: 'Kivisydämessä on tasainen lämpötila (+16°C) läpi vuoden. Se toimii myös kulttuuritapahtumien ja taideteosten uniikkina näyttelytilana.',
      en: 'Maintains a constant +16°C year-round. Frequently hosts underground contemporary art and light festivals.',
      selko: 'Kivisydämessä on aina lämmintä, vaikka ulkona olisi kova pakkanen.',
      sami: 'Bákterokkis lea álo liekkas (+16°C) vaikko olgun lea buolaš.'
    },
    statuteAnchor: 'Oulun Pysäköinti Oy & Väestönsuojeluasetus',
    practicalTip: {
      fi: 'Pääset Kivisydämeen lasihisseillä suoraan Rotuaarin kävelykadulta ja kauppakeskus Valkeasta ilman ulkovaatteita.',
      en: 'Glass elevators in Rotuaari square and Valkea shopping center drop directly into Kivisydän.',
      selko: 'Mene hissiin Rotuaarilta tai Valkeasta, niin pääset suoraan alas lämpimään.',
      sami: 'Váldde hissa Rotuaaris ja beasat njuolgga liegga sadjái.'
    }
  },
  'pelastuslaitos': {
    term: 'Pelastuslaitos',
    finnishTerm: 'Pohjois-Pohjanmaan pelastuslaitos',
    definition: {
      fi: 'Alueellinen pelastusviranomainen, joka vastaa sammutus-, pelastus- ja ensihoitotehtävistä Oulun seudulla.',
      en: 'Regional rescue services responsible for fire, accident, and emergency medical operations in Oulu.',
      selko: 'Palomiehet ja ensihoitajat, jotka auttavat onnettomuuksissa ja tulipaloissa.',
      sami: 'Báikkálaš gádjunlágádus mii jáddada doliid ja veahkeha lihkohisvuođain.'
    },
    culturalContext: {
      fi: 'Pelastuslaitos tiedottaa aktiivisesti vaaroista ja opastaa kansalaisia turvalliseen toimintaan arjessa.',
      en: 'Finnish rescue services emphasize proactive citizen education and rapid clearance of transit hazards.',
      selko: 'Pelastuslaitos huolehtii siitä, että teillä ja kodeissa on turvallista.',
      sami: 'Gádjunlágádus fuolaha ahte buohkain lea dorvvolaš.'
    },
    statuteAnchor: 'Pelastuslaki (379/2011) & Hätäkeskuslaitos 112',
    practicalTip: {
      fi: 'Anna aina hälytysajoneuvolle esteetön kulku siirtymällä ajoradan reunaan.',
      en: 'Always pull over promptly to the edge of the road when emergency sirens approach.',
      selko: 'Väistä aina paloautoa ja ambulanssia.',
      sami: 'Atte álo saji gádjunbiilii go gulat sirenaid.'
    }
  }
};

export const STORY_SLIDES: StorySlide[] = [
  // 1. REAL INCIDENT: VT4 Kaakkurin ramppi (22.-24.10.2026)
  {
    id: 'story-1-kaakkuri-vt4',
    category: 'TRANSIT',
    categoryLabel: {
      fi: 'LIIKENNEHÄIRIÖ',
      en: 'TRAFFIC ALERT',
      selko: 'LIIKENNE',
      sami: 'JOHTOLAT'
    },
    district: 'Pohjantie (VT4) • Kaakkuri',
    timeAgo: 'Päivitetty 35 min sitten',
    jsnStatus: 'JSN § 10 Tarkistettu',
    credibilityScore: 99,
    diagram: {
      problem: {
        icon: '🚛💥📦',
        image: 'https://images.unsplash.com/photo-1542282088-72c9c27ed0cd?auto=format&fit=crop&w=800&q=80',
        caption: 'VT4 Kaakkuri • Kaista suljettu',
        title: {
          fi: 'Tie tukossa Kaakkurissa',
          en: 'Highway Blocked: Cargo on Road',
          selko: 'Tie on poikki: Tavaraa tiellä',
          sami: 'Geaidnu lea gitta: Dávvirat luoddas'
        },
        detail: {
          fi: 'Rekan kuorma levisi tielle, 2 km ruuhka.',
          en: 'Spilled cargo blocks lane, 2 km bottleneck.',
          selko: 'Rekan tavaraa putosi tielle. Pitkä jono.',
          sami: 'Reka dávvirat luoddas. Guhkes ráidu.'
        },
        badge: {
          fi: 'KAISTA SULJETTU',
          en: 'LANE BLOCKED',
          selko: 'TIE SULJETTU',
          sami: 'LUODDA GITTA'
        },
        color: 'red'
      },
      arrowLabel: {
        fi: 'SUOSITELTU KIERTOTIE ⬇️',
        en: 'RECOMMENDED DETOUR ⬇️',
        selko: 'AJA TÄSTÄ OHI ⬇️',
        sami: 'VUOLGGÁN DÁN LUODDA MIELDE ⬇️'
      },
      solution: {
        icon: '🔄🚗✅',
        image: 'https://images.unsplash.com/photo-1502877338535-766e1452684a?auto=format&fit=crop&w=800&q=80',
        caption: 'Kaakkurintie • Vapaa kiertoreitti',
        title: {
          fi: 'Kierrä rampin kautta',
          en: 'Exit via Kaakkuri Interchange',
          selko: 'Aja Kaakkurin rampin kautta',
          sami: 'Mane Kaakkuri luoddaearu mielde'
        },
        detail: {
          fi: 'Poistu Kaakkurintielle tai Iinatin kautta. Vältät 20 min jonon.',
          en: 'Exit to Kaakkurintie or through Iinatti. Save 20 min.',
          selko: 'Aja pikkuteiden kautta. Vältät pitkän ruuhkan.',
          sami: 'Mane unnit luottaid mielde ja garvve ráiddu.'
        },
        badge: {
          fi: 'REITTI VAPAA',
          en: 'FREE ROUTE',
          selko: 'VAPAA TIE',
          sami: 'RABA LUODDA'
        },
        color: 'emerald'
      }
    },
    headline: {
      fi: 'Rekasta irtosi kuormalavallinen tavaraa Pohjantielle Kaakkurissa – Pelastuslaitos raivaa ajorataa',
      en: 'Cargo dropped from truck onto Pohjantie motorway at Kaakkuri – Crews clearing lane',
      selko: 'Rekasta putosi tavaraa moottoritielle Kaakkurissa – Palokunta siivoaa tietä',
      sami: 'Rekas gahčče dávvirat mohtorluoddii Kaakkuris – Gádjunlágádus buhtista luotta'
    },
    bullet1: {
      fi: 'Valtatie 4 etelään vievällä kaistalla tapahtui vaaratilanne, kun rekan ovesta levinnyt kuorma osui takana tulleeseen autoon Kaakkurin ramppi kohdalla.',
      en: 'Hazard on Route 4 south: dropped pallet cargo struck a following passenger car near Kaakkuri.',
      selko: 'Rekan ovi aukesi ja tavaraa putosi auton eteen Kaakkurissa. Kukaan ei loukkaantunut.',
      sami: 'Valtatie 4 -luoddas gahčče dávvirat biilla ovdii Kaakkuris. Ii oktage roasmmohuvvan.'
    },
    bullet2: {
      fi: 'Pelastuslaitos ja poliisi ohjaavat liikennettä. Henkilövahinkoja ei tullut, mutta Valtatie 4 ruuhka etelään on jo 2 kilometriä.',
      en: 'Police and rescue services on scene. No injuries reported; southbound queue stretches 2 km.',
      selko: 'Poliisi ja Pelastuslaitos ohjaavat autoja. Tiellä on kahden kilometrin autojono.',
      sami: 'Bolesat ja gádjunlágádus stivrejit biillaid. Luoddas lea guovtti kilomehtera ráidu.'
    },
    keywords: ['kaakkurin-ramppi', 'pohjantie', 'pelastuslaitos'],
    solution: {
      badge: {
        fi: 'LIIKENNETIEDOTE',
        en: 'TRAFFIC NOTICE',
        selko: 'LIIKENNEOHJE',
        sami: 'JOHTOLATDIEHTU'
      },
      text: {
        fi: 'Käytä kiertotietä: Käänny Kaakkurin rampista Kaakkurintielle tai Iinatin kautta Limingantulliin.',
        en: 'Use detour: Exit at Kaakkuri interchange to Kaakkurintie or through Iinatti.',
        selko: 'Aja Kaakkurin rampin kautta pikkuteille, niin et jää jumiin ruuhkaan.',
        sami: 'Mane unnit luottaid mielde Kaakkurintie bokte.'
      },
      actionLabel: {
        fi: 'Avaa Fintraffic-kartta & Kiertotie',
        en: 'Open Detour Map & Traffic Status',
        selko: 'Katso kartta ja kiertotie',
        sami: 'Raba kártta ja ođđa geainnu'
      },
      actionType: 'MAP'
    },
    traditionalDepth: {
      leadParagraph: {
        fi: 'Pohjantiellä sattui torstaina vaarallinen välikohtaus, kun Oulun Kaakkurin liittymän kohdalla etelän suuntaan ajaneesta rekasta putosi ajoradalle kokonainen kuormalavallinen tavaraa. Takana ajanut henkilöauto vaurioitui.',
        en: 'A hazardous incident occurred on Pohjantie when a full freight pallet fell from a semi-trailer into the southbound lanes near Kaakkuri interchange, damaging a trailing passenger vehicle.',
        selko: 'Moottoritiellä tapahtui vaaratilanne Oulussa. Rekasta putosi tavaraa tielle Kaakkurissa. Takana tullut henkilöauto kolhiintui, mutta ihmiset säilyivät ehjinä.',
        sami: 'Mohtorluoddas dáhpáhuvai váralaš dilli go rekas gahčče dávvirat luoddii Kaakkuris. Biila maŋis bávhkai dávviriidda.'
      },
      bodyText: {
        fi: 'Pohjois-Pohjanmaan pelastuslaitoksen ja poliisin mukaan rekan perävaunun sivukaapin ovi oli auennut ajon aikana yllättäen. Ajoradalle levinnyt kuorma vaurioitti takana tulleen auton keulaa, mutta kuljettaja selvisi säikähdyksellä ja henkilövahingoilta vältyttiin.\n\nPelastuslaitos sulki toisen etelään vievistä kaistoista raivaustöiden ajaksi. Onnettomuuspaikalle muodostui nopeasti noin kahden kilometrin mittainen liikennesumpu. Poliisi ohjasi osan liikenteestä Kaakkurin eritasoliittymän kautta rinnakkaistieverkolle. Kunnossapito varmisti tien puhtauden ennen kaistan avaamista.',
        en: 'According to Northern Ostrobothnia Rescue Services, the side access compartment of the freight trailer unlocked unexpectedly. The debris impacted the front bumper of a following car. No physical injuries occurred.\n\nCrews blocked one southbound lane for safe removal. Heavy congestion backed up for nearly two kilometers. Traffic was diverted onto the local Kaakkurintie street network until the highway was certified clear.',
        selko: 'Pelastuslaitos ja poliisi tulivat nopeasti paikalle. Tie siivottiin roskista ja tavaroista. Toinen kaista oli kiinni hetken aikaa, minkä vuoksi syntyi autojonoa. Nyt tie on jälleen puhdas ja turvallinen ajaa.',
        sami: 'Gádjunlágádus ja bolesat bohte dakkaviđe báikái. Luodda buhtistuvvui johtilit ja lea dál fas raba ja dorvvolaš.'
      },
      reporterName: 'Antti Ervasti, Kalevan aluetoimitus',
      section: 'Oulu & Liikenne'
    }
  },

  // 2. REAL INCIDENT: Keskusta & Rotuaari yöhäiriö (23.-24.10.2026)
  {
    id: 'story-2-rotuaari-keskusta',
    category: 'EMERGENCY',
    categoryLabel: {
      fi: 'POLIISIOPERAATIO',
      en: 'POLICE REPORT',
      selko: 'POLIISI',
      sami: 'BOLES'
    },
    district: 'Keskusta • Rotuaari & Kauppatori',
    timeAgo: 'Päivitetty 1 tunti sitten',
    jsnStatus: 'JSN § 10 Tarkistettu',
    credibilityScore: 98,
    diagram: {
      isResolved: true,
      problem: {
        icon: '🎭📢🏃‍♂️',
        image: 'https://images.unsplash.com/photo-1508849789987-4e5333c12b78?auto=format&fit=crop&w=800&q=80',
        caption: 'Rotuaari yöllä • Poliisitehtävä',
        title: {
          fi: 'Yöllinen häiriö Rotuaarilla',
          en: 'Night Disturbance on Rotuaari',
          selko: 'Meteliä yöllä keskustassa',
          sami: 'Ráfehisvuohta guovddážis ihkku'
        },
        detail: {
          fi: 'Nuorisojoukko aiheutti häiriötä kävelykadulla.',
          en: 'Masked youth group caused disturbance on the pedestrian precinct.',
          selko: 'Naamioituneet nuoret huusivat ja pitivät meteliä kävelykadulla.',
          sami: 'Maskejuvvon nuorat muosehihted olbmuid vázzinluoddas.'
        },
        badge: {
          fi: 'HÄIRIÖTILA',
          en: 'DISTURBANCE',
          selko: 'HÄIRIÖ',
          sami: 'MUOSEHUHUS'
        },
        color: 'red'
      },
      arrowLabel: {
        fi: 'TILANNE NYT RAUHOITETTU ⬇️',
        en: 'SITUATION RESTORED ⬇️',
        selko: 'KAIKKI ON NYT HYVIN ⬇️',
        sami: 'DILLI LEA FAS RÁFÁLAŠ ⬇️'
      },
      solution: {
        icon: '✅',
        image: 'https://images.unsplash.com/photo-1519501025264-65ba15a82390?auto=format&fit=crop&w=800&q=80',
        caption: 'Keskusta turvallinen • Tilanne ohi',
        title: {
          fi: 'Tilanne on ratkaistu, lisätoimenpiteitä ei vaadita.',
          en: 'Situation resolved, no additional actions required.',
          selko: 'Tilanne on ratkaistu, lisätoimenpiteitä ei vaadita.',
          sami: 'Dilli lea čielggaduvvon, eai dárbbašuvvo lassedoaimmat.'
        },
        detail: {
          fi: 'Poliisi otti kuusi häirikköä kiinni. Keskusta ja Valkea ovat rauhallisia.',
          en: 'Police detained six individuals. High-street and Valkea mall completely secure.',
          selko: 'Poliisi otti häiriköt kiinni. Voit liikkua keskustassa turvallisesti.',
          sami: 'Bolesat válde guhtta olbmo gitta. Guovddáš lea fas dorvvolaš.'
        },
        badge: {
          fi: 'TILANNE HALLINNASSA',
          en: 'SECURED',
          selko: 'TURVALLINEN',
          sami: 'DORVVOLAŠ'
        },
        color: 'emerald'
      }
    },
    headline: {
      fi: 'Naamioitunut seurue aiheutti yöllä häiriötä Oulun keskustassa – Poliisi otti kiinni kuusi henkilöä',
      en: 'Masked group caused nighttime disruption in Oulu center – Police detained six',
      selko: 'Naamioituneet henkilöt aiheuttivat meteliä Oulussa – Poliisi otti kiinni 6 nuorta',
      sami: 'Maskejuvvon joavkku muosehii Oulus ihkku – Bolesat válde gitta guhtta olbmo'
    },
    bullet1: {
      fi: 'Perjantain ja lauantain välisenä yönä Rotuaari alueella liikkunut noin kymmenen hengen joukko häiritsi kaupunkilaisia ja pyrki karkuun poliisia.',
      en: 'A group of ~10 masked individuals startled pedestrians near Rotuaari after midnight and fled when approached.',
      selko: 'Noin kymmenen naamioitunutta ihmistä piti kovaa ääntä ja juoksi karkuun poliisia.',
      sami: 'Logi olbmo maskkain gárvvodan muosehedje olbmuid ja viehke eret bolesiin.'
    },
    bullet2: {
      fi: 'Oulun poliisilaitoksen useat partiot saartoivat alueen nopeasti. Kuusi henkilöä otettiin kiinni rikoksilta ja häiriöiltä suojaamiseksi.',
      en: 'Multiple police patrols contained the precinct swiftly. Six individuals detained to protect public order.',
      selko: 'Poliisipartio otti kiinni kuusi häiriköitsijää. Sivullisille ei aiheutunut vaaraa.',
      sami: 'Poliisipartio válddii gitta guhtta olbmo. Eai leat earát vaháguvvon.'
    },
    keywords: ['rotuaari', 'poliisipartio', 'kivisydan'],
    solution: {
      badge: {
        fi: 'TURVALLISUUSINFO',
        en: 'PUBLIC SAFETY',
        selko: 'TURVAOHJE',
        sami: 'DORVVODIEHTU'
      },
      text: {
        fi: 'Keskustan kävelykatu on normaali ja turvallinen. Mikäli havaitset häiriöitä yöelämässä, ota yhteys poliisiin numerossa 112.',
        en: 'Downtown pedestrian zone is fully secure. For any suspicious night activity, contact police at 112.',
        selko: 'Keskustassa on turvallista kävellä ja asioida. Hätätilanteessa soita aina 112.',
        sami: 'Guovddážis lea dorvvolaš vázzit. Heahtedilis riŋge álo 112.'
      },
      actionLabel: {
        fi: 'Oulun poliisin virallinen tiedote',
        en: 'Official Police Bulletin',
        selko: 'Lue poliisin tiedote',
        sami: 'Loga bolesa dieđu'
      },
      actionType: 'VERIFY'
    },
    traditionalDepth: {
      leadParagraph: {
        fi: 'Oulun keskustassa herätti lauantain vastaisena yönä huomiota ja hämmennystä noin kymmenen hengen naamioitunut nuorisoseurue, joka liikkui huudellen ja aiheutti järjestyshäiriöitä kävelykadun ravintoloiden ja asuintalojen lähistöllä.',
        en: 'Public order units responded past midnight in central Oulu after a masked youth cohort caused loud disruptions along the pedestrian dining and commercial strip.',
        selko: 'Oulun keskustassa oli yöllä häiriö, kun naamioituneet henkilöt huusivat ja pitivät meteliä kadulla. Poliisi saapui nopeasti paikalle.',
        sami: 'Oulu guovddážis lei ihkku ráfehisvuohta go maskkain gárvvodan nuorat čurrejedje luoddas. Bolesat bohte dakkaviđe.'
      },
      bodyText: {
        fi: 'Poliisin mennessä puhuttamaan seuruetta osa heistä lähti juoksemaan karkuun kauppakeskus Valkean ja Torikadun suuntiin. Useat poliisipartiot tavoittivat joukosta kuusi henkilöä ja ottivat heidät kiinni poliisilain nojalla rikoksilta ja häiriöiltä suojaamiseksi.\n\nPoliisin mukaan sivullisille ei aiheutunut tilanteessa fyysistä vaaraa. Vastaavanlaisia naamioituneiden nuorten ryhmittymisiä on havaittu syksyn aikana myös muissa Suomen kaupungeissa. Oulun poliisi jatkaa tehostettua näkyvää valvontaa viikonloppuisin.',
        en: 'When officers approached, several subjects fled towards Valkea mall and Torikatu. Responding units apprehended six individuals under the Police Act for public safety protection.\n\nPolice confirmed no weapons were displayed and no citizens were injured. Similar flash-mob occurrences have been monitored nationally. Enhanced weekend patrols continue across Oulu core.',
        selko: 'Poliisi otti kuusi henkilöä kiinni rauhoittaakseen keskustan. Kukaan ei loukkaantunut. Keskustassa on nyt rauhallista ja vartijat sekä poliisi valvovat aluetta.',
        sami: 'Bolesat válde guhtta olbmo gitta ja dilli ráfáiduvai. Ii oktage roasmmohuvvan. Guovddáš lea fas dorvvolaš.'
      },
      reporterName: 'Kari Sankala, Kalevan rikos- ja oikeustoimitus',
      section: 'Oulu & Turvallisuus'
    }
  },

  // 3. REAL DOMESTIC EVENT: Oulunsalo aamuinen autopalo (22.-24.10.2026)
  {
    id: 'story-3-oulunsalo-autopalo',
    category: 'EMERGENCY',
    categoryLabel: {
      fi: 'PELASTUSTEHTÄVÄ',
      en: 'RESCUE ACTION',
      selko: 'PELASTUS',
      sami: 'GÁDJUN'
    },
    district: 'Oulunsalo • Omakotialue',
    timeAgo: 'Päivitetty 2 tuntia sitten',
    jsnStatus: 'JSN § 10 Tarkistettu',
    credibilityScore: 99,
    diagram: {
      isResolved: true,
      problem: {
        icon: '🚗🔥💨',
        image: 'https://images.unsplash.com/photo-1517524206127-48bbd363f3d7?auto=format&fit=crop&w=800&q=80',
        caption: 'Oulunsalo • Autopalo pihassa',
        title: {
          fi: 'Autopalo asuinpihalla',
          en: 'Car Fire Near Residence',
          selko: 'Autopalo talon pihalla',
          sami: 'Biilla buollin dálus'
        },
        detail: {
          fi: 'Moottoritila syttyi pakkasaamuna asuintalon vieressä.',
          en: 'Car engine caught fire on freezing morning near residence.',
          selko: 'Auto syttyi palamaan aamulla pihassa. Savua nousi konepellin alta.',
          sami: 'Biilla mohtor buollái iđđedis. Suovva measta manai dállui.'
        },
        badge: {
          fi: 'TULIPALO',
          en: 'FIRE HAZARD',
          selko: 'PALO',
          sami: 'DOALLA'
        },
        color: 'red'
      },
      arrowLabel: {
        fi: 'NOPEA ALKUSAMMUTUS PELASTI ⬇️',
        en: 'FIRST-AID EXTINGUISHING SAVED IT ⬇️',
        selko: 'NOPEA SAMMUTUS PELASTI ⬇️',
        sami: 'JOHTILIS JÁDDADEAPMI GÁDJUI ⬇️'
      },
      solution: {
        icon: '✅',
        image: 'https://images.unsplash.com/photo-1542838132-92c53300491e?auto=format&fit=crop&w=800&q=80',
        caption: 'Talo ja piha turvassa',
        title: {
          fi: 'Tilanne on ratkaistu, lisätoimenpiteitä ei vaadita.',
          en: 'Situation resolved, no additional actions required.',
          selko: 'Tilanne on ratkaistu, lisätoimenpiteitä ei vaadita.',
          sami: 'Dilli lea čielggaduvvon, eai dárbbašuvvo lassedoaimmat.'
        },
        detail: {
          fi: 'Naapuri sammutti liekit lumella. Palo ei levinnyt taloon.',
          en: 'Neighbor smothered flames with snow. Home saved.',
          selko: 'Naapuri heitti lunta ja sammutti tulen. Vaara on ohi.',
          sami: 'Ránnjá jáddadii dola muohttagiin. Dállu lea dorvvolaš.'
        },
        badge: {
          fi: 'VAARA OHI',
          en: 'SAFE',
          selko: 'TURVASSA',
          sami: 'DORVVOLAŠ'
        },
        color: 'emerald'
      }
    },
    headline: {
      fi: 'Henkilöauto syttyi palamaan aamulla Oulunsalossa – Naapurin nopea alkusammutus esti talon vauriot',
      en: 'Car erupted in flames in Oulunsalo morning – Neighbor’s quick extinguishing prevented house fire',
      selko: 'Auto syttyi palamaan aamulla Oulunsalossa – Naapuri sammutti palon lumella',
      sami: 'Biila buollái iđđedis Oulunsalos – Ránnjá jáddadii dola muohttagiin'
    },
    bullet1: {
      fi: 'Oulunsalossa omakotitalon pihassa seissyt henkilöauto syttyi tuleen varhain aamulla. Naapuri huomasi savun ja hälytti apua.',
      en: 'A passenger vehicle caught fire in a driveway in Oulunsalo. An observant neighbor spotted smoke and dialed 112.',
      selko: 'Pihassa ollut auto alkoi palaa aamulla. Naapuri näki savun ja soitti hätänumeroon.',
      sami: 'Biila buollái dálosa šiljus iđđedis. Ránnjá oinnii suova ja riŋgii 112:i.'
    },
    bullet2: {
      fi: 'Auton omistaja ja sivullinen tekivät tehokkaan alkusammutus lumella ja jauhesammuttimella. Pelastuslaitos hoiti jälkivarmistuksen.',
      en: 'The owner and bystander executed rapid suppression using snow and powder extinguisher before crews arrived.',
      selko: 'Omistaja ja naapuri tekivät alkusammutuksen lumella. Pelastuslaitos tarkisti tilanteen.',
      sami: 'Eaiggát ja ránnjá jáddadeigga dola muohttagiin. Palokunta dárkkistii dili.'
    },
    keywords: ['alkusammutus', 'pelastuslaitos', 'musta-jää'],
    solution: {
      badge: {
        fi: 'KOTITURVA-VINKKI',
        en: 'HOME SAFETY',
        selko: 'KOTIVINKKI',
        sami: 'RUOVDDORVODIEHTU'
      },
      text: {
        fi: 'Tarkista aina talvella auton lämmitysjohdon kunto. Pidä kodissa ja autossa aina toimiva 6 kg jauhesammutin ja sammutuspeite.',
        en: 'Inspect engine heater cables for winter wear. Keep a certified 6kg dry powder extinguisher and fire blanket at hand.',
        selko: 'Tarkista auton lämmitysjohto pakkasella. Pidä kotona aina käsisammutin ja sammutuspeite.',
        sami: 'Dárkkis biilla liekkasjohtosa dálvet. Ane álo sammutina ruovttus.'
      },
      actionLabel: {
        fi: 'Pelastuslaitoksen talvipaloturvallisuusohje',
        en: 'Fire Safety Guidelines',
        selko: 'Lue talviset paloturvaohjeet',
        sami: 'Loga buollindorvodieđuid'
      },
      actionType: 'GUIDE'
    },
    traditionalDepth: {
      leadParagraph: {
        fi: 'Oulunsalolaisen omakotitalon pihassa koettiin varhain aamulla säikähdyttäviä hetkiä, kun pysäköidyn henkilöauton moottoritilasta alkoi tupruta sakeaa savua ja liekkejä. Ripeä toiminta kuitenkin esti suuronnettomuuden.',
        en: 'Tense moments unfolded in Oulunsalo as thick smoke and flames broke out from a stationary car parked close to an inhabited single-family wooden home.',
        selko: 'Oulunsalossa syttyi auto palamaan omakotitalon edessä. Naapurin nopea toiminta esti paloa leviämästä asuinrakennukseen.',
        sami: 'Oulunsalos buollái biila dálosa šiljus. Ránnjá jáddadii dola johtilit ja dállu gádjunii.'
      },
      bodyText: {
        fi: 'Pohjois-Pohjanmaan pelastuslaitoksen mukaan palon havaitsi ensimmäisenä viereisen kiinteistön asukas, joka riensi apuun ja ilmoitti hätäkeskukseen. Auton omistaja ja naapuri aloittivat välittömästi alkusammutustoimet käyttämällä pihalta löytynyttä lunta sekä jauhesammutinta.\n\nKun pelastuslaitoksen ensimmäinen sammutusyksikkö saapui kohteeseen, liekit oli jo pääosin saatu taltutettua. Palomiehet suorittivat moottoritilan lämpökameratarkastuksen, irrottivat akun ja varmistivat jälkisammutuksen. Pelastusviranomaiset kiittelevät kansalaisten mallikasta toimintaa.',
        en: 'Rescue officials confirmed the neighbor immediately alerted 112 and commenced smothering flames using available snowbanks and a powder extinguisher. By the time primary engines arrived, combustion was suppressed.\n\nFirefighters isolated the battery terminals, deployed thermal imaging, and doused residual hot spots. Authorities commended the exemplary prompt civilian response.',
        selko: 'Palomiehet kiittivät asukkaita hyvästä toiminnasta. Auto sammutettiin lumella ja sammuttimella ennen kuin palo ehti levitä taloon. Kukaan ei loukkaantunut.',
        sami: 'Palokunta giittii olbmuid buori barggus. Biila jáddaduvvui muohttagiin ovdal go dállu buollái. Ii oktage vaháguvvon.'
      },
      reporterName: 'Päivi Alasuutari, Kalevan kotimaantoimitus',
      section: 'Oulu & Arki'
    }
  },

  // 4. REAL TRANSIT/WEATHER: OSL bussit & Musta Jää / Baana (23.-24.10.2026)
  {
    id: 'story-4-osl-liukkaus-baana',
    category: 'TRANSIT',
    categoryLabel: {
      fi: 'JOUKKOLIIKENNE',
      en: 'TRANSIT & ROADS',
      selko: 'BUSSIT & PYÖRÄILY',
      sami: 'BUSSAT JA SIHKKEL'
    },
    district: 'Koko Oulu • Keskusta & Linnanmaa',
    timeAgo: 'Päivitetty 15 min sitten',
    jsnStatus: 'JSN § 10 Tarkistettu',
    credibilityScore: 99,
    diagram: {
      problem: {
        icon: '🧊🚌⚠️',
        image: 'https://images.unsplash.com/photo-1548777123-e216912df7d8?auto=format&fit=crop&w=800&q=80',
        caption: 'Ajoradat peilijäässä • Bussit +15 min',
        title: {
          fi: 'Musta jää hidastaa busseja',
          en: 'Black Ice Slows City Buses',
          selko: 'Jää teillä hidastaa busseja',
          sami: 'Čáhppes jiekŋa njoazula bussaid'
        },
        detail: {
          fi: 'Kosteus jäätyi ajoradoille. OSL-bussit 1, 2 ja 3 myöhässä 15 min.',
          en: 'Clear ice on roads. OSL city buses delayed 15 minutes.',
          selko: 'Tiet ovat liukkaita. Bussit myöhässä 15 minuuttia.',
          sami: 'Luottat leat jikŋon. Bussat maŋŋonan 15 min.'
        },
        badge: {
          fi: 'PÄÄKALLOKELI',
          en: 'BLACK ICE',
          selko: 'LIUKAS KELI',
          sami: 'NJUOLGGUS DÁLKI'
        },
        color: 'red'
      },
      arrowLabel: {
        fi: 'PARAS JA NOPEIN TAPA LIIKKUA ⬇️',
        en: 'FASTEST COMMUTE TODAY ⬇️',
        selko: 'NOPEIN REITTI TÄNÄÄN ⬇️',
        sami: 'JOHTILAMOS GEAIDNU ODNE ⬇️'
      },
      solution: {
        icon: '🚲✨⏱️',
        image: 'https://images.unsplash.com/photo-1485965120184-e220f721d03e?auto=format&fit=crop&w=800&q=80',
        caption: 'Baana harjasuolattu • Sula asfaltti',
        title: {
          fi: 'Pyöräile Baanaa tai katso GPS',
          en: 'Cycle Baana or Track Live Bus GPS',
          selko: 'Aja pyörällä Baanaa tai katso bussi puhelimesta',
          sami: 'Sihkkeldal Baana mielde dahje geahča bussa'
        },
        detail: {
          fi: 'Baana Linnanmaalle on sula ja hiekoitettu.',
          en: 'Baana cycleway to university is bare and salted.',
          selko: 'Pyörätie yliopistolle on puhdas. Katso bussi puhelimesta.',
          sami: 'Sihkkelgeaidnu lea buhtis. Geahča bussa telefovnnas.'
        },
        badge: {
          fi: 'REITTI AUKI',
          en: 'CLEARED',
          selko: 'PUHDAS TIE',
          sami: 'BUHTIS GEAIDNU'
        },
        color: 'emerald'
      }
    },
    headline: {
      fi: 'Petollinen musta jää liukastuttaa Oulun katuja – OSL:n bussit myöhässä, pyöräilyn Baana harjasuolattu',
      en: 'Treacherous black ice covers Oulu roads – OSL buses running behind, Baana cycling superhighway swept bare',
      selko: 'Teillä on vaarallista mustaa jäätä Oulussa – Bussit ovat myöhässä, mutta Baana-pyörätie on puhdas',
      sami: 'Váralaš jiekŋa luoddain Oulus – Bussat leat maŋŋonan, muhto Baana-sihkkelgeaidnu lea buhtis'
    },
    bullet1: {
      fi: 'Kosteuden jäätyminen yöpakkasilla on luonut peilijäätä ajoradoille ja risteysalueille. OSL-bussit ajavat varovaisuusnopeuksilla aiheuttaen 10–15 min viiveitä.',
      en: 'Subzero drop froze street moisture into clear ice. OSL city buses operate at reduced cautious speed, causing 15 min delays.',
      selko: 'Tiet ovat jäässä ja liukkaita. OSL-bussit ajavat varovasti, joten ne tulevat pysäkeille myöhässä.',
      sami: 'Luottat leat jikŋon. OSL-bussat vudjet várrogasat ja leat maŋŋonan 15 minuhta.'
    },
    bullet2: {
      fi: 'Kaupungin ykköshoitoluokan Baana Linnanmaan yliopistolta keskustaan on harjasuolattu ja täysin sula. Nastakengät ja pyörän talvirenkaat suositeltavia.',
      en: 'Priority Baana express corridor from Linnanmaa campus to downtown is swept clean. Studded winter footwear strongly advised.',
      selko: 'Yliopistolle vievä Baana pyörätie on harjattu ja hiekoitettu. Muista laittaa kengät, jotka eivät luista.',
      sami: 'Baana sihkkelgeaidnu universitehtii lea buhtis. Ane dálveskuovaid maiguin ii njuola.'
    },
    keywords: ['musta-jää', 'baana', 'osl-bussit'],
    solution: {
      badge: {
        fi: 'LIIKENNEOPAS',
        en: 'COMMUTE ADVICE',
        selko: 'LIIKKUMISVINKKI',
        sami: 'JOHTOLATVÁVVA'
      },
      text: {
        fi: 'Tarkista bussisi reaaliaikainen GPS OSL-reittioppaasta ennen ulosmenoa. Pyöräillessä käytä aina suolattua Baanaa.',
        en: 'Monitor real-time bus GPS via OSL Route Planner before heading outside. Use the salted Baana for cycling.',
        selko: 'Katso OSL-sovelluksesta, missä bussi menee, jotta et joudu seisomaan pakkasessa.',
        sami: 'Geahča OSL-kárttas gos bussi lea, ammet galmmo šiljus.'
      },
      actionLabel: {
        fi: 'Avaa OSL Live GPS & Baana-tilanne',
        en: 'Open Live Bus Tracker & Baana Status',
        selko: 'Avaa bussikartta ja aikataulut',
        sami: 'Raba bussa reálasaji kártta'
      },
      actionType: 'MAP'
    },
    traditionalDepth: {
      leadParagraph: {
        fi: 'Talven ensimmäiset todelliset pääkallokelit ovat saapuneet Oulun seudulle. Lämpötilan sahatessa nollan molemmin puolin teiden pinnoille on muodostunut petollisen liukasta mustaa jäätä, joka haastaa aamuliikenteen sujuvuutta.',
        en: 'Winter black ice conditions have descended upon the Oulu metropolitan area. Rapid thermal swings around zero degrees caused invisible glaze ice across road intersections.',
        selko: 'Talven liukkaat kelit ovat alkaneet Oulussa. Asfaltti on jäätynyt vaarallisen liukkaaksi ja autot sekä bussit joutuvat ajamaan hiljaa.',
        sami: 'Dálvvi vuosttaš njuolggus dálkkát leat boahtán Oului. Luottat leat jikŋon ja johtolat manná njozet.'
      },
      bodyText: {
        fi: 'Oulun seudun liikenne (OSL) ilmoittaa runkolinjojen 1, 2, 3 ja 5 kärsivän 10–20 minuutin viiveistä aamun ja iltapäivän tunteina. Bussinkuljettajia on ohjeistettu noudattamaan korostettua varovaisuutta matkustajien turvallisuuden takaamiseksi.\n\nSamaan aikaan Oulun kaupungin katuosasto muistuttaa maailmankuulusta pyöräteiden talvihoidostaan: Linnanmaan ja keskustan välinen Baana harjataan ja käsitellään nestemäisellä suolaliuoksella aamuvarhaisella, joten se tarjoaa tänäänkin auton ja bussin voittavan nopean ja turvallisen työmatkareitin.',
        en: 'OSL Transit reports arterial routes 1, 2, 3, and 5 operating with 10–20 minute delays. Bus operators were instructed to prioritize safety margins over rigid timetable adherence.\n\nMeanwhile, Oulu Municipal Works Department highlights its flagship cycling infrastructure: the Baana thoroughfare between Linnanmaa university and the city center was sweep-salted at 05:00, remaining bare black asphalt.',
        selko: 'OSL-bussit ovat vähän myöhässä, koska kuskit ajavat varovasti liukkaalla säällä. Pyörätiet on kuitenkin harjattu puhtaiksi, joten pyöräily on tänään nopea ja hyvä tapa liikkua kaupungissa.',
        sami: 'OSL-bussat leat veháš maŋŋonan livkka dálkki dihte. Sihkkelgeaidnu lea dattetge buhtistuvvon ja sihkkelastin lea johtilis vuohki mátkkoštit.'
      },
      reporterName: 'Jukka Harju, Kalevan liikennetoimitus',
      section: 'Oulu & Talvi'
    }
  },

  // 5. REAL CULTURAL/CITY EVENT: Kivisydän "Kuuttaren puutarha" (24.10.2026)
  {
    id: 'story-5-kivisydan-kuutar',
    category: 'CAMPUS',
    categoryLabel: {
      fi: 'KAUPUNKIKULTTUURI',
      en: 'CITY CULTURE',
      selko: 'KULTTUURI',
      sami: 'KULTUVRA'
    },
    district: 'Maan alla • Kivisydän & Rotuaari',
    timeAgo: 'Päivitetty 3 tuntia sitten',
    jsnStatus: 'JSN § 10 Tarkistettu',
    credibilityScore: 100,
    diagram: {
      problem: {
        icon: '🥶🌧️🏙️',
        image: 'https://images.unsplash.com/photo-1516715094483-75da7dee9758?auto=format&fit=crop&w=800&q=80',
        caption: 'Pakkastuuli ja pimeys ulkona',
        title: {
          fi: 'Pakkasviimaa ulkona',
          en: 'Cold & Gloomy Outside',
          selko: 'Ulkona on kylmää ja tuulee',
          sami: 'Galmmas ja biekka olgun'
        },
        detail: {
          fi: 'Viima ja pimeys koettelevat keskustassa.',
          en: 'Subzero winds and darkness in the streets.',
          selko: 'Ulkona tuulee ja on kylmä.',
          sami: 'Olgun lea buolaš ja seavdnjat.'
        },
        badge: {
          fi: 'TALVIARKI',
          en: 'WINTER CHILL',
          selko: 'TALVI',
          sami: 'DÁLVI'
        },
        color: 'red'
      },
      arrowLabel: {
        fi: 'ASTU MAAN ALLE LÄMPÖÖN ⬇️',
        en: 'STEP UNDERGROUND INTO WARMTH ⬇️',
        selko: 'MENE ALAS LÄMPIMÄÄN ⬇️',
        sami: 'MANA VUOLOS LIEGGA SADJÁI ⬇️'
      },
      solution: {
        icon: '🏛️🌸✨',
        image: 'https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w=800&q=80',
        caption: 'Kivisydän +16°C • Kuuttaren puutarha',
        title: {
          fi: 'Koe Kuuttaren puutarha',
          en: 'Visit Kuutar’s Garden',
          selko: 'Koe Kuuttaren puutarha maan alla',
          sami: 'Oza Kuuttara bákterokkis'
        },
        detail: {
          fi: 'Lämmin taidepuutarha (+16°C). Hissi Rotuaarilta.',
          en: 'Warm 3D art cavern (+16°C). Lift from Rotuaari.',
          selko: 'Lämmin taidenäyttely maan alla. Hissi suoraan Rotuaarilta.',
          sami: 'Liegga dáiddačájáhus bákterokkis. Hissi Rotuaaris.'
        },
        badge: {
          fi: 'UUTUUS OULUSSA',
          en: 'NEW IN OULU',
          selko: 'UUTUUS',
          sami: 'OĐAS OULUS'
        },
        color: 'emerald'
      }
    },
    headline: {
      fi: 'Maanalainen Kivisydän muuttuu satumaiseksi puutarhaksi – Kansainvälinen huipputaideteos avautuu Oulun alle',
      en: 'Subterranean Kivisydän transforms into mythical garden – International art masterpiece opens beneath Oulu',
      selko: 'Kivisydämen kallioluolaan aukeaa upea taidenäyttely – Pääset lämpimään suoraan Rotuaarin hissillä',
      sami: 'Kivisydän-bákteroggái rahpasa čáppa dáiddačájáhus – Beasat liegga sadjái hissiin njuolgga Rotuaaris'
    },
    bullet1: {
      fi: 'Tanskalaisen Jakob Kudsk Steensenin immersiivinen "Kuuttaren puutarha" tuo pohjoisen luonnon ja digitaalisen 3D-maailman Kivisydän-kallioluolaan.',
      en: 'Danish artist Jakob Kudsk Steensen’s immersive "Kuutar’s Garden" melds Nordic nature with 3D animation inside Kivisydän cavern.',
      selko: 'Kansainvälinen taiteilija tuo upean valo- ja ääninäyttelyn Oulun maanalaiseen Kivisydämeen.',
      sami: 'Dánskalaš dáiddár buktá čáppa čuovga- ja jietnačájáhusa Kivisydän-bákteroggái.'
    },
    bullet2: {
      fi: 'Näyttelyyn on esteetön kulku lasihisseillä suoraan Rotuaari kävelykadulta ja Valkeasta. Luolassa on ympäri vuoden mukava +16°C lämpötila.',
      en: 'Direct barrier-free glass elevator access from Rotuaari high-street and Valkea mall. Cavern stays a comfortable +16°C.',
      selko: 'Pääset näyttelyyn helposti hissillä Rotuaarilta tai Valkeasta. Sisällä on aina mukavan lämmintä ilman takkia.',
      sami: 'Beasat čájáhussii hissiin Rotuaaris dahje Valkeas. Doppe lea liekkas almmá dálvetáhki haga.'
    },
    keywords: ['kivisydan', 'rotuaari', 'baana'],
    solution: {
      badge: {
        fi: 'KULTTUURITÄRPPI',
        en: 'CULTURE PICK',
        selko: 'MENOVINKKI',
        sami: 'KULTURAVÁVVA'
      },
      text: {
        fi: 'Astu Rotuaarin lasihissiin ja laskeudu suoraan maanalaiseen näyttelyyn. Lämmin ja elämyksellinen pakopaikka talvipakkasilta.',
        en: 'Step into the Rotuaari glass elevator directly down into the exhibition. A warm escape from winter chill.',
        selko: 'Mene Rotuaarin hissiin ja tule katsomaan upeaa näyttelyä. Sisäänpääsy on helppo kaikille.',
        sami: 'Váldde hissa Rotuaaris ja boađe geahččat čájáhusa liegga bákterokkis.'
      },
      actionLabel: {
        fi: 'Näytä Kivisydämen hissireitti & tiedot',
        en: 'Show Kivisydän Lift Access & Hours',
        selko: 'Katso aukioloajat ja hissireitti',
        sami: 'Čájet hissa geainnu ja rabasáiggiid'
      },
      actionType: 'GUIDE'
    },
    traditionalDepth: {
      leadParagraph: {
        fi: 'Oulun ydinkeskustan alapuolella sykkivä maanalainen kalliopysäköintilaitos Kivisydän saa poikkeuksellisen kulttuurisen kruunun, kun tanskalaistaustaisen huipputaiteilijan Jakob Kudsk Steensenin luoma suurteos "Kuuttaren puutarha" avataan yleisölle.',
        en: 'The subterranean granite chamber beneath downtown Oulu receives an extraordinary cultural elevation as world-renowned Danish artist Jakob Kudsk Steensen opens "Kuutar’s Garden" to the public.',
        selko: 'Oulun keskustan alle Kivisydämeen avataan suuri ja upea taideteos. Näyttelyssä yhdistyvät pohjoinen luonto, valot ja äänet.',
        sami: 'Oulu guovddáža vuolde Kivisydän-bákterokkis rahpasa stuorra ja erenoamáš dáiddačájáhus mas leat čuovggat ja jienat.'
      },
      bodyText: {
        fi: 'Teos yhdistää pohjoisen suoluonnon ikiaikaisen biologian, kalevalaisen Kuutar-mytologian ja huipputason digitaalisen 3D-animaation. Teos levittäytyy Kivisydämen massiivisille kallioseinille ja äänimaisemaan luoden maagisen elämyksen keskelle tavallista arkiympäristöä.\n\nKivisydämen etuna on sen poikkeuksellinen helppopääsyisyys: Oulun keskustan vilinässä asioivat voivat astua Rotuaarin tai kauppakeskus Valkean lasihissiin ja laskeutua suoraan lämpimään (+16 astetta) luolamiljööseen ilman talvitakkeja ja pakkasviimaa. Teos on osa Oulu2026-Euroopan kulttuuripääkaupunkivuoteen valmistautuvaa ohjelmistoa.',
        en: 'The artwork combines archaic mire wetland biology, ancient Kuutar mythology, and photorealistic 3D visual effects. Animations cascade across raw granite walls alongside a bespoke spatial acoustic score.\n\nA key asset is accessibility: pedestrians in Rotuaari or Valkea mall can take glass elevators directly into the temperate (+16°C) underground cavern without coats. The project serves as a cornerstone installation leading towards Oulu2026 European Capital of Culture.',
        selko: 'Kivisydämeen pääsee suoraan Rotuaarin tai Valkean kauppakeskuksen hisseillä. Siellä on aina tasainen +16 asteen lämpötila, joten talvella siellä on mukava viettää aikaa. Tämä on osa Oulu2026-kulttuuriohjelmaa.',
        sami: 'Čájáhussii beasat hissiin njuolgga Rotuaaris ja Valkeas. Doppe lea liekkas (+16°C). Dáiddadahkos lea oassi Oulu2026-kulturođđasis.'
      },
      reporterName: 'Heidi Hietala, Kalevan kulttuuritoimitus',
      section: 'Kulttuuri & Oulu2026'
    }
  }
];
