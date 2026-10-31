// android/app/src/main/java/com/vivrelanglais/livre/accueil/ExpressionDuJour.kt
package com.vivrelanglais.livre.accueil

import android.app.PendingIntent
import android.appwidget.AppWidgetManager
import android.appwidget.AppWidgetProvider
import android.content.Context
import android.content.Intent
import android.net.Uri
import android.widget.RemoteViews
import com.vivrelanglais.livre.R
import org.json.JSONObject
import java.io.File

class ExpressionDuJour : AppWidgetProvider() {
    override fun onUpdate(ctx: Context, gestion: AppWidgetManager, ids: IntArray) {
        val e = choisir(ctx) ?: return
        for (id in ids) {
            val vues = RemoteViews(ctx.packageName, R.layout.expression_du_jour).apply {
                setTextViewText(R.id.enonce, e.getString("en"))
                setTextViewText(R.id.sens, e.getString("sens"))
                setTextViewText(R.id.accent, if (e.getString("accent") == "uk") "Brit." else "Am.")
                setOnClickPendingIntent(R.id.enonce, ouvrir(ctx, "vivrelanglais://expression/${e.getString("id")}?ecouter=1", 1))
                setOnClickPendingIntent(R.id.cadre, ouvrir(ctx, "vivrelanglais://expression/${e.getString("id")}", 2))
            }
            gestion.updateAppWidget(id, vues)
        }
    }

    /** Lit la liste écrite par l'application (files/accueil/expressions.json) ; une expression par jour, bascule à 4 h. */
    private fun choisir(ctx: Context): JSONObject? {
        val f = File(ctx.filesDir, "accueil/expressions.json")
        if (!f.exists()) return null
        val liste = JSONObject(f.readText()).getJSONArray("expressions")
        if (liste.length() == 0) return null
        val jour = (System.currentTimeMillis() + java.util.TimeZone.getDefault().getOffset(System.currentTimeMillis()) - 4 * 3_600_000L) / 86_400_000L
        return liste.getJSONObject((jour % liste.length()).toInt())
    }

    private fun ouvrir(ctx: Context, adresse: String, code: Int) = PendingIntent.getActivity(
        ctx, code, Intent(Intent.ACTION_VIEW, Uri.parse(adresse)).setPackage(ctx.packageName),
        PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE)
}
