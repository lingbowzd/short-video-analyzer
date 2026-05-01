"""Main public summarizer API."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .config import KeyframeConfig, SummarizerConfig, coerce_keyframe_config
from .prompts import build_summary_input
from .result import SummaryResult


@dataclass
class VideoMetadata:
    """Metadata commonly available for short-form social videos."""

    duration: float | None = None
    description: str | None = None
    hashtags: list[str] | None = None
    subtitle: str | None = None
    sticker_text: str | None = None
    transcript: str | None = None
    music_title: str | None = None
    music_author: str | None = None
    manual_keyframes: list[str] | None = None


class SocialVideoSummarizer:
    """Efficient, metadata-aware summarizer for short-form social videos."""

    def __init__(
        self,
        *,
        keyframes: KeyframeConfig | dict | None = None,
        transcriber: Any | None = None,
        summary_provider: Any | None = None,
        config: SummarizerConfig | None = None,
    ) -> None:
        keyframe_config = coerce_keyframe_config(keyframes)
        self.config = config or SummarizerConfig(keyframes=keyframe_config)
        self.transcriber = transcriber
        self.summary_provider = summary_provider

    def summarize(
        self,
        video_path: str | Path | None = None,
        *,
        duration: float | None = None,
        description: str | None = None,
        hashtags: list[str] | None = None,
        subtitle: str | None = None,
        sticker_text: str | None = None,
        transcript: str | None = None,
        music_title: str | None = None,
        music_author: str | None = None,
        manual_keyframes: list[str] | None = None,
    ) -> SummaryResult:
        """Summarize a short-form social video.

        If no summary provider is configured, this returns a structured
        `SummaryResult` with the formatted summary input and processing metadata.
        """

        metadata = VideoMetadata(
            duration=duration,
            description=description,
            hashtags=hashtags,
            subtitle=subtitle,
            sticker_text=sticker_text,
            transcript=transcript,
            music_title=music_title,
            music_author=music_author,
            manual_keyframes=manual_keyframes,
        )

        transcript = transcript or self._maybe_transcribe(video_path)
        keyframes = self._maybe_extract_keyframes(video_path, metadata)

        summary_input = build_summary_input(
            duration=duration,
            description=description,
            hashtags=hashtags,
            subtitle=subtitle,
            sticker_text=sticker_text,
            transcript=transcript,
            music_title=music_title,
            music_author=music_author,
        )

        summary = None
        if self.summary_provider is not None and hasattr(self.summary_provider, "summarize"):
            summary = self.summary_provider.summarize(
                summary_input=summary_input,
                keyframes=keyframes,
                metadata=metadata,
            )

        return SummaryResult(
            summary=summary,
            summary_input=summary_input,
            transcript=transcript,
            keyframes=[str(path) for path in keyframes],
            metadata_used={
                "description": bool(description),
                "hashtags": bool(hashtags),
                "subtitle": bool(subtitle),
                "sticker_text": bool(sticker_text),
                "transcript": bool(transcript),
                "music": bool(music_title or music_author),
                "keyframes": bool(keyframes),
            },
            processing={
                "keyframe_strategy": self.config.keyframes.strategy,
                "max_keyframes": self.config.keyframes.max_keyframes,
                "summary_provider": _provider_name(self.summary_provider),
                "transcriber": _provider_name(self.transcriber),
            },
        )

    def _maybe_transcribe(self, video_path: str | Path | None) -> str | None:
        if video_path is None or self.transcriber is None:
            return None
        if hasattr(self.transcriber, "transcribe_video"):
            return self.transcriber.transcribe_video(video_path)
        if hasattr(self.transcriber, "transcribe"):
            return self.transcriber.transcribe(video_path)
        return None

    def _maybe_extract_keyframes(
        self,
        video_path: str | Path | None,
        metadata: VideoMetadata,
    ) -> list[Path | str]:
        config = self.config.keyframes
        if config.strategy == "manual":
            return metadata.manual_keyframes or []
        if config.strategy == "none" or video_path is None:
            return []

        from .video.keyframes import extract_keyframes

        return extract_keyframes(
            video_path,
            output_dir=config.output_dir,
            config=config,
            duration_seconds=metadata.duration,
        )


def _provider_name(provider: Any | None) -> str | None:
    if provider is None:
        return None
    return provider.__class__.__name__
