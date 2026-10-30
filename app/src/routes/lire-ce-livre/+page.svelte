<script lang="ts">
  // Lire ce livre (8.12) : six pages courtes, chacune lisible en moins d'une minute.
  import { t } from '$lib/textes/fr';
  import Entete from '$lib/ui/Entete.svelte';
</script>

<Entete titre={t.lireCeLivre.titre} retour />

<main class="page">
  <p class="intro">{t.lireCeLivre.intro}</p>
  {#each t.lireCeLivre.pages as p, i (p.id)}
    <section class="carte" id={p.id}>
      <p class="surtitre">{t.lireCeLivre.page(i + 1, t.lireCeLivre.pages.length)}</p>
      <h2>{p.titre}</h2>
      <p>{p.texte}</p>
    </section>
  {/each}
</main>

<style>
  .intro { margin: var(--e6) 0; }
</style>
