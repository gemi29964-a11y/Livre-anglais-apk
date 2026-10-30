// Une page par itinéraire déclaré dans corpus/itineraires.yaml (compilé en itineraires.json).
import type { EntryGenerator } from './$types';

// « auto » : tant qu'aucune entrée n'existe (scènes non encore écrites), la page reste servie par le repli index.html.
export const prerender = 'auto';
import itineraires from '../../../../static/corpus/itineraires.json';

export const entries: EntryGenerator = () => (itineraires as { id: string }[]).map((i) => ({ id: i.id }));

export function load({ params }) {
  return { id: params.id };
}
