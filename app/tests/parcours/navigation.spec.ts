import { expect, test } from '@playwright/test';
import { lecteurInstalle, sansViolation } from './outils';

test.beforeEach(async ({ page }) => lecteurInstalle(page));

test('les quatre destinations et leurs écrans sont accessibles (8.1)', async ({ page }) => {
  await page.goto('/');
  await expect(page.getByRole('heading', { level: 1, name: 'Aujourd’hui' })).toBeVisible();
  await expect(page.getByText(/^(Bonjour|Bon après-midi|Bonsoir)$/)).toBeVisible();
  await sansViolation(page, 'Aujourd’hui');
  const nav = page.getByRole('navigation', { name: 'Carte de l’ouvrage' });
  for (const [lien, titre] of [['Le Livre', 'Le Livre'], ['La promenade', 'La promenade'], ['Mon carnet', 'Mon carnet']]) {
    await nav.getByRole('link', { name: lien }).click();
    await expect(page.getByRole('heading', { level: 1, name: titre })).toBeVisible();
    await expect(nav.getByRole('link', { name: lien })).toHaveAttribute('aria-current', 'page');
    await sansViolation(page, titre);
  }
});

test('le sommaire : Prélude et vingt-six chapitres, puis une page de chapitre (8.3)', async ({ page }) => {
  await page.goto('/livre/');
  await expect(page.getByText('Le Prélude', { exact: true })).toBeVisible();
  await expect(page.getByText('Chapitre XXVI')).toBeVisible();
  await expect(page.locator('ol.chapitres > li')).toHaveCount(27);
  await page.getByText('Chapitre I', { exact: true }).click();
  await expect(page.getByRole('heading', { level: 1, name: 'Chapitre 1' })).toBeVisible();
  await expect(page.getByText('Scène 1.1', { exact: true })).toBeVisible();
  await sansViolation(page, 'Chapitre 1');
});

test('lire ce livre : six pages courtes (8.24)', async ({ page }) => {
  await page.goto('/lire-ce-livre/');
  await expect(page.locator('section.carte')).toHaveCount(6);
  await sansViolation(page, 'Lire ce livre');
});
