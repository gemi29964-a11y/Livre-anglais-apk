import { expect, test } from '@playwright/test';
import { lecteurInstalle, sansViolation } from './outils';

test.beforeEach(async ({ page }) => lecteurInstalle(page));

test('les Préférences s’appliquent et se conservent (8.10)', async ({ page }) => {
  await page.goto('/preferences/');
  await expect(page.getByRole('heading', { level: 2, name: 'Les voix' })).toBeVisible();
  await sansViolation(page, 'Préférences');
  await page.getByRole('radiogroup', { name: 'Thème' }).getByRole('radio', { name: 'Nuit' }).click();
  await expect(page.locator('html')).toHaveAttribute('data-theme', 'nuit');
  await sansViolation(page, 'Préférences, thème Nuit');
  await page.getByRole('radiogroup', { name: 'Thème' }).getByRole('radio', { name: 'Contraste' }).click();
  await expect(page.locator('html')).toHaveAttribute('data-theme', 'contraste');
  await sansViolation(page, 'Préférences, thème Contraste');
  await page.getByRole('radiogroup', { name: 'Thème' }).getByRole('radio', { name: 'Ambre' }).click();
  await sansViolation(page, 'Préférences, thème Ambre');
  await page.getByRole('radiogroup', { name: 'Accent préféré' }).getByRole('radio', { name: 'Américain' }).click();
  await page.reload();
  await expect(page.locator('html')).toHaveAttribute('data-theme', 'ambre');
  await expect(page.getByRole('radiogroup', { name: 'Accent préféré' }).getByRole('radio', { name: 'Américain' })).toHaveAttribute('aria-checked', 'true');
});

test('tout effacer demande une double confirmation (8.10)', async ({ page }) => {
  await page.goto('/preferences/');
  const bouton = page.getByRole('button', { name: 'Tout effacer' });
  await bouton.click();
  await expect(page.getByText(/Effacer définitivement votre carnet/)).toBeVisible();
  await bouton.click();
  await expect(page.getByText(/Vraiment tout effacer/)).toBeVisible();
  await bouton.click();
  await expect(page.getByText('Votre carnet a été effacé.')).toBeAttached();
});
