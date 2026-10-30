// app/capacitor.config.ts
import type { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.vivrelanglais.livre',
  appName: "Vivre l'Anglais",
  webDir: 'build',
  android: {
    path: '../android',
    allowMixedContent: false,
    captureInput: false
  },
  plugins: {
    SplashScreen: { launchAutoHide: false, backgroundColor: '#FBF8F3', showSpinner: false },
    LocalNotifications: { smallIcon: 'ic_stat_plume', iconColor: '#1F3A5F' }
  }
};
export default config;
