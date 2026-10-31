// Adresses de l'ouvrage (10.20) : vivrelanglais://… et https://vivrelanglais.com/e/{id}.
// Toute adresse inconnue ou tout identifiant absent du sommaire ouvre Aujourd'hui, sans message d'erreur.
import type { Sommaire } from '$lib/corpus/chargeur';

const EXPRESSION = /^c\d{2}\.s\d{2}\.[A-Z]\d{1,2}$/;
const SCENE = /^c\d{2}\.s\d{2}$/;

const sceneExiste = (s: Sommaire, id: string) => s.chapitres.some((c) => c.scenes.some((x) => x.id === id && x.disponible));

/** Traduit une adresse externe en chemin interne de l'application. */
export function chemin(adresse: string, sommaire: Sommaire): string {
  let u: URL;
  try {
    u = new URL(adresse);
  } catch {
    return '/';
  }
  let morceaux: string[];
  if (u.protocol === 'vivrelanglais:') morceaux = [u.hostname, ...u.pathname.split('/').filter(Boolean)];
  else if (u.protocol === 'https:' && u.hostname === 'vivrelanglais.com' && u.pathname.startsWith('/e/')) morceaux = ['expression', u.pathname.slice(3).replace(/\/$/, '')];
  else return '/';
  const [genre, id = ''] = morceaux;
  const ecouter = u.searchParams.get('ecouter') === '1';
  switch (genre) {
    case 'expression': {
      const scene = id.split('.').slice(0, 2).join('.');
      if (!EXPRESSION.test(id) || !sceneExiste(sommaire, scene)) return '/';
      return `/scene/${scene}/${ecouter ? '?ecouter=1' : ''}#${id}`;
    }
    case 'scene':
      return SCENE.test(id) && sceneExiste(sommaire, id) ? `/scene/${id}/` : '/';
    case 'retrouvailles':
      return '/?retrouvailles=1';
    case 'promenade':
      return '/promenade/?programme=reprendre';
    case 'reprendre':
      return '/?reprendre=1';
    case 'recherche':
      return '/recherche/';
    default:
      return '/';
  }
}

/** Branche l'écoute des adresses au démarrage (App.getLaunchUrl) et pendant la lecture (appUrlOpen). */
export async function ecouterLiens(sommaire: () => Promise<Sommaire | null>, aller: (c: string) => void): Promise<void> {
  const { Capacitor } = await import('@capacitor/core');
  if (!Capacitor.isNativePlatform()) return;
  const { App } = await import('@capacitor/app');
  const ouvrir = async (url: string) => {
    const s = await sommaire();
    if (s) aller(chemin(url, s));
  };
  const depart = await App.getLaunchUrl();
  if (depart?.url) await ouvrir(depart.url);
  await App.addListener('appUrlOpen', ({ url }) => void ouvrir(url));
}
