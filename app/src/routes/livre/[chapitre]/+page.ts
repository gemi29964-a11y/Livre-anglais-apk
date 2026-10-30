// Les 27 pages de chapitre (Prélude et chapitres 1 à 26) sont produites à la construction.
import type { EntryGenerator } from './$types';

export const entries: EntryGenerator = () =>
  Array.from({ length: 27 }, (_, n) => ({ chapitre: `c${String(n).padStart(2, '0')}` }));

export function load({ params }) {
  return { chapitre: params.chapitre };
}
