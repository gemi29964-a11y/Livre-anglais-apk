// Rend les lots préparés par creer.py avec la voix intégrée (Gemini 2.5 Pro TTS) — reprenable :
// un lot qui possède déjà son rendu (rendu.mp3) n'est pas rejoué. Usage : depuis l'orchestrateur JS,
//   await rendre(tools, motif, concurrence)
import fs from "node:fs"; import path from "node:path";
export async function rendre(tools, filtre, concurrence = 6, journal = () => {}) {
  const T = "/home/user/workspace/repo/voix/travail";
  const lots = fs.readdirSync(T).filter(d => filtre(d)).map(d => path.join(T, d))
    .filter(d => fs.existsSync(path.join(d, "lot.json")) && !fs.existsSync(path.join(d, "rendu.mp3")))
    .filter(d => !JSON.parse(fs.readFileSync(path.join(d, "lot.json"))).integre);
  let i = 0; const res = [];
  async function ouvrier() {
    while (i < lots.length) {
      const d = lots[i++]; const lot = JSON.parse(fs.readFileSync(path.join(d, "lot.json")));
      const txt = path.join(d, lot.nom + ".txt");
      const tmp = path.join("/home/user/workspace/rendu_tmp", lot.nom + ".txt");
      fs.mkdirSync(path.dirname(tmp), { recursive: true }); fs.copyFileSync(txt, tmp);
      try {
        // un appel qui ne répond pas en 5 min est abandonné (il sera rejoué au tour suivant)
        const r = await Promise.race([tools.text_to_speech({ file_path: tmp, voice: lot.voix_moteur }),
          new Promise((_, ko) => setTimeout(() => ko(new Error("délai dépassé (300 s)")), 300000))]);
        const p = (r.paths || [])[0];
        if (!p || !fs.existsSync(p)) throw new Error(r.error || "aucun fichier");
        fs.renameSync(p, path.join(d, "rendu.mp3")); res.push({ lot: lot.nom, ok: true });
      } catch (e) { res.push({ lot: lot.nom, ok: false, err: String(e).slice(0, 200) }); }
      journal(res.length + "/" + lots.length);
    }
  }
  await Promise.all(Array.from({ length: concurrence }, ouvrier));
  return res;
}
