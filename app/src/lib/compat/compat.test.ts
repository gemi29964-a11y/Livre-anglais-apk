// Vérifie le complément de compatibilité static/compat/compat.js sur un environnement privé de replaceAll et structuredClone.
import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { afterEach, beforeEach, describe, expect, it } from 'vitest';

const source = readFileSync(resolve(__dirname, '../../../static/compat/compat.js'), 'utf8');
const g = globalThis as unknown as { structuredClone?: unknown };
const proto = String.prototype as unknown as { replaceAll?: unknown };
let origineReplaceAll: unknown;
let origineClone: unknown;

beforeEach(() => {
  origineReplaceAll = proto.replaceAll;
  origineClone = g.structuredClone;
  delete proto.replaceAll;
  delete g.structuredClone;
  new Function(source)();
});

afterEach(() => {
  Object.defineProperty(String.prototype, 'replaceAll', { value: origineReplaceAll, configurable: true, writable: true });
  g.structuredClone = origineClone;
});

describe('compat.js', () => {
  it('complète replaceAll avec une chaîne, des caractères spéciaux et le motif $', () => {
    const s = 'a<!>b<!>c' as unknown as { replaceAll: (m: string | RegExp, r: string) => string };
    expect(s.replaceAll('<!>', '<!---->')).toBe('a<!---->b<!---->c');
    expect(('1.2.3' as unknown as typeof s).replaceAll('.', '$')).toBe('1$2$3');
    expect(('x/*n*/y' as unknown as typeof s).replaceAll(/\/\*.*?\*\//g, '')).toBe('xy');
    expect(() => ('x' as unknown as typeof s).replaceAll(/x/, '')).toThrow(TypeError);
  });

  it('complète structuredClone par une copie profonde indépendante', () => {
    const clone = g.structuredClone as <T>(v: T) => T;
    const o = { a: [1, { b: 2 }], d: new Date(5), m: new Map([[1, 'un']]) };
    const c = clone(o);
    expect(c).toEqual(o);
    expect(c.a).not.toBe(o.a);
    expect(c.d.getTime()).toBe(5);
    expect(c.m.get(1)).toBe('un');
    const cyclique: { soi?: unknown } = {};
    cyclique.soi = cyclique;
    const cc = clone(cyclique);
    expect(cc.soi).toBe(cc);
  });
});
