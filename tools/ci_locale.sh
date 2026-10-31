#!/usr/bin/env bash
# Exécute localement, dans l'ordre, les étapes des flux .github/workflows/contenu.yml et android.yml (10.16).
# Équivalent de l'intégration continue lorsque les exécuteurs GitHub ne sont pas disponibles.
# Variables attendues pour la signature : VA_ENVOI_JKS, VA_ENVOI_MDP, VA_DIRECT_JKS, VA_DIRECT_MDP.
# Usage : tools/ci_locale.sh [numéro d'exécution]   — sortie : pilotage/portes/ci-locale.txt
set -euo pipefail
RACINE="$(cd "$(dirname "$0")/.." && pwd)"
cd "$RACINE"
N="${1:-1}"
etape() { printf '\n=== %s — %s ===\n' "$(date -u +%H:%M:%S)" "$1"; }

etape "contenu : tests des outils"
python3 -m pytest -q tools/tests
etape "contenu : validations du corpus (--strict)"
python3 tools/valider_corpus.py --strict
etape "contenu : lexique"
python3 tools/lexique_verifier.py
etape "contenu : phrasé"
python3 tools/phrase_verifier.py

etape "android : voix (récupération)"
python3 tools/voix_recuperer.py --tout
etape "android : construire --strict"
python3 tools/construire.py --strict
etape "android : socle des voix et paquets"
python3 tools/voix_recuperer.py --socle && python3 tools/generer_paquets.py

etape "android : application web (ci, check, test, build, e2e, cap sync)"
( cd app && npm ci && npm run check && npm run test && npm run build && npm run e2e && npx cap sync android )

export VA_VERSION_CODE=$((1000 + N))
export VA_VERSION_NAME="${VA_VERSION_NAME:-1.0.$((N - 1))}"
etape "android : bundle Play (versionCode $VA_VERSION_CODE)"
( cd android && VA_KEYSTORE="$VA_ENVOI_JKS" VA_KEYSTORE_MDP="$VA_ENVOI_MDP" VA_CLE_ALIAS=envoi VA_CLE_MDP="$VA_ENVOI_MDP" \
  ./gradlew --no-daemon -q bundlePlayRelease )
etape "android : APK direct"
( cd android && VA_KEYSTORE="$VA_DIRECT_JKS" VA_KEYSTORE_MDP="$VA_DIRECT_MDP" VA_CLE_ALIAS=direct VA_CLE_MDP="$VA_DIRECT_MDP" \
  ./gradlew --no-daemon -q assembleDirectRelease )

etape "android : vérifier"
APK=android/app/build/outputs/apk/direct/release/app-direct-release.apk
AAB=android/app/build/outputs/bundle/playRelease/app-play-release.aab
"$ANDROID_HOME/build-tools/36.0.0/apksigner" verify --print-certs "$APK" | grep -v '^WARNING'
jarsigner -verify "$AAB" | grep -i verified
sha256sum "$APK" "$AAB"
etape "terminé : toutes les étapes ont réussi"
