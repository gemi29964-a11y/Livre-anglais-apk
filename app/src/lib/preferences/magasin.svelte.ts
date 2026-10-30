// État réactif des Préférences, enregistré par @capacitor/preferences (stockage privé, 10.10).
import { Preferences as Stockage } from '@capacitor/preferences';
import { DEFAUT, lire, type Preferences } from './modele';

const CLE = 'preferences';

class Magasin {
  valeur = $state<Preferences>(structuredClone(DEFAUT));
  pret = $state(false);

  async ouvrir(): Promise<void> {
    try {
      const { value } = await Stockage.get({ key: CLE });
      this.valeur = lire(value ? JSON.parse(value) : {});
    } catch {
      this.valeur = structuredClone(DEFAUT);
    }
    this.pret = true;
  }

  async changer(modif: Partial<Preferences>): Promise<void> {
    this.valeur = lire({ ...$state.snapshot(this.valeur), ...modif });
    await Stockage.set({ key: CLE, value: JSON.stringify($state.snapshot(this.valeur)) });
  }
}

export const preferences = new Magasin();
