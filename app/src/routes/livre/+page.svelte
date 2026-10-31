<script lang="ts">
  // Le Livre (8.3) : le sommaire — Prélude, vingt-six chapitres, Itinéraires, Appendices.
  import { onMount } from 'svelte';
  import { t } from '$lib/textes/fr';
  import Entete from '$lib/ui/Entete.svelte';
  import { chargerSommaire, type Sommaire } from '$lib/corpus/chargeur';
  import { carnet } from '$lib/carnet/base';

  let sommaire = $state<Sommaire | null>(null);
  let parcourues = $state(new Set<string>());
  let itineraires = $state<{ id: string; titre: string; pourQui: string }[]>([]);

  onMount(async () => {
    sommaire = await chargerSommaire().catch(() => null);
    parcourues = await carnet.parcourues().catch(() => new Set<string>());
    itineraires = await fetch('/corpus/itineraires.json').then((r) => (r.ok ? r.json() : [])).catch(() => []);
  });

  const total = $derived(sommaire?.chapitres.reduce((n, c) => n + c.scenes.length, 0) ?? 0);
</script>

<Entete titre={t.livre.titre} />

<main class="page">
  {#if sommaire}
    <p class="ui douce">{t.livre.cheminParcouru(parcourues.size, total)}</p>
    <div class="filet-chemin" aria-hidden="true"><span style:width="{total ? (100 * parcourues.size) / total : 0}%"></span></div>
    <ol class="chapitres">
      {#each sommaire.chapitres as c (c.id)}
        {@const faites = c.scenes.filter((s) => parcourues.has(s.id)).length}
        <li>
          <a class="carte chapitre" href="/livre/{c.id}/">
            <span class="surtitre">{c.numero === 0 ? t.livre.prelude : t.livre.chapitreRomain(c.numero)}</span>
            <span class="titre">{c.numero === 0 ? c.titre.replace(/^Le Prélude — /, '') : c.titre}</span>
            <span class="ui douce">{t.livre.scenes(c.scenes.length)}</span>
            <span class="filet-chemin" aria-hidden="true"><span style:width="{(100 * faites) / c.scenes.length}%"></span></span>
          </a>
        </li>
      {/each}
    </ol>

    {#if itineraires.length}
      <h2>{t.livre.itineraires}</h2>
      {#each itineraires as i (i.id)}
        <a class="carte" href="/itineraire/{i.id}/"><span class="titre">{i.titre}</span><span class="douce">{i.pourQui}</span></a>
      {/each}
    {/if}

    <h2>{t.livre.appendices}</h2>
    <a class="carte" href="/lire-ce-livre/">{t.lireCeLivre.titre}</a>
  {:else}
    <p class="etat-vide">{t.lettres.attente}</p>
  {/if}
</main>

<style>
  .chapitres { list-style: none; margin: var(--e6) 0; padding: 0; }
  .chapitre { display: flex; flex-direction: column; gap: var(--e1); }
  .titre { font-family: var(--police-titre); font-size: 1.15em; display: block; }
  h2 { font-family: var(--police-titre); font-weight: 600; margin: var(--e8) 0 var(--e4); }
</style>
