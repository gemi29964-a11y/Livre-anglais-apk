<script lang="ts">
  // L'encre qui s'écrit (9.8) : au-delà de 300 ms d'attente, un fin trait se trace sous le titre.
  // Aucun indicateur rotatif, aucun mot pour l'attente.
  let { active = false }: { active?: boolean } = $props();
  let visible = $state(false);

  $effect(() => {
    if (!active) { visible = false; return; }
    const minuteur = setTimeout(() => (visible = true), 300);
    return () => clearTimeout(minuteur);
  });
</script>

<div class="piste" aria-hidden="true">
  {#if visible}<span class="encre"></span>{/if}
</div>

<style>
  .piste { height: 2px; overflow: hidden; }
  .encre {
    display: block;
    height: 2px;
    background: var(--accent);
    transform-origin: left center;
    animation: ecrire 1.2s var(--courbe-entree) infinite;
  }
  @keyframes ecrire {
    from { transform: scaleX(0); opacity: 1; }
    80% { transform: scaleX(1); opacity: 1; }
    to { transform: scaleX(1); opacity: 0; }
  }
  @media (prefers-reduced-motion: reduce) {
    .encre { animation: none; opacity: 0.6; }
  }
</style>
