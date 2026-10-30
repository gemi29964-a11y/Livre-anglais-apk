<script lang="ts">
  // Un itinéraire (8.3, 4.6) : ses étapes et leurs expressions.
  import { t } from '$lib/textes/fr';
  import Entete from '$lib/ui/Entete.svelte';
  import type { Itineraire } from '$lib/corpus/types';

  let { data } = $props();
  let itineraire = $state<Itineraire | null>(null);

  $effect(() => {
    const id = data.id;
    void fetch('/corpus/itineraires.json').then((r) => r.json()).then((l: Itineraire[]) => (itineraire = l.find((i) => i.id === id) ?? null)).catch(() => (itineraire = null));
  });
</script>

<Entete titre={itineraire?.titre ?? t.livre.itineraires} retour />

<main class="page">
  {#if itineraire}
    <p class="douce">{itineraire.pourQui}</p>
    <ol class="etapes">
      {#each itineraire.etapes as e, i (i)}
        <li class="carte"><h2>{e.titre}</h2><p class="ui douce">{t.aujourdhui.expressionsRestantes(e.expressions.length)}</p></li>
      {/each}
    </ol>
  {:else}
    <p class="etat-vide">{t.lettres.attente}</p>
  {/if}
</main>

<style>
  .etapes { list-style: none; padding: 0; margin: var(--e6) 0; }
</style>
