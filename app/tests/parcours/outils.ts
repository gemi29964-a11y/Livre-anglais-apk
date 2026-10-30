import AxeBuilder from '@axe-core/playwright';
import { expect, type Page } from '@playwright/test';

/** Accessibilité (11.2) : zéro violation « serious » ou « critical » sur l'écran affiché. */
export async function sansViolation(page: Page, ecran: string) {
  // Les transitions d'entrée (9.7) sont achevées avant la mesure : on juge l'écran tel qu'il se lit.
  await page.waitForFunction(() => document.getAnimations().every((a) => a.playState !== 'running'));
  const r = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa']).analyze();
  const graves = r.violations.filter((v) => v.impact === 'serious' || v.impact === 'critical');
  expect(graves.map((v) => `${ecran} — ${v.id} : ${v.nodes.map((n) => n.target.join(' ')).join(', ')}`)).toEqual([]);
}

/** Lecteur ayant déjà passé l'accueil (préférences Capacitor stockées dans localStorage sur le web). */
export async function lecteurInstalle(page: Page, prefs: Record<string, unknown> = {}) {
  await page.addInitScript((p) => {
    if (localStorage.getItem('CapacitorStorage.preferences') === null)
      localStorage.setItem('CapacitorStorage.preferences', JSON.stringify({ accueilFait: true, ...p }));
  }, prefs);
}
