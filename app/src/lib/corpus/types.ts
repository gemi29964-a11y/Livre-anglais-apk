// app/src/lib/corpus/types.ts
export type Accent = 'us' | 'uk';
export type Rythme = 'pose' | 'spontane';
export type Ton = 'courant' | 'complice' | 'cru' | 'soutenu';
export type Niveau = 'fondations' | 'aisance' | 'maitrise';
export type Region = 'commun' | 'us' | 'uk' | 'au' | 'ie' | 'ng' | 'gh' | 'za';

export interface Phrase {
  phrase: string;        // système du Phrasé (section 6), ex. "maï ə·LÂMZ gəou·ing OF ↘"
  expert: string;        // alphabet phonétique international, ex. "/maɪ əˈlɑːmz ˌɡəʊɪŋ ˈɒf/"
  entendu?: string;      // ce que l'oreille entend (spontané), ex. "Whatcha doin'?"
}

export type Phrases = Record<Accent, Record<Rythme, Phrase>>;

export interface Enonce {
  id: string;                          // "c01.s01.A1.e1"
  texte: Record<Accent, string>;       // graphies par accent (identiques si commun)
  region: Region;                      // 'uk' → texte.us contient l'équivalent américain
  phrases: Phrases;
  jeu: { contexte: string; emotion: string };   // indication de jeu (en anglais, transmise au moteur des voix)
}

export interface Declinaison {
  id: string;                          // "c01.s01.A1.d1"
  texte: Record<Accent, string>;
  sens: string;
  phrases: Phrases;                    // obligatoires (6.7)
  renvoi?: string;
}

export interface Expression {
  id: string;                          // "c01.s01.A1"
  enonces: Enonce[];                   // 1 à 3
  sens: string;
  motAMot?: string;
  usage: string;
  coulisses?: string;
  gabarit?: string;                    // "[quelque chose] is going off"
  declinaisons: Declinaison[];         // 3 à 6
  ton: Ton;
  niveau: Niveau;
  frequence: 1 | 2 | 3 | 4 | 5;
  situations: string[];
  fonctions: string[];
  renvois: string[];
}

export interface Moment { lettre: string; titre: string; expressions: Expression[] }

export interface Replique {
  id: string;                          // "c01.s01.sv.l01"
  personnage: string;                  // clé de personnages.yaml
  texte: Record<Accent, string>;
  sens: string;
  emotion: string;
}

export interface Itineraire {
  id: string;                          // "premier-voyage"
  titre: string;
  pourQui: string;
  etapes: { titre: string; expressions: string[] }[];   // ids d'expressions
}

export interface FauxPas { fautif: string; naturel: string; pourquoi: string }

export interface Scene {
  id: string;                          // "c01.s01"
  chapitre: number;
  numero: number;
  titre: string;
  intention: string;
  moments: Moment[];
  essentiel: { incontournables: string[]; fauxPas: FauxPas[] };  // ids d'expressions
  sceneVivante: { titre: string; repliques: Replique[] };
  rituel: string[];
  version: number;
}
