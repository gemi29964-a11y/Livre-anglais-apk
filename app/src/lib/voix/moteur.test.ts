import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';

vi.mock('./source', () => ({ urlVoix: vi.fn(async (id: string) => (id.startsWith('absent') ? null : `/voix/${id}.opus`)) }));

// Contexte audio factice : horloge pilotée par le test, sources dont la fin est déclenchée à la main.
class Param { value = 1; setValueAtTime() { return this; } linearRampToValueAtTime() { return this; } cancelScheduledValues() { return this; } }
const sources: FausseSource[] = [];
class FausseSource {
  buffer: unknown = null; onended: (() => void) | null = null; demarre: unknown[] = []; arrete = false;
  connect(n: unknown) { return n; }
  start(...a: unknown[]) { this.demarre = a; }
  stop() { this.arrete = true; }
  finir() { this.onended?.(); }
  constructor() { sources.push(this); }
}
class FauxContexte {
  state = 'suspended'; currentTime = 0; destination = {};
  resume() { this.state = 'running'; return Promise.resolve(); }
  createGain() { return { gain: new Param(), connect: (n: unknown) => n }; }
  createBufferSource() { return new FausseSource(); }
  decodeAudioData = vi.fn(async (_b: ArrayBuffer) => ({ duration: 0.01 }));
}
let ctx: FauxContexte;
vi.stubGlobal('AudioContext', vi.fn(function () { ctx = new FauxContexte(); return ctx; }));
let rafs: FrameRequestCallback[] = [];
vi.stubGlobal('requestAnimationFrame', (f: FrameRequestCallback) => { rafs.push(f); return rafs.length; });
vi.stubGlobal('cancelAnimationFrame', () => undefined);
const fetchMock = vi.fn(async (u: string) => ({ ok: !u.includes('casse'), arrayBuffer: async () => new ArrayBuffer(8) }));
vi.stubGlobal('fetch', fetchMock);

import { moteur } from './moteur';

const attendre = () => new Promise((r) => setTimeout(r, 0));
const derniere = () => sources[sources.length - 1];

