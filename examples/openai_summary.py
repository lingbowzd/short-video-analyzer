"""Summarize one video with OpenAI.

Requires:
    pip install social-video-summarizer[openai]
    export OPENAI_API_KEY=...
"""

from social_video_summarizer import SocialVideoSummarizer
from social_video_summarizer.providers.openai import OpenAISummaryProvider


def main() -> None:
    summarizer = SocialVideoSummarizer(
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

