// Application du thème, de la taille du texte et de la police d'aide (8.10, 9.2, 9.3, 10.8).
import { Capacitor } from '@capacitor/core';
import { StatusBar, Style } from '@capacitor/status-bar';
import { INTERLIGNES, TAILLES, type Preferences } from '$lib/preferences/modele';

export function themeEffectif(theme: Preferences['theme'], sombre: boolean, contrasteEleve: boolean): Exclude<Preferences['theme'], 'automatique'> {
  if (theme !== 'automatique') return theme;
  if (contrasteEleve) return 'contraste';
  return sombre ? 'nuit' : 'papier';
}

export function appliquer(p: Preferences, racine: HTMLElement = document.documentElement): void {
  const sombre = window.matchMedia?.('(prefers-color-scheme: dark)').matches ?? false;
  const contraste = window.matchMedia?.('(prefers-contrast: more)').matches ?? false;
  const effectif = themeEffectif(p.theme, sombre, contraste);
  racine.dataset.theme = effectif;
  racine.dataset.aideLecture = p.aideLecture ? 'oui' : 'non';
  racine.style.setProperty('--base', `${TAILLES[p.tailleCran]}px`);
  racine.style.setProperty('--interligne', String(INTERLIGNES[p.interligneCran]));
  const fond = getComputedStyle(racine).getPropertyValue('--fond').trim();
  document.querySelector('meta[name="theme-color"]')?.setAttribute('content', fond || '#FBF8F3');
  if (Capacitor.isNativePlatform()) {
    void StatusBar.setStyle({ style: effectif === 'nuit' ? Style.Dark : Style.Light }).catch(() => undefined);
  }
}
