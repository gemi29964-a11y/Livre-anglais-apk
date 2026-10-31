import { describe, expect, it, vi } from 'vitest';

const fichiers: { name: string }[] = [];
let absent = false;
vi.mock('@capacitor/filesystem', () => ({
  Directory: { Data: 'DATA' },
  Filesystem: {
    readdir: vi.fn(async () => { if (absent) throw new Error('absent'); return { files: fichiers }; }),
    rmdir: vi.fn(async () => { if (absent) throw new Error('absent'); fichiers.length = 0; })
  }
}));

import { decoder, lister, toutEffacer } from './maVoix';

describe('Ma voix (10.10)', () => {
  it('décode les noms {id}-{horodatage}.m4a', () => {
    expect(decoder('c01.s01.A1.e1-1761800000000.m4a')).toEqual({ nom: 'c01.s01.A1.e1-1761800000000.m4a', expression: 'c01.s01.A1.e1', date: 1761800000000 });
    expect(decoder('autre.txt')).toBeNull();
  });
  it('liste du plus récent au plus ancien et efface tout', async () => {
    fichiers.push({ name: 'a-1761800000000.m4a' }, { name: 'b-1761900000000.m4a' }, { name: 'intrus.tmp' });
    expect((await lister()).map((e) => e.expression)).toEqual(['b', 'a']);
    await toutEffacer();
    expect(await lister()).toEqual([]);
    absent = true;
    expect(await lister()).toEqual([]);
    await expect(toutEffacer()).resolves.toBeUndefined();
  });
});
