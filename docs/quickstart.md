# Quick Start

```python
from social_video_summarizer import SocialVideoSummarizer

summarizer = SocialVideoSummarizer(keyframes={"strategy": "none"})

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
from social_video_summarizer import SocialVideoSummarizer
from social_video_summarizer.providers.openai import OpenAISummaryProvider

summarizer = SocialVideoSummarizer(
    keyframes={"strategy": "scene", "max_keyframes": 8},
    summary_provider=OpenAISummaryProvider(model="gpt-4o-mini"),
)

result = summarizer.summarize(
    video_path="example.mp4",
    description="A day in my life",
)

print(result.summary)
```
