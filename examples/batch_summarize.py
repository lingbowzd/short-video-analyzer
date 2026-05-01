"""Simple batch summarization pattern."""

from social_video_summarizer import SocialVideoSummarizer


def main() -> None:
    rows = [
        {
            "video_path": "video_001.mp4",
            "description": "Morning routine #grwm",
            "hashtags": ["grwm"],
            "transcript": "Here is my morning routine.",
        },
        {
            "video_path": "video_002.mp4",
            "description": "Quick dinner recipe #food",
            "hashtags": ["food"],
            "transcript": "This is a quick dinner recipe.",
        },
    ]

    summarizer = SocialVideoSummarizer(keyframes={"strategy": "none"})
    for index, row in enumerate(rows):
        result = summarizer.summarize(**row)
        result.save_json(f"outputs/summary_{index:03d}.json")


if __name__ == "__main__":
    main()

