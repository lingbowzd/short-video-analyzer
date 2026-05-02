# Quick Start

```python
from short_video_analyzer import ShortVideoAnalyzer

summarizer = ShortVideoAnalyzer(keyframes={"strategy": "none"})

result = summarizer.summarize(
    video_path="example.mp4",
    description="Trying this new recipe! #food",
    hashtags=["food", "recipe"],
    transcript="Today I am making a quick dinner recipe.",
    music_title="Example Song",
)

print(result.summary_input)
print(result.to_features())
```

All metadata fields are optional. For platforms where music, sticker text,
subtitles, or hashtags are unavailable, simply omit those arguments.

Add a summary provider when you are ready to call a model:

```python
from short_video_analyzer import ShortVideoAnalyzer
from short_video_analyzer.providers.openai import OpenAISummaryProvider

summarizer = ShortVideoAnalyzer(
    keyframes={"strategy": "scene", "max_keyframes": 8},
    summary_provider=OpenAISummaryProvider(model="gpt-4o-mini"),
)

result = summarizer.summarize(
    video_path="example.mp4",
    description="A day in my life",
)

print(result.summary)
```
