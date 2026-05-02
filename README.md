# Short Video Analyzer

Short Video Analyzer is an efficient, metadata-aware toolkit for summarizing
short-form social media videos. It is designed primarily for TikTok-style data
and for researchers or dataset builders who need scalable video summaries
without running expensive frame-by-frame analysis.

## Why This Toolkit?

Short-form social videos are not just video files. Their meaning often depends
on creator descriptions, hashtags, subtitles, text stickers, audio transcripts,
and music metadata when those fields are available. This toolkit combines the
available signals with a compact set of informative keyframes to generate
grounded summaries. Missing fields are simply ignored.

In this project, "metadata-aware" means that the summarizer can use platform-
specific fields collected alongside a video, such as description text, hashtags,
subtitles, sticker text, music title, and music artist. It does not require all
of these fields. Many platforms or scraping workflows only provide the video
file and description, and that is a valid input.

## Design Goals

- Efficient keyframe-based summarization instead of frame-by-frame analysis.
- Configurable screenshot/keyframe extraction.
- Social metadata-aware prompts.
- Provider-based architecture for OpenAI, Azure, Whisper, local VLMs, and
  custom backends.
- Batch-friendly outputs for research datasets.
- Optional lightweight post-summary features, kept secondary to summarization.

## Installation

Short Video Analyzer requires Python 3.9 or later.

### Install From PyPI

After the package is published to PyPI, install it with:

```bash
pip install short-video-analyzer
```

### Install From GitHub

Before the PyPI release, or if you want the latest development version, install
directly from GitHub:

```bash
pip install git+https://github.com/lingbow/short-video-analyzer.git
```

### Install From a Local Clone

```bash
git clone https://github.com/lingbow/short-video-analyzer.git
cd short-video-analyzer
pip install -e .
```

### Optional Dependencies

Install only the backends you need:

```bash
# Video/keyframe extraction
pip install "short-video-analyzer[video]"

# OpenAI summary provider
pip install "short-video-analyzer[openai]"

# Azure Speech-to-Text provider
pip install "short-video-analyzer[azure]"

# Local Whisper transcription
pip install "short-video-analyzer[whisper]"

# Local VLM dependencies
pip install "short-video-analyzer[local]"

# Everything
pip install "short-video-analyzer[all]"
```

For local development:

```bash
pip install -e ".[dev]"
```

## Quick Start

This example does not call any external API. It formats the available video
metadata into the prompt input that a summary provider would use:

```python
from short_video_analyzer import ShortVideoAnalyzer

summarizer = ShortVideoAnalyzer(
    keyframes={
        "strategy": "scene",
        "max_keyframes": 8,
        "include_first_last": True,
    },
    transcriber=None,
    summary_provider=None,
)

result = summarizer.summarize(
    video_path="example.mp4",
    description="Trying this new recipe! #food",
    hashtags=["food", "recipe"],
    music_title="Example Song",
)

print(result.summary_input)
```

To generate summaries with OpenAI, install the OpenAI extra and set your API
key:

```bash
pip install "short-video-analyzer[openai]"
export OPENAI_API_KEY="your-api-key"
```

Then configure the provider:

```python
from short_video_analyzer import ShortVideoAnalyzer
from short_video_analyzer.providers.openai import OpenAISummaryProvider

summarizer = ShortVideoAnalyzer(
    summary_provider=OpenAISummaryProvider(model="gpt-4o-mini"),
)

result = summarizer.summarize("example.mp4", description="A day in my life")
print(result.summary)
```

To extract keyframes from a video file, install the video extra:

```bash
pip install "short-video-analyzer[video]"
```

Then use a keyframe strategy such as `scene`, `interval`, or `uniform`.

## Output

The main output is a structured summary result:

```python
{
    "summary": "...",
    "summary_input": "...",
    "transcript": "...",
    "keyframes": ["keyframe_000.jpg", "keyframe_001.jpg"],
    "metadata_used": {
        "description": true,
        "hashtags": true,
        "music": true,
        "transcript": true,
        "keyframes": true
    },
    "processing": {
        "keyframe_strategy": "scene",
        "max_keyframes": 8,
        "summary_provider": "openai"
    }
}
```

## Optional Features

The package keeps feature extraction optional. The MVP includes simple
post-summary/text helpers such as word counts, hashtag counts, question counts,
emoji counts, and speaking rate.

```python
features = result.to_features()
```

Topic modeling, emotion classification, and embeddings can be added later as
optional modules.

## Scope

The toolkit is optimized primarily for TikTok and TikTok-like short-form social
media videos. It can also be used for Instagram Reels, YouTube Shorts, Douyin,
RedNote/Xiaohongshu, influencer posts, short ads, and product demo clips.

The expected video length is roughly a few seconds to a few minutes. Longer
videos can be supported through chunking or custom keyframe strategies, but
long-form video analysis is not the primary target.
