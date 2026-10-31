// android/app/src/direct/java/com/vivrelanglais/livre/voix/FabriqueSource.kt
package com.vivrelanglais.livre.voix

import android.util.Base64
import com.getcapacitor.JSObject
import com.vivrelanglais.livre.BuildConfig
import org.json.JSONObject
import java.io.File
import java.net.HttpURLConnection
import java.net.URL
import java.security.KeyFactory
import java.security.MessageDigest
import java.security.Signature
import java.security.spec.X509EncodedKeySpec
import java.util.concurrent.Executors
import java.util.zip.ZipInputStream

object FabriqueSource { fun creer(p: VoixPlugin): SourceVoix = SourceDirecte(p) }

class SourceDirecte(private val p: VoixPlugin) : SourceVoix {
    private val racine = File(p.context.filesDir, "voix_paquets")
    private val fil = Executors.newSingleThreadExecutor()

    private fun dossier(ch: String) = File(racine, ch)
    override fun etat(chapitre: String): JSObject {
        val d = dossier(chapitre)
        return if (File(d, ".complet").exists()) JSObject().put("etat", "installe").put("base", d.absolutePath)
        else JSObject().put("etat", "absent")
    }

    private fun lire(url: String): ByteArray =
        (URL(url).openConnection() as HttpURLConnection).run {
            connectTimeout = 15_000; readTimeout = 30_000
            inputStream.use { it.readBytes() }
        }

    private fun verifierSignature(donnees: ByteArray, sig: ByteArray) {
        val cle = KeyFactory.getInstance("EC").generatePublic(
            X509EncodedKeySpec(Base64.decode(BuildConfig.CATALOGUE_CLE, Base64.DEFAULT)))
        val v = Signature.getInstance("SHA256withECDSA").apply { initVerify(cle); update(donnees) }
        require(v.verify(sig)) { "catalogue non authentique" }
    }

    override fun faireVenir(chapitre: String, fin: (Throwable?) -> Unit) = fil.execute {
        try {
            val brut = lire(BuildConfig.CATALOGUE_URL)
            verifierSignature(brut, lire(BuildConfig.CATALOGUE_URL + ".sig"))
            val entree = JSONObject(String(brut)).getJSONObject("chapitres").getJSONObject(chapitre)
            val total = entree.getLong("taille")
            val tmp = File(p.context.cacheDir, "voix_$chapitre.zip")
            val sha = MessageDigest.getInstance("SHA-256")
            racine.mkdirs(); require(racine.usableSpace > total * 12 / 10) { "place insuffisante" }
            (URL(entree.getString("url")).openConnection() as HttpURLConnection).apply {
                connectTimeout = 15_000; readTimeout = 30_000
            }.inputStream.use { ins ->
                tmp.outputStream().use { out ->
                    val tampon = ByteArray(64 * 1024); var lu: Int; var cumul = 0L; var dernier = 0L
                    while (ins.read(tampon).also { lu = it } != -1) {
                        out.write(tampon, 0, lu); sha.update(tampon, 0, lu); cumul += lu
                        val maintenant = System.currentTimeMillis()
                        if (maintenant - dernier >= 250) { dernier = maintenant; p.emettre(chapitre, cumul, total, "en_cours") }
                    }
                }
            }
            val empreinte = sha.digest().joinToString("") { "%02x".format(it) }
            require(empreinte == entree.getString("sha256")) { "archive altérée" }
            val d = dossier(chapitre).apply { deleteRecursively(); mkdirs() }
            ZipInputStream(tmp.inputStream()).use { zip ->
                generateSequence { zip.nextEntry }.forEach { e ->
                    val cible = File(d, e.name)
                    require(cible.canonicalPath.startsWith(d.canonicalPath + File.separator)) { "chemin refusé" }
                    if (e.isDirectory) cible.mkdirs() else { cible.parentFile?.mkdirs(); cible.outputStream().use { zip.copyTo(it) } }
                }
            }
            File(d, ".complet").writeText(entree.getString("version"))
            tmp.delete()
            p.emettre(chapitre, total, total, "installe")
            fin(null)
        } catch (t: Throwable) { p.emettre(chapitre, 0, 0, "absent"); fin(t) }
    }

    override fun retirer(chapitre: String) { dossier(chapitre).deleteRecursively() }
}
