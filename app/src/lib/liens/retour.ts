// Retour arrière (10.6, 10.8) : un seul écouteur backButton. Il ferme d'abord un volet ouvert,
// puis remonte l'historique, puis, depuis Aujourd'hui, laisse le système refermer le livre.
import { App } from '@capacitor/app';
import { Capacitor } from '@capacitor/core';

const volets: (() => void)[] = [];

/** Déclare un volet ouvert ; renvoie la fonction qui le retire de la pile. */
export function voletOuvert(fermer: () => void): () => void {
  volets.push(fermer);
  return () => {
    const i = volets.lastIndexOf(fermer);
    if (i !== -1) volets.splice(i, 1);
  };
}

export type Action = 'volet' | 'historique' | 'quitter';

/** Décision pure, testée unitairement : que faire d'un retour ? */
export function decider(nbVolets: number, chemin: string, peutRevenir: boolean): Action {
  if (nbVolets > 0) return 'volet';
  if (chemin !== '/' && peutRevenir) return 'historique';
  if (chemin !== '/') return 'historique';
  return 'quitter';
}

export function traiterRetour(chemin: string, peutRevenir: boolean, allerAujourdhui: () => void): Action {
  const action = decider(volets.length, chemin, peutRevenir);
  if (action === 'volet') volets.pop()?.();
  else if (action === 'historique') {
    if (peutRevenir) history.back();
    else allerAujourdhui();
  } else void App.minimizeApp();
  return action;
}

let installe = false;

export function installerRetour(chemin: () => string, allerAujourdhui: () => void): void {
  if (installe || !Capacitor.isNativePlatform()) return;
  installe = true;
  void App.addListener('backButton', ({ canGoBack }) => traiterRetour(chemin(), canGoBack, allerAujourdhui));
  // Plan B prescrit (10.8) : MainActivity émet « retourDemande » si le système intercepte le geste.
  window.addEventListener('retourDemande', () => traiterRetour(chemin(), history.length > 1, allerAujourdhui));
}

export const _test = { volets };
