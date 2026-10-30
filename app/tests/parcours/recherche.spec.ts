import { expect, test } from '@playwright/test';
import { lecteurInstalle, sansViolation } from './outils';

test.beforeEach(async ({ page }) => lecteurInstalle(page));

test('« Comment dit-on… ? » trouve dès les premières lettres, sans accents ni casse (8.9)', async ({ page }) => {
  await page.goto('/');
  await page.getByRole('link', { name: 'Comment dit-on… ?' }).click();
  const champ = page.getByRole('searchbox', { name: 'Une expression, en français ou en anglais' });
  await expect(champ).toBeFocused();
  await expect(page.getByRole('button', { name: 'Refuser poliment' })).toBeVisible();
  await sansViolation(page, 'recherche vide');
  await champ.fill('reveil');
  await expect(page.locator('.resultats a').first()).toBeVisible();
  await expect(page.locator('.resultats')).toContainText(/réveil/i);
  await sansViolation(page, 'résultats');
  await champ.fill('zzqqxx');
  await expect(page.getByText(/Rien de tel dans le livre pour l’instant/)).toBeVisible();
  await page.getByRole('button', { name: 'Effacer la recherche' }).click();
  await expect(champ).toHaveValue('');
});
