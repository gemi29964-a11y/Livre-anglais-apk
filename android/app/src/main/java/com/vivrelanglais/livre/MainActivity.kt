package com.vivrelanglais.livre

import android.os.Bundle
import androidx.activity.result.ActivityResultLauncher
import androidx.activity.result.IntentSenderRequest
import androidx.activity.result.contract.ActivityResultContracts
import com.getcapacitor.BridgeActivity
import com.vivrelanglais.livre.accueil.RaccourcisPlugin
import com.vivrelanglais.livre.promenade.PromenadePlugin
import com.vivrelanglais.livre.voix.VoixPlugin

class MainActivity : BridgeActivity() {
    /** Confirmation d'un téléchargement de paquet sur réseau mobile (enregistré avant STARTED). */
    val confirmationPaquets: ActivityResultLauncher<IntentSenderRequest> =
        registerForActivityResult(ActivityResultContracts.StartIntentSenderForResult()) { }

    override fun onCreate(savedInstanceState: Bundle?) {
        registerPlugin(VoixPlugin::class.java)
        registerPlugin(PromenadePlugin::class.java)
        registerPlugin(RaccourcisPlugin::class.java)
        super.onCreate(savedInstanceState)
    }
}
