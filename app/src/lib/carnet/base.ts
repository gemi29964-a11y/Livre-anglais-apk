// Mon carnet (8.8) : base locale Dexie (IndexedDB), stockage privé de l'application (10.10).
import Dexie, { type EntityTable } from 'dexie';

export interface MarquePage { id: string; genre: 'expression' | 'declinaison' | 'replique'; scene: string; date: number; note?: string }
export interface Enregistrement { id?: number; enonce: string; date: number; duree: number; voix: Blob; auto?: 'tres-proche' | 'presque' | 'a-retravailler' }
export interface Version { id?: number; expression: string; texte: string; date: number; voix?: Blob }
export interface JourDePratique { jour: string; scenes: number; retrouvailles: number; minutes: number }
export interface Lecture { cle: 'reprise'; scene: string; moment: string; expression: string; date: number }
export interface SceneParcourue { scene: string; date: number }

export class BaseCarnet extends Dexie {
  marquePages!: EntityTable<MarquePage, 'id'>;
  maVoix!: EntityTable<Enregistrement, 'id'>;
  versions!: EntityTable<Version, 'id'>;
  pratique!: EntityTable<JourDePratique, 'jour'>;
  lecture!: EntityTable<Lecture, 'cle'>;
  parcourues!: EntityTable<SceneParcourue, 'scene'>;

  constructor(nom = 'carnet') {
    super(nom);
    this.version(1).stores({
      marquePages: 'id, scene, date',
      maVoix: '++id, enonce, date',
      versions: '++id, expression, date',
      pratique: 'jour',
      lecture: 'cle',
      parcourues: 'scene, date'
    });
  }
}

export const carnet = new BaseCarnet();

/** Journée de pratique : elle bascule à 4 h du matin, heure locale (8.6). */
export function jourDePratique(d: Date = new Date()): string {
  const decale = new Date(d.getTime() - 4 * 3600_000);
  const a = decale.getFullYear(), m = String(decale.getMonth() + 1).padStart(2, '0'), j = String(decale.getDate()).padStart(2, '0');
  return `${a}-${m}-${j}`;
}

/**
 * Constance (8.8) : jours de pratique consécutifs jusqu'à aujourd'hui, avec un jour de grâce
 * par semaine glissante (aucune pénalité, aucun jour perdu pour un oubli isolé).
 */
export function constance(jours: Iterable<string>, aujourdhui: string = jourDePratique()): number {
  const ensemble = new Set(jours);
  const precedent = (j: string) => {
    const [a, m, d] = j.split('-').map(Number);
    const x = new Date(Date.UTC(a, m - 1, d - 1));
    return x.toISOString().slice(0, 10);
  };
  let j = ensemble.has(aujourdhui) ? aujourdhui : precedent(aujourdhui);
  let n = 0, graces: number[] = [];
  for (let pas = 0; pas < 3660; pas++) {
    if (ensemble.has(j)) { n++; j = precedent(j); continue; }
    graces = graces.filter((g) => pas - g < 7);
    if (graces.length === 0 && n > 0) { graces.push(pas); j = precedent(j); continue; }
    break;
  }
  return n;
}
