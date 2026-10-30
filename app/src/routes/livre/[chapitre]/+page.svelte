<script lang="ts">
  // Page de chapitre (8.3) : ses scènes, leur intention et leur état de lecture.
  import { t } from '$lib/textes/fr';
  import Entete from '$lib/ui/Entete.svelte';
  import { chargerSommaire, chapitreDe, type ChapitreSommaire } from '$lib/corpus/chargeur';
  import { carnet } from '$lib/carnet/base';

  let { data } = $props();
  let chapitre = $state<ChapitreSommaire | null>(null);
  let parcourues = $state(new Set<string>());

  $effect(() => {
    const id = data.chapitre;
    void chargerSommaire().then((s) => (chapitre = chapitreDe(s, id) ?? null)).catch(() => (chapitre = null));
    void carnet.parcourues.toArray().then((p) => (parcourues = new Set(p.map((x) => x.scene)))).catch(() => undefined);
  });
</script>

<Entete titre={chapitre ? (chapitre.numero === 0 ? t.livre.prelude : t.livre.chapitre(chapitre.numero)) : t.livre.titre} retour />

<main class="page">
  {#if chapitre}
    <p class="titre-chapitre">{chapitre.numero === 0 ? chapitre.titre.replace(/^Le Prélude — /, '') : chapitre.titre}</p>
    <ol class="scenes">
      {#each chapitre.scenes as s (s.id)}
        <li>
          {#if s.disponible}
            <a class="carte" href="/scene/{s.id}/">
              <span class="surtitre">{t.livre.scene(s.numero)} · {parcourues.has(s.id) ? t.livre.etat.parcourue : t.livre.etat.decouvrir}</span>
              <span class="titre">{s.titre}</span>
              {#if s.intention}<span class="douce">{s.intention}</span>{/if}
            </a>
          {:else}
            <div class="carte a-venir" aria-disabled="true">
              <span class="surtitre">{t.livre.scene(s.numero)}</span>
              <span class="titre">{s.titre}</span>
            </div>
          {/if}
        </li>
      {/each}
    </ol>
  {:else}
    <p class="etat-vide">{t.lettres.attente}</p>
  {/if}
</main>

<style>
  .titre-chapitre { font-family: var(--police-titre); font-size: 1.6rem; line-height: 1.25; margin: var(--e6) 0; }
  .scenes { list-style: none; margin: 0; padding: 0; }
  .carte { display: flex; flex-direction: column; gap: var(--e1); }
  .titre { font-family: var(--police-titre); font-size: 1.1em; }
  .a-venir { color: var(--encre-douce); border-style: dashed; }
</style>