describe('moteur des voix (10.6)', () => {
  beforeEach(() => { sources.length = 0; rafs = []; fetchMock.mockClear(); });
  afterEach(() => { moteur.arreter(); vi.useRealTimers(); });

  it('joue une voix et se résout « fini » à la fin, en suivant mots et syllabes', async () => {
    const mots: number[] = []; let fortes = 0; const temps: number[] = [];
    moteur.onMot = (i) => mots.push(i); moteur.onSyllabeForte = () => fortes++; moteur.onTemps = (t) => temps.push(t);
    const p = moteur.jouer({ id: 'c01.s01.A1.e1', accent: 'uk', rythme: 'pose', mots: [['My', 0, 0.2], ['alarm', 0.2, 0.6]], syllabes: [[0, 0.2, 0], [0.2, 0.6, 1]] });
    await attendre(); await attendre();
    expect(moteur.enLecture).toBe(true);
    ctx.currentTime = 0.1; rafs.shift()?.(0);
    ctx.currentTime = 0.3; rafs.shift()?.(0);
    ctx.currentTime = 0.35; rafs.shift()?.(0);
    expect(mots).toEqual([0, 1]);
    expect(fortes).toBe(1);
    expect(temps.length).toBe(3);
    derniere().finir();
    await expect(p).resolves.toBe('fini');
    expect(moteur.enLecture).toBe(false);
  });

  it('garde les voix décodées en cache et partage un chargement en cours', async () => {
    const a = moteur.preparer('cache.1', 'uk', 'pose');
    const b = moteur.preparer('cache.1', 'uk', 'pose');
    expect(await a).toBe(await b);
    await moteur.preparer('cache.1', 'uk', 'pose');
    expect(fetchMock).toHaveBeenCalledTimes(1);
    for (let i = 0; i < 100; i++) await moteur.preparer(`lru.${i}`, 'us', 'pose');
    fetchMock.mockClear();
    await moteur.preparer('cache.1', 'uk', 'pose');
    expect(fetchMock).toHaveBeenCalledTimes(1);              // chassé du cache LRU (96 entrées)
  });

  it('rend « absent » pour une voix introuvable, un fichier en erreur ou abîmé', async () => {
    expect(await moteur.jouer({ id: 'absent.1', accent: 'uk', rythme: 'pose' })).toBe('absent');
    expect(await moteur.jouer({ id: 'casse.1', accent: 'uk', rythme: 'pose' })).toBe('absent');
    ctx.decodeAudioData.mockRejectedValueOnce(new Error('abîmé'));
    expect(await moteur.jouer({ id: 'abime.1', accent: 'uk', rythme: 'pose' })).toBe('absent');
  });

  it('interrompt la voix en cours avec un fondu', async () => {
    const p = moteur.jouer({ id: 'stop.1', accent: 'uk', rythme: 'pose' });
    await attendre(); await attendre();
    const s = derniere();
    moteur.arreter();
    await expect(p).resolves.toBe('interrompu');
    expect(s.arrete).toBe(true);
    s.finir();                                               // une fin tardive n'a plus d'effet
  });

  it('écoute au mot : segment exact, ou groupe de souffle pour un mot faible (8.14)', async () => {
    const mots: [string, number, number][] = [['I', 0, 0.1], ['want', 0.1, 0.4], ['to', 0.4, 0.5], ['go', 0.5, 0.9]];
    expect(await moteur.jouerMot({ id: 'mot.1', accent: 'uk', rythme: 'pose', mots }, 9)).toBe('absent');
    const p = moteur.jouerMot({ id: 'mot.1', accent: 'uk', rythme: 'pose', mots }, 1);
    await attendre(); await attendre();
    expect(derniere().demarre).toEqual([0, 0.1, expect.closeTo(0.3, 5)]);
    derniere().finir(); await p;
    const q = moteur.jouerMot({ id: 'mot.1', accent: 'uk', rythme: 'pose', mots }, 2);
    await attendre(); await attendre();
    expect(derniere().demarre).toEqual([0, 0.1, expect.closeTo(0.8, 5)]);
    derniere().finir(); await q;
  });

  it('les quatre voix : ordre du lecteur, saut des absentes, arrêt sur interruption', async () => {
    vi.useFakeTimers();
    const ordre: string[] = [];
    const p = moteur.quatre('q.1', 'us', () => ({}), (a, r) => ordre.push(`${a}-${r}`));
    for (let i = 0; i < 4; i++) {
      await vi.advanceTimersByTimeAsync(0);
      derniere().finir();
      await vi.advanceTimersByTimeAsync(600);
    }
    await expect(p).resolves.toBe('fini');
    expect(ordre).toEqual(['us-pose', 'us-spontane', 'uk-pose', 'uk-spontane']);
    const absent = moteur.quatre('absent.q', 'uk', () => ({}), () => undefined);
    await expect(absent).resolves.toBe('fini');
    const r = moteur.quatre('q.2', 'uk', () => ({}), () => undefined);
    await vi.advanceTimersByTimeAsync(0);
    derniere().finir();
    await vi.advanceTimersByTimeAsync(100);
    moteur.arreter();
    await vi.advanceTimersByTimeAsync(600);
    await expect(r).resolves.toBe('interrompu');
    const s = moteur.quatre('q.3', 'uk', () => ({}), () => undefined);
    await vi.advanceTimersByTimeAsync(0);
    moteur.arreter();
    await expect(s).resolves.toBe('interrompu');
  });

  it('l’écho : passages séparés d’un silence de 1,3 fois la durée (8.16)', async () => {
    vi.useFakeTimers();
    const silences: number[] = [];
    const p = moteur.echo({ id: 'echo.1', accent: 'uk', rythme: 'pose' }, 2, (ms) => silences.push(ms));
    for (let i = 0; i < 2; i++) { await vi.advanceTimersByTimeAsync(0); derniere().finir(); await vi.advanceTimersByTimeAsync(13); }
    await expect(p).resolves.toBe('fini');
    expect(silences).toEqual([13, 13]);
    expect(await moteur.echo({ id: 'absent.e', accent: 'uk', rythme: 'pose' }, 2, () => undefined)).toBe('absent');
    const q = moteur.echo({ id: 'echo.2', accent: 'uk', rythme: 'pose' }, 3, () => undefined);
    await vi.advanceTimersByTimeAsync(0); moteur.arreter();
    await expect(q).resolves.toBe('interrompu');
    const r = moteur.echo({ id: 'echo.3', accent: 'uk', rythme: 'pose' }, 3, () => undefined);
    await vi.advanceTimersByTimeAsync(0); derniere().finir(); await vi.advanceTimersByTimeAsync(1); moteur.arreter();
    await vi.advanceTimersByTimeAsync(20);
    await expect(r).resolves.toBe('interrompu');
  });
});
