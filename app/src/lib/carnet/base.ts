// Mon carnet (8.8) : base locale Dexie « vivre » (IndexedDB), stockage privé de l'application (10.10).
// Tables prescrites : progression, cartes, journal, marques, notes, constance, versions, itineraires, contretemps.
// Les enregistrements « Ma voix » vont dans Directory.Data/ma_voix/ (fichiers .m4a), pas dans la base.
import Dexie, { type EntityTable } from 'dexie';

/** Progression d'une scène ; la ligne de clé « reprise » garde la position exacte de lecture. */
export interface Progression { scene: string; etat: 'en-cours' | 'parcourue'; moment: string; expression: string; date: number; ouverte?: string }
/** État de mémorisation d'une expression (FSRS, 8.6). */
export interface Carte { expression: string; due: number; stabilite: number; difficulte: number; etat: number; repetitions: number; oublis: number; derniere?: number; familiere: boolean }
/** Journal des retrouvailles (une ligne par réponse). */
export interface EntreeJournal { id?: number; expression: string; date: number; forme: string; note: 1 | 2 | 3 | 4 }
export interface Marque { id: string; genre: 'expression' | 'declinaison' | 'replique'; scene: string; date: number }
export interface Note { id: string; texte: string; date: number }
export interface JourDeConstance { jour: string; scenes: number; retrouvailles: number; minutes: number }
export interface Version { id?: number; expression: string; texte: string; date: number; fichier?: string }
export interface ItineraireSuivi { id: string; etape: number; debut: number }
export interface Contretemps { id?: number; date: number; code: string; ecran: string }

export const REPRISE = 'reprise';

export class BaseCarnet extends Dexie {
  progression!: EntityTable<Progression, 'scene'>;
  cartes!: EntityTable<Carte, 'expression'>;
  journal!: EntityTable<EntreeJournal, 'id'>;
  marques!: EntityTable<Marque, 'id'>;
  notes!: EntityTable<Note, 'id'>;
  constance!: EntityTable<JourDeConstance, 'jour'>;
  versions!: EntityTable<Version, 'id'>;
  itineraires!: EntityTable<ItineraireSuivi, 'id'>;
  contretemps!: EntityTable<Contretemps, 'id'>;

  constructor(nom = 'vivre') {
    super(nom);
    this.version(1).stores({
      progression: 'scene, etat, date',
      cartes: 'expression, due, familiere',
      journal: '++id, expression, date',
      marques: 'id, scene, date',
      notes: 'id, date',
      constance: 'jour',
      versions: '++id, expression, date',
      itineraires: 'id',
      contretemps: '++id, date'
    });
  }

  /** Scènes parcourues (8.3). */
  async parcourues(): Promise<Set<string>> {
    const l = await this.progression.where('etat').equals('parcourue').toArray();
    return new Set(l.map((p) => p.scene));
  }

  /** Position de reprise (8.2) : dernière scène ouverte. */
  async reprise(): Promise<Progression | undefined> {
    return this.progression.get(REPRISE);
  }

  async noterReprise(ouverte: string, moment: string, expression: string): Promise<void> {
    const date = Date.now();
    await this.progression.put({ scene: REPRISE, etat: 'en-cours', ouverte, moment, expression, date });
    const actuelle = await this.progression.get(ouverte);
    if (actuelle?.etat !== 'parcourue') await this.progression.put({ scene: ouverte, etat: 'en-cours', moment, expression, date });
  }

  /** Journal des contretemps : 200 entrées au plus, les plus anciennes s'effacent (10.10). */
  async contretempsSurvenu(code: string, ecran: string): Promise<void> {
    await this.contretemps.add({ date: Date.now(), code, ecran });
    const n = await this.contretemps.count();
    if (n > 200) {
      const anciens = await this.contretemps.orderBy('date').limit(n - 200).primaryKeys();
      await this.contretemps.bulkDelete(anciens);
    }
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
