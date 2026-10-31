// Boucle de production reprenable : préparer → rendre (voix intégrée) → intégrer (découpe + contrôle 7.10) → reprendre.
// Usage (orchestrateur JS) : const { tour } = await import(".../pipeline.mjs"); await tour(tools, opts)
import cp from "node:child_process"; import fs from "node:fs";
import { rendre } from "./rendre_lots.mjs";
const R = "/home/user/workspace/repo";
const py = (args) => cp.execFileSync("python3", args, { cwd: R, maxBuffer: 1 << 26 }).toString();
export function preparer(scripts, rythme, maxT = 6, taille = 12, essai = false) {
  const lots = [];
  for (const s of scripts) {
    const o = JSON.parse(py(["voix/outils/creer.py", "preparer", "--script", s, "--rythme", rythme, "--taille", String(taille), "--max-tentatives", String(maxT), ...(essai ? ["--essai"] : [])]));
    lots.push(...o.lots);
  }
  return lots;
}
export function integrer(filtre) {
  return new Promise((ok) => {
    const p = cp.spawn("python3", ["voix/outils/creer.py", "integrer-tout", "--filtre", filtre], { cwd: R });
    let out = ""; p.stdout.on("data", d => out += d); p.stderr.on("data", () => {});
    p.on("close", () => ok(out.split("\n").filter(l => l.startsWith("{")).map(l => JSON.parse(l))));
  });
}
export async function tour(tools, { scripts, rythme, filtre, maxT = 6, conc = 6, journal = () => {} }) {
  const lots = preparer(scripts, rythme, maxT);
  journal(`préparés ${lots.length}`);
  const rendus = await rendre(tools, d => new RegExp(filtre).test(d), conc);
  journal(`rendus ${rendus.filter(x => x.ok).length}/${rendus.length}`);
  const bilan = await integrer(filtre);
  return { prepares: lots.length, rendus: rendus.filter(x => x.ok).length, echecs_rendu: rendus.filter(x => !x.ok).length, bilan };
}
