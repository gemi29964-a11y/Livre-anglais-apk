import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: 'tests/parcours',
  webServer: { command: 'npm run preview -- --port 4173', port: 4173, reuseExistingServer: false },
  use: { baseURL: 'http://localhost:4173', ...devices['Pixel 7'], locale: 'fr-FR' },
  reporter: [['list'], ['html', { open: 'never' }]]
});
