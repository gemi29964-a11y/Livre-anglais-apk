# Porte — budgets mesurables en tranche 1 (10.12)

Mesures faites le 31 octobre 2026 sur les produits de compilation de ce commit.

| Mesure | Budget 10.12 | Mesuré | Verdict |
|---|---|---|---|
| JavaScript initial compressé (gzip -9 : modules préchargés par index.html, entrée, compat.js) | ≤ 150 Ko | 52,7 Kio (18 fichiers) ; avec la page d'accueil (nœud 2) : 54,3 Kio | conforme |
| APK direct | ≤ 240 Mo | 3 474 699 octets (3,3 Mio) | conforme |
| Module de base Play (AAB complet) | ≤ 240 Mo | 5 531 480 octets (5,3 Mio) | conforme |
| Démarrage à froid, ouverture de scène, latences du son, défilement, mémoire | voir 10.12 | non mesurables ici : ils exigent l'appareil de référence (Galaxy A15 ou équivalent) et le contenu | reportés en tranche 10 (matrice 11.3) |

Ces chiffres de tranche 1 précèdent le corpus et les voix ; les budgets seront remesurés à chaque tranche.
