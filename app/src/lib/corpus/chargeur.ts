// Chargement du corpus compilé (10.6) : sommaire au démarrage, une scène à son ouverture.
import type { Scene } from './types';

export interface SceneSommaire {
  id: string; numero: string; titre: string; disponible: boolean; intention: string | null; expressions: number;
}
export interface ChapitreSommaire { id: string; numero: number; titre: string; tailleVoix: number; scenes: SceneSommaire[] }
export interface Sommaire { chapitres: ChapitreSommaire[] }

let sommaire: Promise<Sommaire> | null = null;
const scenes = new Map<string, Promise<Scene | null>>();

type Recuperer = (url: string) => Promise<Response>;

export function chargerSommaire(recuperer: Recuperer = fetch): Promise<Sommaire> {
  sommaire ??= recuperer('/corpus/sommaire.json').then((r) => {
    if (!r.ok) throw new Error(`sommaire ${r.status}`);
    return r.json() as Promise<Sommaire>;
  }).catch((e) => { sommaire = null; throw e; });
  return sommaire;
}

export function chargerScene(id: string, recuperer: Recuperer = fetch): Promise<Scene | null> {
  if (!/^c\d{2}\.s\d{2}$/.test(id)) return Promise.resolve(null);
  if (!scenes.has(id)) {
    scenes.set(id, recuperer(`/corpus/${id}.json`).then((r) => (r.ok ? (r.json() as Promise<Scene>) : null)).catch(() => {
      scenes.delete(id);
      return null;
    }));
  }
  return scenes.get(id)!;
}

export function chapitreDe(s: Sommaire, id: string): ChapitreSommaire | undefined {
  return s.chapitres.find((c) => c.id === id);
}

export function sceneDe(s: Sommaire, id: string): { chapitre: ChapitreSommaire; scene: SceneSommaire } | undefined {
  for (const chapitre of s.chapitres) {
    const scene = chapitre.scenes.find((x) => x.id === id);
    if (scene) return { chapitre, scene };
  }
  return undefined;
}

/** Retire le balisage <en>…</en> et renvoie les fragments, pour un rendu lang="en" (3.4, règle 6). */
export function fragments(texte: string): { en: boolean; texte: string }[] {
  const sortie: { en: boolean; texte: string }[] = [];
  const motif = /<en>(.*?)<\/en>/gs;
  let i = 0;
  for (const m of texte.matchAll(motif)) {
    if (m.index! > i) sortie.push({ en: false, texte: texte.slice(i, m.index) });
    sortie.push({ en: true, texte: m[1] });
    i = m.index! + m[0].length;
  }
  if (i < texte.length) sortie.push({ en: false, texte: texte.slice(i) });
  return sortie;
}

export function oublierCache(): void { sommaire = null; scenes.clear(); }
