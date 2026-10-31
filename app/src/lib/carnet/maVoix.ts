// « Ma voix » (8.8, 10.10) : enregistrements du lecteur dans Directory.Data/ma_voix/{id}-{horodatage}.m4a.
// Jamais dans la sauvegarde en ligne (res/xml/extraction_donnees.xml) ; effaçables en un geste.
import { Directory, Filesystem } from '@capacitor/filesystem';

export const DOSSIER = 'ma_voix';

export interface Enregistrement { nom: string; expression: string; date: number }

export function decoder(nom: string): Enregistrement | null {
  const m = /^(.+)-(\d{10,})\.m4a$/.exec(nom);
  return m ? { nom, expression: m[1], date: Number(m[2]) } : null;
}

export async function lister(): Promise<Enregistrement[]> {
  try {
    const { files } = await Filesystem.readdir({ path: DOSSIER, directory: Directory.Data });
    return files.map((f) => decoder(f.name)).filter((e): e is Enregistrement => e !== null).sort((a, b) => b.date - a.date);
  } catch {
    return [];                                          // dossier pas encore créé : aucun enregistrement
  }
}

export async function toutEffacer(): Promise<void> {
  try {
    await Filesystem.rmdir({ path: DOSSIER, directory: Directory.Data, recursive: true });
  } catch {
    /* rien à effacer */
  }
}
