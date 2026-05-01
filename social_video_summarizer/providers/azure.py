"""Azure Speech-to-Text provider."""

from __future__ import annotations

from pathlib import Path


class AzureSpeechTranscriber:
    """Transcribe media with Azure Speech-to-Text."""

    def __init__(self, speech_key: str | None = None, service_region: str | None = None) -> None:
        try:
            import azure.cognitiveservices.speech as speechsdk
        except ImportError as exc:
            raise ImportError(
                "Install Azure dependencies with `pip install social-video-summarizer[azure]`."
            ) from exc
        self.speechsdk = speechsdk
        self.speech_key = speech_key
        self.service_region = service_region

    def transcribe(self, audio_path: str | Path) -> str:
        if not self.speech_key or not self.service_region:
            raise ValueError("AzureSpeechTranscriber requires speech_key and service_region.")

        speech_config = self.speechsdk.SpeechConfig(
            subscription=self.speech_key,
            region=self.service_region,
        )
        audio_config = self.speechsdk.audio.AudioConfig(filename=str(audio_path))
        recognizer = self.speechsdk.SpeechRecognizer(
            speech_config=speech_config,
            audio_config=audio_config,
        )
        result = recognizer.recognize_once()
        return result.text

