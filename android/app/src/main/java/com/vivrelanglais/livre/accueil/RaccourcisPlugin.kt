// android/app/src/main/java/com/vivrelanglais/livre/accueil/RaccourcisPlugin.kt
package com.vivrelanglais.livre.accueil

import android.appwidget.AppWidgetManager
import android.content.ComponentName
import android.content.Intent
import androidx.work.*
import com.getcapacitor.*
import com.getcapacitor.annotation.CapacitorPlugin
import java.util.concurrent.TimeUnit

@CapacitorPlugin(name = "Accueil")
class RaccourcisPlugin : Plugin() {
    override fun load() {
        WorkManager.getInstance(context).enqueueUniquePeriodicWork(
            "expression_du_jour", ExistingPeriodicWorkPolicy.KEEP,
            PeriodicWorkRequestBuilder<Rafraichir>(24, TimeUnit.HOURS).build())
    }

    @PluginMethod
    fun rafraichir(call: PluginCall) { Rafraichir.envoyer(context); call.resolve() }

    class Rafraichir(ctx: android.content.Context, p: WorkerParameters) : Worker(ctx, p) {
        override fun doWork(): Result { envoyer(applicationContext); return Result.success() }
        companion object {
            fun envoyer(ctx: android.content.Context) {
                val gestion = AppWidgetManager.getInstance(ctx)
                val ids = gestion.getAppWidgetIds(ComponentName(ctx, ExpressionDuJour::class.java))
                if (ids.isEmpty()) return
                ctx.sendBroadcast(Intent(AppWidgetManager.ACTION_APPWIDGET_UPDATE)
                    .setClass(ctx, ExpressionDuJour::class.java)
                    .putExtra(AppWidgetManager.EXTRA_APPWIDGET_IDS, ids))
            }
        }
    }
}
