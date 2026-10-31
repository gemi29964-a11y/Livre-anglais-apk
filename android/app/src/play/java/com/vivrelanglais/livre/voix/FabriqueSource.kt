// android/app/src/play/java/com/vivrelanglais/livre/voix/FabriqueSource.kt
package com.vivrelanglais.livre.voix

import androidx.activity.result.ActivityResultLauncher
import androidx.activity.result.IntentSenderRequest
import com.getcapacitor.JSObject
import com.google.android.play.core.assetpacks.AssetPackManagerFactory
import com.google.android.play.core.assetpacks.AssetPackStateUpdateListener
import com.google.android.play.core.assetpacks.model.AssetPackStatus

object FabriqueSource { fun creer(p: VoixPlugin): SourceVoix = SourcePlay(p) }

class SourcePlay(private val p: VoixPlugin) : SourceVoix {
    private val gestion = AssetPackManagerFactory.getInstance(p.context)
    private val attentes = mutableMapOf<String, (Throwable?) -> Unit>()
    // Le lanceur est enregistré par MainActivity avant son démarrage (exigence d'AndroidX Activity)
    private val confirmation: ActivityResultLauncher<IntentSenderRequest>
        get() = (p.activity as com.vivrelanglais.livre.MainActivity).confirmationPaquets

    private val ecoute = AssetPackStateUpdateListener { s ->
        val ch = s.name().removePrefix("voix_")
        val etat = when (s.status()) {
            AssetPackStatus.COMPLETED -> "installe"
            AssetPackStatus.FAILED, AssetPackStatus.CANCELED -> "absent"
            AssetPackStatus.WAITING_FOR_WIFI, AssetPackStatus.REQUIRES_USER_CONFIRMATION -> "confirmation"
            else -> "en_cours"
        }
        p.emettre(ch, s.bytesDownloaded(), s.totalBytesToDownload(), etat)
        if (etat == "confirmation") gestion.showConfirmationDialog(confirmation)
        if (etat == "installe") attentes.remove(ch)?.invoke(null)
        if (s.status() == AssetPackStatus.FAILED) attentes.remove(ch)?.invoke(IllegalStateException("code ${s.errorCode()}"))
    }
    init { gestion.registerListener(ecoute) }

    override fun etat(chapitre: String): JSObject {
        val lieu = gestion.getPackLocation("voix_$chapitre")
        return if (lieu?.assetsPath() != null) JSObject().put("etat", "installe").put("base", lieu.assetsPath())
        else JSObject().put("etat", "absent")
    }
    override fun faireVenir(chapitre: String, fin: (Throwable?) -> Unit) {
        attentes[chapitre] = fin
        gestion.fetch(listOf("voix_$chapitre"))
    }
    override fun retirer(chapitre: String) { gestion.removePack("voix_$chapitre") }
}
