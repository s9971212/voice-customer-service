import librosa
import numpy as np
from faster_whisper import WhisperModel

from ..config import settings


class WhisperASR:

    def __init__(self):

        # =========================
        # Whisper Model
        # =========================

        self.model = WhisperModel(
            model_size_or_path=settings.model_size_or_path,
            device=settings.device,
            compute_type=settings.compute_type,
            download_root=settings.model_dir,
        )

    def transcribe(self, audio_file):
        """
        語音轉文字
        """

        orig_audio, orig_sr = librosa.load(
            audio_file,
            sr=None,
            mono=False
        )

        processed_audio = self._preprocess(orig_audio, orig_sr)

        segments, _ = self.model.transcribe(
            audio=processed_audio,
            language=settings.language,
            beam_size=settings.beam_size,
            vad_filter=settings.vad_filter
        )

        text = "".join(
            seg.text
            for seg in segments
        ).strip()

        return processed_audio, text

    @staticmethod
    def _preprocess(audio, orig_sr, target_peak=settings.target_peak, max_gain=settings.max_gain):
        """
        語音預處理
        """

        if audio.ndim > 1:
            audio = np.mean(audio, axis=1)

        audio = audio.astype(np.float32)

        peak = np.max(np.abs(audio)) + 1e-12
        gain = min(target_peak / peak, max_gain)

        audio *= gain
        audio = np.clip(audio, -1.0, 1.0)

        if orig_sr != settings.target_sr:
            audio = librosa.resample(
                audio,
                orig_sr=orig_sr,
                target_sr=settings.target_sr
            )

        return audio.astype(np.float32)
