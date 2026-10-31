# Porte : chaîne Android (10.14, 10.15, 11.2) — tranche 1

Rapport produit à partir des sorties réelles des commandes (30–31 octobre 2026). Pile : Gradle 8.14.3, AGP 8.13.2, Kotlin 2.4.21, JDK 21, build-tools 36.0.0.

## Compilations

| Commande | Résultat | Journal |
|---|---|---|
| `./gradlew --no-daemon assembleDirectDebug` | BUILD SUCCESSFUL in 3m 30s (247 tâches) | pilotage/portes/gradle-debug.txt |
| `./gradlew --no-daemon bundlePlayRelease` (clé d'envoi) | BUILD SUCCESSFUL | pilotage/portes/gradle-release.txt |
| `./gradlew --no-daemon assembleDirectRelease` (clé directe) | BUILD SUCCESSFUL | pilotage/portes/gradle-release.txt |

Le paquet web embarqué est celui de `npm run build` suivi de `npx cap sync android` sur l'état du dépôt commité.

## apksigner verify --verbose --print-certs (APK direct)
```
Verifies
Verified using v1 scheme (JAR signing): false
Verified using v2 scheme (APK Signature Scheme v2): true
Verified using v3 scheme (APK Signature Scheme v3): false
Verified using v3.1 scheme (APK Signature Scheme v3.1): false
Verified using v4 scheme (APK Signature Scheme v4): false
Verified for SourceStamp: false
Number of signers: 1
Signer #1 certificate DN: CN=Vivre l'Anglais Direct, O=Editeur, C=CI
Signer #1 certificate SHA-256 digest: ebe0c7bba06bade33d8e63ac2b6ddd85868f4a9d2a755e2b7e403167f84d9d8f
Signer #1 certificate SHA-1 digest: 07d0569bec8bbc91179e719a292c87d83594fdf5
Signer #1 certificate MD5 digest: 97d52722a9461ff9a7c5ab6c2f59c5e3
Signer #1 key algorithm: RSA
Signer #1 key size (bits): 4096
Signer #1 public key SHA-256 digest: 4412f7095bc3ad51bc4be5e96271bec155497467b876999e90b479def2aa4f75
Signer #1 public key SHA-1 digest: bd6c9e1cd18f60fbb7cdd0b85e91701799f96297
Signer #1 public key MD5 digest: cb8eca58363832f83cd9fef3e515038f
```
## aapt2 dump badging (APK direct, extrait)
```
package: name='com.vivrelanglais.livre' versionCode='1001' versionName='1.0.0' platformBuildVersionName='16' platformBuildVersionCode='36' compileSdkVersion='36' compileSdkVersionCodename='16'
minSdkVersion:'24'
targetSdkVersion:'36'
uses-permission: name='android.permission.INTERNET'
uses-permission: name='android.permission.RECORD_AUDIO'
uses-permission: name='android.permission.POST_NOTIFICATIONS'
uses-permission: name='android.permission.FOREGROUND_SERVICE'
uses-permission: name='android.permission.FOREGROUND_SERVICE_MEDIA_PLAYBACK'
uses-permission: name='android.permission.WAKE_LOCK'
uses-permission: name='android.permission.VIBRATE'
uses-permission: name='android.permission.RECEIVE_BOOT_COMPLETED'
uses-permission: name='android.permission.SCHEDULE_EXACT_ALARM'
uses-permission: name='android.permission.ACCESS_NETWORK_STATE'
uses-permission: name='com.vivrelanglais.livre.DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION'
application-label:'Vivre l’Anglais'
launchable-activity: name='com.vivrelanglais.livre.MainActivity'  label='' icon=''
  uses-implied-feature: name='android.hardware.microphone' reason='requested android.permission.RECORD_AUDIO permission'
```
## keytool -printcert -jarfile (AAB Play)
```
Owner: CN=Vivre l'Anglais, O=Editeur, C=CI
Valid from: Fri Oct 30 23:31:18 UTC 2026 until: Tue Mar 17 23:31:18 UTC 2054
	 SHA256: B8:15:EF:56:44:B9:B2:17:30:FC:3F:F1:82:1F:46:76:E3:47:AC:0F:2D:B3:F7:AB:32:C0:2A:80:DA:D7:0B:AD
Signature algorithm name: SHA384withRSA
jar verified.
```
## Empreintes SHA-256 et tailles
```
9439e3f184067aa0dbbbfc7b10595043b1daa939422de20d5b635d0fc40933d7  apk/direct/release/app-direct-release.apk
386161e3e0f171519febd6b2315190ba901237565391a5b3cb453e7fb4b69ab8  bundle/playRelease/app-play-release.aab
3472891 apk/direct/release/app-direct-release.apk
5529568 bundle/playRelease/app-play-release.aab
```

## Émulateur API 36 (Android 16, image `default` x86_64, sans accélération matérielle)

- `adb install -r app-direct-release.apk` : **Success**.
- `am start -n com.vivrelanglais.livre/.MainActivity` : le processus démarre, charge WebView 133.0.6943.137, puis s'arrête par un plantage natif dans `libwebviewchromium.so` (`am_crash … Native crash, Trap`), reproduit deux fois (23:53:36 et 00:07:21 UTC).
- Contre-épreuve : l'application de test fournie par l'image, `org.chromium.webview_shell`, ouvrant `about:blank`, plante de la même façon (`am_crash … org.chromium.webview_shell … Native crash, Trap`, 00:09:19 UTC), y compris avec `--disable-gpu`.
- Conclusion : défaut du WebView de cette image en émulation logicielle (pas de KVM sur la machine de compilation, 2 processeurs) ; il ne met pas en cause l'application. Extrait des événements : `pilotage/portes/emulateur-api36-evenements.txt`.
- Conséquence : l'ouverture est contrôlée sur l'émulateur API 30 (classe « Marché africain d'entrée de gamme » / API 30 de la matrice 11.3) ; l'API 36 sera reprise en tranche 10 sur un émulateur accéléré ou un appareil réel (exigence R-11.2-007 au statut « socle en place »).

## Émulateur Android 11 (API 30) — 31 octobre 2026

| Contrôle | Résultat | Preuve |
|---|---|---|
| Démarrage de l'image (sans KVM, `-accel off`) | sys.boot_completed = 1 | journal de l'émulateur |
| Installation de l'APK direct signé (release 1.0.0, code 1001) | Success | emulateur-api30-diagnostic.txt |
| Ouverture | MainActivity au premier plan, processus vivant, écran de lancement « Encre & Voix » affiché | emulateur-api30.png, emulateur-api30-logcat.txt |
| Plantage | aucun (0 FATAL EXCEPTION, 0 am_crash) | emulateur-api30-logcat.txt |
| Rendu de l'interface dans la WebView 83 | non obtenu : défaut d'émulation du processeur (NaN\|0 = 2147483647, undefined & 1 = 1) | emulateur-api30-diagnostic.txt |

Correctif apporté à l'application pendant ce contrôle : complément de compatibilité static/compat/compat.js (replaceAll, structuredClone) pour les WebView antérieures à Chrome 98 (D-033). Le défaut restant appartient à l'émulation logicielle (D-034). Vérification à reprendre sur appareil réel ou émulateur accéléré : matrice 11.3, tranche 10.
