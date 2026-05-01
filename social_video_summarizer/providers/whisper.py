"""Whisper transcription provider."""

from __future__ import annotations

from pathlib import Path


class WhisperTranscriber:
    """Transcribe audio or video files using local Whisper."""

    def __init__(self, model_name: str = "base") -> None:
        try:
            import whisper
        except ImportError as exc:
            raise ImportError(
                "Install Whisper dependencies with `pip install social-video-summarizer[whisper]`."
            ) from exc
        self.model = whisper.load_model(model_name)

    def transcribe(self, media_path: str | Path) -> str:
        result = self.model.transcribe(str(media_path))
        return result.get("text", "").strip()

