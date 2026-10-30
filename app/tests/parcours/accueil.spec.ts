import { expect, test } from '@playwright/test';
import { sansViolation } from './outils';

test('premier lancement : quatre écrans, choix de l’accent et du niveau (8.11)', async ({ page }) => {
  await page.goto('/');
  await expect(page.getByText('Vivre l’Anglais')).toBeVisible();
  await expect(page.getByText('Bienvenue. Ce livre se lit avec les oreilles autant qu’avec les yeux.')).toBeVisible();
  await sansViolation(page, 'accueil 1');
  await page.getByRole('button', { name: 'Commencer' }).click();
  await expect(page.getByText(/Quelle voix souhaitez-vous entendre en premier/)).toBeVisible();
  await page.getByRole('button', { name: /Américain/ }).click();
  await expect(page.getByRole('button', { name: /Américain/ })).toHaveAttribute('aria-pressed', 'true');
  await sansViolation(page, 'accueil 2');
  await page.getByRole('button', { name: 'Continuer' }).click();
  await expect(page.getByText(/Où en êtes-vous en anglais/)).toBeVisible();
  await sansViolation(page, 'accueil 3');
  await page.getByRole('button', { name: 'Je suis à l’aise' }).click();
  await expect(page.getByText(/Un rendez-vous quotidien/)).toBeVisible();
  await sansViolation(page, 'accueil 4');
  await page.getByRole('button', { name: 'Pas maintenant' }).click();
  await expect(page.getByRole('navigation', { name: 'Carte de l’ouvrage' })).toBeVisible();
  const prefs = await page.evaluate(() => JSON.parse(localStorage.getItem('CapacitorStorage.preferences') ?? '{}'));
  expect(prefs).toMatchObject({ accueilFait: true, accent: 'us', niveau: 'maitrise', rythme: 'spontane' });
});

test('l’accueil se passe en un geste', async ({ page }) => {
  await page.goto('/');
  await page.getByRole('button', { name: 'Passer l’accueil' }).click();
  await expect(page.getByRole('navigation', { name: 'Carte de l’ouvrage' })).toBeVisible();
  await page.reload();
  await expect(page.getByRole('button', { name: 'Commencer' })).toHaveCount(0);
});
