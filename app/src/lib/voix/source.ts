// app/src/lib/voix/source.ts
import { Capacitor, registerPlugin } from '@capacitor/core';
import type { Accent, Rythme } from '$lib/corpus/types';

export interface EtatChapitre { etat: 'socle' | 'installe' | 'absent' | 'en_cours'; base?: string; taille: number }
interface VoixPlugin {
  etat(o: { chapitre: string }): Promise<EtatChapitre>;
  faireVenir(o: { chapitre: string }): Promise<void>;
  retirer(o: { chapitre: string }): Promise<void>;
  addListener(e: 'progression', f: (p: { chapitre: string; octets: number; total: number; etat: string }) => void): Promise<{ remove: () => void }>;
}
export const Voix = registerPlugin<VoixPlugin>('Voix');

const SOCLE = new Set(['c00', 'c01', 'c02']);   // Prélude, Chapitres 1 et 2 : dans le module de base
const bases = new Map<string, string | null>();

export function nomFichier(id: string, accent: Accent, rythme: Rythme): string {
  // "c01.s01.A1.e1" → "c01s01-A1-e1.uk.pose.opus"
  const [c, s, ...reste] = id.split('.');
  return `${c}${s}-${reste.join('-')}.${accent}.${rythme}.opus`;
}

export async function urlVoix(id: string, accent: Accent, rythme: Rythme): Promise<string | null> {
  const [c, s] = id.split('.');
  const chemin = `voix/${c}/${s}/${nomFichier(id, accent, rythme)}`;
  if (SOCLE.has(c)) return `/${chemin}`;
  if (!bases.has(c)) {
    const e = await Voix.etat({ chapitre: c });
    bases.set(c, e.etat === 'installe' && e.base ? e.base : null);
  }
  const base = bases.get(c);
  return base ? Capacitor.convertFileSrc(`${base}/${chemin}`) : null;
}
export async function urlSens(id: string): Promise<string | null> {
  // "c01.s01.A1" → "voix/c01/s01/c01s01-A1.fr.sens.opus" (même emplacement que les voix anglaises)
  const [c, s, ...reste] = id.split('.');
  const chemin = `voix/${c}/${s}/${c}${s}-${reste.join('-')}.fr.sens.opus`;
  if (SOCLE.has(c)) return `/${chemin}`;
  const base = bases.get(c) ?? (await Voix.etat({ chapitre: c })).base ?? null;
  return base ? Capacitor.convertFileSrc(`${base}/${chemin}`) : null;
}
export function oublierBase(chapitre: string) { bases.delete(chapitre); }
