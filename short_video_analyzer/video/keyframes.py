"""Configurable keyframe extraction."""

from __future__ import annotations

from pathlib import Path

from ..config import KeyframeConfig


def extract_keyframes(
    video_path: str | Path,
    *,
    output_dir: str | Path,
    config: KeyframeConfig,
    duration_seconds: float | None = None,
) -> list[Path]:
    """Extract compact keyframes according to the configured strategy."""

    if config.strategy == "scene":
        return extract_scene_keyframes(video_path, output_dir, config=config)
    if config.strategy in {"interval", "uniform"}:
        return extract_sampled_keyframes(video_path, output_dir, config=config)
    if config.strategy == "none":
        return []
    raise ValueError(f"Unsupported keyframe strategy: {config.strategy}")


def extract_scene_keyframes(
    video_path: str | Path,
    output_dir: str | Path,
    *,
    config: KeyframeConfig,
) -> list[Path]:
    """Extract scene-change keyframes with PySceneDetect."""

    try:
        import cv2
        from scenedetect import AdaptiveDetector, SceneManager, open_video
    except ImportError as exc:
        raise ImportError(
            "Install video dependencies with `pip install short-video-analyzer[video]`."
        ) from exc

    video_path = Path(video_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    video = open_video(str(video_path))
    scene_manager = SceneManager()
    scene_manager.add_detector(AdaptiveDetector(adaptive_threshold=config.scene_threshold))
    scene_manager.detect_scenes(video)
    scenes = scene_manager.get_scene_list()

    capture = cv2.VideoCapture(str(video_path))
    fps = capture.get(cv2.CAP_PROP_FPS) or 30
    total_frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT) or 0)

    frame_numbers: set[int] = set()
    if config.include_first_last and total_frames > 0:
        frame_numbers.update({0, max(total_frames - 1, 0)})

    for start, end in scenes:
        midpoint_seconds = (start.get_seconds() + end.get_seconds()) / 2
        frame_numbers.add(max(0, int(midpoint_seconds * fps)))

    return _write_frames(capture, sorted(frame_numbers)[: config.max_keyframes], output_dir)


def extract_sampled_keyframes(
    video_path: str | Path,
    output_dir: str | Path,
    *,
    config: KeyframeConfig,
) -> list[Path]:
    """Extract interval or uniformly sampled keyframes."""

    try:
        import cv2
        import numpy as np
    except ImportError as exc:
        raise ImportError(
            "Install video dependencies with `pip install short-video-analyzer[video]`."
        ) from exc

    video_path = Path(video_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    capture = cv2.VideoCapture(str(video_path))
    fps = capture.get(cv2.CAP_PROP_FPS) or 30
    total_frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT) or 0)
    if total_frames <= 0:
        return []

    if config.strategy == "interval":
        step = max(int(config.interval_seconds * fps), 1)
        frame_numbers = list(range(0, total_frames, step))
    else:
        frame_numbers = np.linspace(0, total_frames - 1, num=config.max_keyframes, dtype=int).tolist()

    if config.include_first_last:
        frame_numbers.extend([0, total_frames - 1])

    unique = sorted(set(frame_numbers))[: config.max_keyframes]
    return _write_frames(capture, unique, output_dir)


def _write_frames(capture, frame_numbers: list[int], output_dir: Path) -> list[Path]:
    import cv2

    paths: list[Path] = []
    for index, frame_number in enumerate(frame_numbers):
        capture.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        ok, frame = capture.read()
        if not ok:
            continue
        path = output_dir / f"keyframe_{index:03d}.jpg"
        cv2.imwrite(str(path), frame)
        paths.append(path)
    capture.release()
    return paths

