"""Audio extraction helpers."""

from __future__ import annotations

from pathlib import Path


def extract_audio(video_path: str | Path, output_path: str | Path) -> Path:
    """Extract audio from a video file."""

    try:
        from moviepy.editor import VideoFileClip
    except ImportError as exc:
        raise ImportError(
            "Install video dependencies with `pip install social-video-summarizer[video]`."
        ) from exc

    video_path = Path(video_path)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with VideoFileClip(str(video_path)) as clip:
        if clip.audio is None:
            raise ValueError(f"No audio stream found in {video_path}.")
        clip.audio.write_audiofile(str(output_path), verbose=False, logger=None)
    return output_path

