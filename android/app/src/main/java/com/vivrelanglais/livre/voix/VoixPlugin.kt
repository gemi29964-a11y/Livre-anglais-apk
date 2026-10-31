// android/app/src/main/java/com/vivrelanglais/livre/voix/VoixPlugin.kt
package com.vivrelanglais.livre.voix

import com.getcapacitor.*
import com.getcapacitor.annotation.CapacitorPlugin

interface SourceVoix {
    fun etat(chapitre: String): JSObject
    fun faireVenir(chapitre: String, fin: (Throwable?) -> Unit)
    fun retirer(chapitre: String)
}

@CapacitorPlugin(name = "Voix")
class VoixPlugin : Plugin() {
    private lateinit var source: SourceVoix

    override fun load() { source = FabriqueSource.creer(this) }   // définie par saveur (play / direct)

    fun emettre(chapitre: String, octets: Long, total: Long, etat: String) {
        notifyListeners("progression", JSObject()
            .put("chapitre", chapitre).put("octets", octets).put("total", total).put("etat", etat))
    }

    @PluginMethod
    fun etat(call: PluginCall) {
        val ch = call.getString("chapitre") ?: return call.reject("chapitre manquant")
        call.resolve(source.etat(ch))
    }

    @PluginMethod
    fun faireVenir(call: PluginCall) {
        val ch = call.getString("chapitre") ?: return call.reject("chapitre manquant")
        source.faireVenir(ch) { e -> if (e == null) call.resolve() else call.reject(e.message ?: "contretemps") }
    }

    @PluginMethod
    fun retirer(call: PluginCall) {
        val ch = call.getString("chapitre") ?: return call.reject("chapitre manquant")
        source.retirer(ch); call.resolve()
    }
}
