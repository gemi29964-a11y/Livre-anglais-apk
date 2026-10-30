<script lang="ts">
  // La promenade (8.7) : les programmes d'écoute mains libres, écran éteint.
  import { onMount } from 'svelte';
  import { t } from '$lib/textes/fr';
  import Entete from '$lib/ui/Entete.svelte';
  import Icone from '$lib/ui/Icone.svelte';
  import { chargerSommaire } from '$lib/corpus/chargeur';

  const programmes = Object.entries(t.promenade.programme);
  let disponible = $state(false);

  onMount(async () => {
    const s = await chargerSommaire().catch(() => null);
    disponible = !!s?.chapitres.some((c) => c.scenes.some((x) => x.disponible));
  });
</script>

<Entete titre={t.promenade.titre} />

<main class="page">
  <p class="intro">{t.promenade.intro}</p>
  {#if disponible}
    <h2 class="surtitre">{t.promenade.programmes}</h2>
    {#each programmes as [cle, p] (cle)}
      <div class="carte">
        <h3>{p.titre}</h3>
        <p class="douce">{p.texte}</p>
      </div>
    {/each}
  {:else}
    <div class="etat-vide">
      <Icone nom="casque" taille={40} />
      <p>{t.promenade.rienAEcouter}</p>
    </div>
  {/if}
</main>

<style>
  .intro { margin: var(--e6) 0; }
</style>
