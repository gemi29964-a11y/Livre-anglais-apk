// android/app/src/main/java/com/vivrelanglais/livre/promenade/PromenadeService.kt
package com.vivrelanglais.livre.promenade

import androidx.annotation.OptIn
import androidx.media3.common.AudioAttributes
import androidx.media3.common.C
import androidx.media3.common.util.UnstableApi
import androidx.media3.exoplayer.ExoPlayer
import androidx.media3.exoplayer.source.DefaultMediaSourceFactory
import androidx.media3.exoplayer.source.MediaSource
import androidx.media3.exoplayer.source.SilenceMediaSource
import androidx.media3.session.MediaSession
import androidx.media3.session.MediaSessionService

@OptIn(UnstableApi::class)
class PromenadeService : MediaSessionService() {
    private var session: MediaSession? = null

    override fun onCreate() {
        super.onCreate()
        val defaut = DefaultMediaSourceFactory(this)
        val fabrique = object : MediaSource.Factory by defaut {
            override fun createMediaSource(item: androidx.media3.common.MediaItem): MediaSource {
                val uri = item.localConfiguration?.uri?.toString().orEmpty()
                return if (uri.startsWith("silence://"))
                    SilenceMediaSource(uri.removePrefix("silence://").toLong() * 1000) // microsecondes
                else defaut.createMediaSource(item)
            }
        }
        val lecteur = ExoPlayer.Builder(this)
            .setMediaSourceFactory(fabrique)
            .setAudioAttributes(AudioAttributes.Builder()
                .setUsage(C.USAGE_MEDIA).setContentType(C.AUDIO_CONTENT_TYPE_SPEECH).build(), true) // gère le focus audio
            .setHandleAudioBecomingNoisy(true)   // pause au débranchement du casque
            .build()
        session = MediaSession.Builder(this, lecteur).build()
    }

    override fun onGetSession(info: MediaSession.ControllerInfo) = session

    override fun onDestroy() {
        session?.run { player.release(); release() }
        session = null
        super.onDestroy()
    }
}
