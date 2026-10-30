<script lang="ts">
  // « Comment dit-on… ? » (8.9) : recherche hors connexion, en français ou en anglais, dès la première lettre.
  import { onMount } from 'svelte';
  import MiniSearch from 'minisearch';
  import { t } from '$lib/textes/fr';
  import Entete from '$lib/ui/Entete.svelte';
  import Icone from '$lib/ui/Icone.svelte';
  import { OPTIONS } from '$lib/recherche/options.js';

  interface Trouve { ref: string; genre: string; texte: string; sens?: string; scene?: string; numero?: string; moment?: string; lien: string; langue: 'fr' | 'en' }

  let fr: MiniSearch | null = null;
  let en: MiniSearch | null = null;
  let requete = $state('');
  let pret = $state(false);
  let champ: HTMLInputElement | undefined = $state();

  const charger = (f: string) => fetch(f).then((r) => r.text()).then((j) => MiniSearch.loadJSON(j, OPTIONS));

  onMount(async () => {
    [fr, en] = await Promise.all([charger('/corpus/index-fr.json'), charger('/corpus/index-en.json')]).catch(() => [null, null]);
    pret = true;
    champ?.focus();
  });

  const resultats = $derived.by((): Trouve[] => {
    const q = requete.trim();
    if (!pret || !q || !fr || !en) return [];
    const a = fr.search(q).map((r) => ({ ...(r as unknown as Trouve), langue: 'fr' as const, score: r.score }));
    const b = en.search(q).map((r) => ({ ...(r as unknown as Trouve), langue: 'en' as const, score: r.score }));
    return [...a, ...b].sort((x, y) => y.score - x.score).slice(0, 40);
  });
</script>

<Entete titre={t.recherche.titre} retour />

<main class="page">
  <div class="champ">
    <Icone nom="loupe" />
    <input bind:this={champ} bind:value={requete} type="search" inputmode="search" autocomplete="off" spellcheck="false" aria-label={t.recherche.champ} placeholder={t.recherche.champ} />
    {#if requete}
      <button type="button" class="icone" aria-label={t.recherche.effacer} onclick={() => { requete = ''; champ?.focus(); }}><Icone nom="fermer" /></button>
    {/if}
  </div>

  {#if !requete.trim()}
    <h2 class="surtitre">{t.recherche.situations}</h2>
    <ul class="suggestions">
      {#each t.recherche.suggestions as s (s)}
        <li><button type="button" class="pastille ui" onclick={() => (requete = s)}>{s}</button></li>
      {/each}
    </ul>
  {:else if resultats.length}
    <ul class="resultats" aria-live="polite">
      {#each resultats as r (r.langue + r.ref)}
        <li>
          <a class="carte" href={r.lien}>
            {#if r.langue === 'en'}<span class="enonce" lang="en">{r.texte}</span>{:else}<span>{r.texte}</span>{/if}
            {#if r.sens}<span class="douce">{r.sens}</span>{/if}
            {#if r.numero && r.genre !== 'chapitre'}
              <span class="ui douce">{r.moment ? t.recherche.trouveDans(r.numero, r.moment) : t.recherche.trouveDansScene(r.numero)}</span>
            {/if}
          </a>
        </li>
      {/each}
    </ul>
  {:else if pret}
    <p class="etat-vide" aria-live="polite">{t.recherche.sansResultat}</p>
  {/if}
</main>

<style>
  .champ { display: flex; align-items: center; gap: var(--e2); margin: var(--e6) 0; padding: 0 var(--e3); min-height: 52px; border: var(--epaisseur-filet) solid var(--filet); border-radius: var(--rond-pilule); background: var(--surface); color: var(--encre-douce); }
  .champ input { flex: 1; min-width: 0; min-height: var(--cible); border: 0; background: transparent; color: var(--encre); font-family: var(--police-ui); font-size: 17px; outline: none; }
  .champ:focus-within { outline: 2px solid var(--accent); outline-offset: 2px; }
  .icone { display: inline-flex; align-items: center; justify-content: center; min-width: var(--cible); min-height: var(--cible); border: 0; background: none; color: var(--encre-douce); cursor: pointer; }
  ul { list-style: none; padding: 0; margin: 0; }
  .suggestions { display: flex; flex-wrap: wrap; gap: var(--e2); }
  .pastille { min-height: var(--cible); padding: 0 var(--e4); border: var(--epaisseur-filet) solid var(--filet); border-radius: var(--rond-pilule); background: var(--surface); color: var(--encre); font: inherit; cursor: pointer; }
  .resultats .carte { display: flex; flex-direction: column; gap: var(--e1); }
</style>
