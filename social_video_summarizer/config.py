"""Configuration objects for video summarization."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

KeyframeStrategy = Literal["scene", "interval", "uniform", "manual", "none"]


@dataclass(frozen=True)
class KeyframeConfig:
    """Screenshot/keyframe extraction configuration."""

    strategy: KeyframeStrategy = "scene"
    max_keyframes: int = 8
    include_first_last: bool = True
    scene_threshold: float = 3.5
    interval_seconds: float = 2.0
    min_seconds_between_frames: float = 1.0
    output_dir: str = "outputs/keyframes"


@dataclass(frozen=True)
class SummarizerConfig:
    """Top-level summarizer configuration."""

    keyframes: KeyframeConfig = KeyframeConfig()
    keep_intermediate_files: bool = True
    audio_output_dir: str = "outputs/audio"


def coerce_keyframe_config(value: KeyframeConfig | dict | None) -> KeyframeConfig:
    """Coerce a user dictionary into `KeyframeConfig`."""

    if value is None:
        return KeyframeConfig()
    if isinstance(value, KeyframeConfig):
        return value
    return KeyframeConfig(**value)

