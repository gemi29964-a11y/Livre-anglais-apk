import { sveltekit } from '@sveltejs/kit/vite';
import { svelteTesting } from '@testing-library/svelte/vite';
import { defineConfig } from 'vitest/config';
import { readFileSync } from 'node:fs';

const { version } = JSON.parse(readFileSync(new URL('./package.json', import.meta.url), 'utf-8')) as { version: string };

export default defineConfig({
  plugins: [sveltekit(), svelteTesting()],
  define: { __EDITION__: JSON.stringify(version) },
  build: { target: 'es2020', cssCodeSplit: true },
  test: {
    environment: 'jsdom',
    include: ['src/**/*.test.ts'],
    setupFiles: ['src/tests/preparation.ts'],
    coverage: {
      provider: 'v8',
      include: ['src/lib/voix/**/*.ts', 'src/lib/retrouvailles/**/*.ts', 'src/lib/carnet/**/*.ts', 'src/lib/corpus/**/*.ts', 'src/lib/textes/**/*.ts', 'src/lib/preferences/**/*.ts', 'src/lib/ui/phrase.ts'],
      exclude: ['**/*.test.ts', 'src/lib/corpus/types.ts'],
      thresholds: { lines: 90, functions: 90, statements: 90, branches: 85 },
      reporter: ['text', 'json-summary']
    }
  }
});
