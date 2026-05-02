"""Provider protocols."""

from __future__ import annotations

from pathlib import Path
from typing import Protocol


class TranscriptionProvider(Protocol):
    def transcribe(self, media_path: str | Path) -> str:
        """Return transcript text for an audio or video file."""


class SummaryProvider(Protocol):
    def summarize(self, *, summary_input: str, keyframes: list[str], metadata) -> str:
        """Return a video summary."""

