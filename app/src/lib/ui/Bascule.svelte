<script lang="ts" generics="V extends string">
  // Bascule segmentée (9.5) : groupe de choix exclusifs, rôle radiogroup (10.6).
  let {
    libelle,
    options,
    valeur,
    onchange
  }: { libelle: string; options: { valeur: V; libelle: string; abrege?: string }[]; valeur: V; onchange: (v: V) => void } = $props();

  function clavier(e: KeyboardEvent, i: number) {
    const pas = e.key === 'ArrowRight' || e.key === 'ArrowDown' ? 1 : e.key === 'ArrowLeft' || e.key === 'ArrowUp' ? -1 : 0;
    if (!pas) return;
    e.preventDefault();
    const suivant = options[(i + pas + options.length) % options.length];
    onchange(suivant.valeur);
    const groupe = (e.currentTarget as HTMLElement).parentElement;
    queueMicrotask(() => (groupe?.querySelector('[aria-checked="true"]') as HTMLElement | null)?.focus());
  }
</script>

<div class="bascule ui" role="radiogroup" aria-label={libelle}>
  {#each options as o, i (o.valeur)}
    <button
      type="button"
      role="radio"
      aria-checked={o.valeur === valeur}
      tabindex={o.valeur === valeur ? 0 : -1}
      onclick={() => onchange(o.valeur)}
      onkeydown={(e) => clavier(e, i)}
    >{o.libelle}</button>
  {/each}
</div>

<style>
  .bascule {
    display: inline-flex;
    flex-wrap: wrap;
    gap: 2px;
    padding: 2px;
    border: var(--epaisseur-filet) solid var(--filet);
    border-radius: var(--rond-pilule);
    background: var(--surface);
  }
  button {
    min-height: var(--cible);
    min-width: var(--cible);
    padding: 0 var(--e4);
    border: 0;
    border-radius: var(--rond-pilule);
    background: transparent;
    color: var(--encre-douce);
    font: inherit;
    cursor: pointer;
    transition: background var(--duree-micro) var(--courbe-entree), color var(--duree-micro) var(--courbe-entree);
  }
  button[aria-checked='true'] {
    background: var(--accent);
    color: var(--surface);
    font-weight: 600;
  }
</style>
