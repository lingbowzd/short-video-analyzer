# Short Video Analyzer

Short Video Analyzer is an efficient, metadata-aware toolkit for summarizing
short-form social media videos.

It is optimized for research workflows where users need scalable summaries for
many videos, not expensive frame-by-frame descriptions of every visual moment.

## Core Idea

The toolkit combines:

- a compact set of configurable keyframes,
- transcript or speech-to-text output,
- creator descriptions,
- hashtags,
- subtitles,
- text stickers,
- and music metadata when available.

These inputs are formatted into a grounded prompt for a summary provider.

## What Metadata-Aware Means

"Metadata-aware" means the summarizer can use social-platform fields that are
collected alongside the video file. For TikTok, this may include description,
hashtags, subtitle text, sticker text, music title, music artist, transcript,
and duration.

All metadata fields are optional. If a platform or scraper only provides the
video file and description, the missing fields are ignored rather than imputed.

## Platforms and Scope

The toolkit is designed primarily for TikTok-style short-form video data. It can
also support Instagram Reels, YouTube Shorts, Douyin, RedNote/Xiaohongshu,
influencer videos, short ads, and product demo clips when similar inputs are
available.

It is optimized for videos ranging from a few seconds to a few minutes. Longer
videos may require chunking or custom sampling strategies.

## Target Users

- Computational social science researchers.
- Marketing and information systems researchers.
- Creator economy researchers.
- Dataset builders.
- Students who need video summaries without building a full multimodal stack.
