<script lang="ts">
  // Le phrasé (6.4, 10.6) : capitales → syllabe forte en bas de casse ; ‿ → liaison arquée ;
  // (t) → son retenu ; ʔ → ’ ; ɾ → d pointillé ; ʳ → r en exposant ; flèches d'intonation.
  // Masqué pour les lecteurs d'écran (9.9) : la voix elle-même est l'information.
  import { decouper } from './phrase';
  import { t } from '$lib/textes/fr';

  let { phrase, active = -1 }: { phrase: string; active?: number } = $props();
  const segments = $derived(decouper(phrase));
</script>

<span class="phrase" aria-hidden="true">
  {#each segments as s, i (i)}
    {#if s.genre === 'syllabe'}
      {#if s.forte}<b class="fort" class:active={s.index === active}>{s.texte}</b>{:else}<span class="syl" class:active={s.index === active}>{s.texte}</span>{/if}
    {:else if s.genre === 'frontiere'}<span class="frontiere">·</span>
    {:else if s.genre === 'lien'}<span class="lien">‿</span>
    {:else if s.genre === 'espace'}{' '}
    {:else if s.genre === 'retenu'}<span class="retenu">{s.texte}</span>
    {:else if s.genre === 'glotte'}<span class="glotte" title={t.phrase.glotte}>’</span>
    {:else if s.genre === 'battu'}<span class="battu" title={t.phrase.battu}>d</span>
    {:else if s.genre === 'liaisonR'}<sup class="liaison-r">r</sup>
    {:else if s.genre === 'intonation'}<span class="intonation">{s.texte}</span>
    {/if}
  {/each}
</span>

<style>
  .phrase {
    font-family: var(--police-phrase);
    font-size: var(--taille-phrase);
    color: var(--encre-douce);
    letter-spacing: 0.01em;
    hyphens: none;
  }
  .fort { font-weight: 700; color: var(--encre); }
  .active { color: var(--accent); text-decoration: underline 2px; text-underline-offset: 4px; }
  .frontiere { opacity: 0.55; padding: 0 0.04em; }
  .lien { display: inline-block; transform: translateY(0.35em); opacity: 0.7; margin: 0 -0.08em; }
  .retenu { opacity: 0.55; }
  .battu { text-decoration: underline dotted 1.5px; text-underline-offset: 3px; }
  .liaison-r { font-size: 0.7em; }
  .intonation { margin-left: 0.25em; color: var(--accent); }
  @media (prefers-reduced-motion: reduce) {
    .active { text-decoration: none; }
  }
</style>
