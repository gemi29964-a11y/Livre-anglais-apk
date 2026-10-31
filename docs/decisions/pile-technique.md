# Pile technique — versions retenues (10.2, règle de gel)

Vérification faite le 30 octobre 2026 ; versions figées dans app/package-lock.json, android/variables.gradle, android/build.gradle et tools/requirements.txt. Décision D-001 du journal.

## Outillage

| Outil | Version installée et utilisée |
|---|---|
| Node.js | v22.23.4 |
| npm | 10.9.9 |
| JDK | openjdk version "21.0.12.1" 2026-08-18 |
| Python | Python 3.12.15 (environnement .venv ; la CI utilise 3.12) |
| ffmpeg | ffmpeg version 8.0.1-3ubuntu2 |
| Gradle (wrapper) | 8.14.3 |
| Android Gradle Plugin | 8.13.2 |
| Kotlin | 2.4.21 |
| build-tools | 36.0.0 |
| SDK | minSdk 24, compileSdk 36, targetSdk 36 |

## Application web (app/package.json)

```json
{
  "dependencies": {
    "@capacitor/android": "^8.6.0",
    "@capacitor/app": "^8.1.2",
    "@capacitor/core": "^8.6.0",
    "@capacitor/filesystem": "^8.1.5",
    "@capacitor/haptics": "^8.0.2",
    "@capacitor/local-notifications": "^8.3.1",
    "@capacitor/preferences": "^8.0.1",
    "@capacitor/share": "^8.0.3",
    "@capacitor/splash-screen": "^8.0.2",
    "@capacitor/status-bar": "^8.0.4",
    "@capgo/capacitor-audio-recorder": "^8.3.5",
    "dexie": "^4.4.7",
    "minisearch": "^7.2.0",
    "ts-fsrs": "^5.4.2"
  },
  "devDependencies": {
    "@axe-core/playwright": "^4.14.0",
    "@capacitor/assets": "^4.0.0",
    "@capacitor/cli": "^8.6.0",
    "@playwright/test": "^1.64.1",
    "@sveltejs/adapter-static": "^3.0.10",
    "@sveltejs/kit": "^2.70.3",
    "@sveltejs/vite-plugin-svelte": "^7.3.1",
    "@testing-library/jest-dom": "^7.0.1",
    "@testing-library/svelte": "^5.4.2",
    "@vitest/coverage-v8": "^5.0.5",
    "fake-indexeddb": "^6.2.7",
    "jsdom": "^30.1.3",
    "svelte": "^5.57.3",
    "svelte-check": "^4.7.7",
    "typescript": "^5.9.3",
    "vite": "^8.3.5",
    "vitest": "^5.0.5"
  }
}
```

## Android (android/variables.gradle)

```
    minSdkVersion = 24
    compileSdkVersion = 36
    targetSdkVersion = 36
    androidxActivityVersion = '1.11.0'
    androidxAppCompatVersion = '1.7.1'
    androidxCoordinatorLayoutVersion = '1.3.0'
    androidxCoreVersion = '1.17.0'
    androidxFragmentVersion = '1.8.9'
    coreSplashScreenVersion = '1.2.0'
    androidxWebkitVersion = '1.14.0'
    junitVersion = '4.13.2'
    androidxJunitVersion = '1.3.0'
    androidxEspressoCoreVersion = '3.7.0'
    cordovaAndroidVersion = '14.0.1'
    media3Version = '1.11.1'          // dernière 1.x stable
    assetDeliveryVersion = '2.3.0'    // dernière 2.x stable
    workVersion = '2.12.0'            // WorkManager : expression du jour, vérification mensuelle des voix
    kotlinVersion = '2.4.21'
```

## Outils Python (tools/requirements.txt)

```
pyyaml==6.0.3
jsonschema==4.26.0
boto3==1.43.123
praat-parselmouth==0.4.7
numpy==2.5.4
Pillow==13.0.0
fonttools==4.68.0
brotli==1.2.1
pytest==9.2.0
ffmpeg-normalize==1.43.0
```
