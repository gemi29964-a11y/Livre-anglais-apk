// android/app/src/main/java/com/vivrelanglais/livre/promenade/PromenadePlugin.kt
package com.vivrelanglais.livre.promenade

import android.content.ComponentName
import androidx.media3.common.MediaItem
import androidx.media3.common.MediaMetadata
import androidx.media3.session.MediaController
import androidx.media3.session.SessionToken
import com.getcapacitor.*
import com.getcapacitor.annotation.CapacitorPlugin
import com.google.common.util.concurrent.MoreExecutors

@CapacitorPlugin(name = "Promenade")
class PromenadePlugin : Plugin() {
    private var controleur: MediaController? = null

    private fun avecControleur(action: (MediaController) -> Unit) {
        controleur?.let { return action(it) }
        val jeton = SessionToken(context, ComponentName(context, PromenadeService::class.java))
        val futur = MediaController.Builder(context, jeton).buildAsync()
        futur.addListener({ controleur = futur.get(); action(controleur!!) }, MoreExecutors.directExecutor())
    }

    /** elements: [{ url, titre, sousTitre }] ou [{ silenceMs }] */
    @PluginMethod
    fun demarrer(call: PluginCall) {
        val elements = call.getArray("elements") ?: return call.reject("elements manquants")
        val items = (0 until elements.length()).map { i ->
            val e = elements.getJSONObject(i)
            if (e.has("silenceMs")) {
                MediaItem.Builder().setUri("silence://${e.getLong("silenceMs")}").setMediaId("silence-$i").build()
            } else {
                MediaItem.Builder()
                    .setUri(e.getString("url"))
                    .setMediaId(e.optString("id", "item-$i"))
                    .setMediaMetadata(MediaMetadata.Builder()
                        .setTitle(e.optString("titre"))
                        .setArtist(e.optString("sousTitre", "Vivre l'Anglais"))
                        .build())
                    .build()
            }
        }
        avecControleur { c -> c.setMediaItems(items); c.prepare(); c.play(); call.resolve() }
    }

    @PluginMethod fun pause(call: PluginCall) = avecControleur { it.pause(); call.resolve() }
    @PluginMethod fun reprendre(call: PluginCall) = avecControleur { it.play(); call.resolve() }
    @PluginMethod fun arreter(call: PluginCall) = avecControleur { it.stop(); it.clearMediaItems(); call.resolve() }
    @PluginMethod fun suivant(call: PluginCall) = avecControleur { it.seekToNextMediaItem(); call.resolve() }
    @PluginMethod fun precedent(call: PluginCall) = avecControleur { it.seekToPreviousMediaItem(); call.resolve() }
}
