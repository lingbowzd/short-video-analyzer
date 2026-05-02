"""Summarize one video with OpenAI.

Requires:
    pip install short-video-analyzer[openai]
    export OPENAI_API_KEY=...
"""

from short_video_analyzer import ShortVideoAnalyzer
from short_video_analyzer.providers.openai import OpenAISummaryProvider


def main() -> None:
    summarizer = ShortVideoAnalyzer(
        keyframes={"strategy": "none"},
        summary_provider=OpenAISummaryProvider(model="gpt-4o-mini"),
    )
    result = summarizer.summarize(
        video_path="example.mp4",
        description="A day in my life #vlog",
        hashtags=["vlog"],
        transcript="Here is my morning routine before work.",
    )
    print(result.summary)


if __name__ == "__main__":
    main()

