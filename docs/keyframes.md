# Keyframes

The toolkit supports configurable keyframe strategies:

```python
SocialVideoSummarizer(
    keyframes={
        "strategy": "scene",
        "scene_threshold": 3.5,
        "max_keyframes": 8,
        "include_first_last": True,
    }
)
```

## Strategies

- `scene`: detect scene changes and sample representative frames.
- `interval`: sample every N seconds.
- `uniform`: sample K frames evenly across the video.
- `manual`: use user-provided screenshots.
- `none`: skip keyframes.

Use `manual` when screenshots have already been extracted by another workflow.

For TikTok-style short videos, a compact set of keyframes is usually more
efficient than analyzing every frame. Users can increase `max_keyframes` or use
interval sampling when videos are longer or visually dense.
