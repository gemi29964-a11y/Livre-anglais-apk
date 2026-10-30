// Les Préférences du lecteur (8.10) : modèle, valeurs par défaut, bornes et lecture tolérante.
import type { Accent, Niveau, Rythme } from '$lib/corpus/types';

export type Theme = 'papier' | 'ambre' | 'nuit' | 'contraste' | 'automatique';
export type Silences = 'court' | 'normal' | 'long';
export type Forme = 'oreille' | 'replique' | 'miroir' | 'deux-anglais' | 'ton-juste' | 'faux-pas' | 'meme-air' | 'oreille-fine';

export interface Preferences {
  accueilFait: boolean;
  accent: Accent;
  rythme: Rythme;
  ordreQuatre: 'prefere' | 'alterne';
  voixDuSens: boolean;
  silences: Silences;
  passagesEcho: number;            // 2 à 5
  tailleCran: number;              // 0 à 6 → 16 à 26 px
  interligneCran: number;          // 0 à 2
  theme: Theme;
  aideLecture: boolean;
  expertParDefaut: boolean;
  courbe: boolean;
  tonCru: boolean;
  battement: boolean;
  haptique: boolean;
  niveau: Niveau;
  nouvellesParJour: number;        // 5 à 50
  retrouvaillesMax: number;        // 20 à 400
  retention: number;               // 80 à 95
  formesEcartees: Forme[];
  silencieuses: boolean;
  momentPresent: boolean;
  rendezVous: { actif: boolean; heure: number; minute: number; jours: number[] };
  ecranAccueil: { accent: Accent; rythme: Rythme; origine: 'parcourues' | 'ouvrage' };
}

export const TAILLES = [16, 17, 18, 20, 22, 24, 26];
export const INTERLIGNES = [1.45, 1.6, 1.75];

export const DEFAUT: Preferences = {
  accueilFait: false,
  accent: 'uk',
  rythme: 'pose',
  ordreQuatre: 'prefere',
  voixDuSens: true,
  silences: 'normal',
  passagesEcho: 3,
  tailleCran: 2,
  interligneCran: 1,
  theme: 'automatique',
  aideLecture: false,
  expertParDefaut: false,
  courbe: false,
  tonCru: true,
  battement: false,
  haptique: true,
  niveau: 'fondations',
  nouvellesParJour: 20,
  retrouvaillesMax: 120,
  retention: 90,
  formesEcartees: [],
  silencieuses: false,
  momentPresent: true,
  rendezVous: { actif: false, heure: 7, minute: 30, jours: [0, 1, 2, 3, 4, 5, 6] },
  ecranAccueil: { accent: 'uk', rythme: 'pose', origine: 'parcourues' }
};

const borne = (v: unknown, min: number, max: number, d: number) =>
  typeof v === 'number' && Number.isFinite(v) ? Math.min(max, Math.max(min, Math.round(v))) : d;
const parmi = <T extends string>(v: unknown, liste: readonly T[], d: T): T =>
  (liste as readonly unknown[]).includes(v) ? (v as T) : d;
const oui = (v: unknown, d: boolean) => (typeof v === 'boolean' ? v : d);

/** Relit des préférences enregistrées en écartant toute valeur hors bornes (sauvegarde ancienne ou abîmée). */
export function lire(brut: unknown): Preferences {
  const o = (brut && typeof brut === 'object' ? brut : {}) as Record<string, unknown>;
  const rv = (o.rendezVous ?? {}) as Record<string, unknown>;
  const ea = (o.ecranAccueil ?? {}) as Record<string, unknown>;
  const formes: Forme[] = ['oreille', 'replique', 'miroir', 'deux-anglais', 'ton-juste', 'faux-pas', 'meme-air', 'oreille-fine'];
  return {
    accueilFait: oui(o.accueilFait, DEFAUT.accueilFait),
    accent: parmi(o.accent, ['uk', 'us'] as const, DEFAUT.accent),
    rythme: parmi(o.rythme, ['pose', 'spontane'] as const, DEFAUT.rythme),
    ordreQuatre: parmi(o.ordreQuatre, ['prefere', 'alterne'] as const, DEFAUT.ordreQuatre),
    voixDuSens: oui(o.voixDuSens, DEFAUT.voixDuSens),
    silences: parmi(o.silences, ['court', 'normal', 'long'] as const, DEFAUT.silences),
    passagesEcho: borne(o.passagesEcho, 2, 5, DEFAUT.passagesEcho),
    tailleCran: borne(o.tailleCran, 0, TAILLES.length - 1, DEFAUT.tailleCran),
    interligneCran: borne(o.interligneCran, 0, INTERLIGNES.length - 1, DEFAUT.interligneCran),
    theme: parmi(o.theme, ['papier', 'ambre', 'nuit', 'contraste', 'automatique'] as const, DEFAUT.theme),
    aideLecture: oui(o.aideLecture, DEFAUT.aideLecture),
    expertParDefaut: oui(o.expertParDefaut, DEFAUT.expertParDefaut),
    courbe: oui(o.courbe, DEFAUT.courbe),
    tonCru: oui(o.tonCru, DEFAUT.tonCru),
    battement: oui(o.battement, DEFAUT.battement),
    haptique: oui(o.haptique, DEFAUT.haptique),
    niveau: parmi(o.niveau, ['fondations', 'aisance', 'maitrise'] as const, DEFAUT.niveau),
    nouvellesParJour: borne(o.nouvellesParJour, 5, 50, DEFAUT.nouvellesParJour),
    retrouvaillesMax: borne(o.retrouvaillesMax, 20, 400, DEFAUT.retrouvaillesMax),
    retention: borne(o.retention, 80, 95, DEFAUT.retention),
    formesEcartees: Array.isArray(o.formesEcartees) ? (o.formesEcartees.filter((f) => formes.includes(f as Forme)) as Forme[]) : [],
    silencieuses: oui(o.silencieuses, DEFAUT.silencieuses),
    momentPresent: oui(o.momentPresent, DEFAUT.momentPresent),
    rendezVous: {
      actif: oui(rv.actif, DEFAUT.rendezVous.actif),
      heure: borne(rv.heure, 0, 23, DEFAUT.rendezVous.heure),
      minute: borne(rv.minute, 0, 59, DEFAUT.rendezVous.minute),
      jours: Array.isArray(rv.jours) ? rv.jours.filter((j) => Number.isInteger(j) && j >= 0 && j <= 6) as number[] : DEFAUT.rendezVous.jours
    },
    ecranAccueil: {
      accent: parmi(ea.accent, ['uk', 'us'] as const, DEFAUT.ecranAccueil.accent),
      rythme: parmi(ea.rythme, ['pose', 'spontane'] as const, DEFAUT.ecranAccueil.rythme),
      origine: parmi(ea.origine, ['parcourues', 'ouvrage'] as const, DEFAUT.ecranAccueil.origine)
    }
  };
}

/** Réglages déduits de la réponse « Où en êtes-vous en anglais ? » (8.11, écran 3). */
export function selonNiveau(p: Preferences, niveau: Niveau): Preferences {
  return {
    ...p,
    niveau,
    rythme: niveau === 'maitrise' ? 'spontane' : 'pose',
    voixDuSens: niveau !== 'maitrise',
    courbe: niveau !== 'fondations'
  };
}

/** « L'usage » ouvert par défaut au niveau Fondations, replié aux niveaux supérieurs (8.2). */
export const usageOuvert = (p: Preferences) => p.niveau === 'fondations';
