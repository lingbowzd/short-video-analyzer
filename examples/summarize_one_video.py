"""Summarize one short-form social video without calling external APIs."""

from short_video_analyzer import ShortVideoAnalyzer


def main() -> None:
    summarizer = ShortVideoAnalyzer(keyframes={"strategy": "none"})
    result = summarizer.summarize(
        video_path="example.mp4",
        duration=20.0,
        description="Trying this new recipe! #food #dinner",
        hashtags=["food", "dinner"],
        transcript="Today I am making a quick dinner recipe.",
        music_title="Example Song",
    )

    print(result.summary_input)
    print(result.to_features())


if __name__ == "__main__":
    main()

