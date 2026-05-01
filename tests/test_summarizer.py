from social_video_summarizer import SocialVideoSummarizer
from social_video_summarizer.prompts import build_summary_input


def test_build_summary_input_uses_social_metadata():
    text = build_summary_input(
        description="Trying a recipe",
        hashtags=["food", "#dinner"],
        music_title="Song",
    )

    assert "Creator description: Trying a recipe" in text
    assert "Hashtags: food, dinner" in text
    assert "Background music: Song" in text


def test_summarizer_without_provider_returns_summary_input():
    summarizer = SocialVideoSummarizer(keyframes={"strategy": "none"})
    result = summarizer.summarize(
        "example.mp4",
        duration=10,
        description="A fun day #vlog",
        transcript="hello world",
    )

    assert result.summary is None
    assert "Creator description: A fun day #vlog" in result.summary_input
    assert result.metadata_used["description"]
    assert result.processing["keyframe_strategy"] == "none"


def test_result_to_features():
    summarizer = SocialVideoSummarizer(keyframes={"strategy": "none"})
    result = summarizer.summarize(
        description="A fun day #vlog",
        transcript="hello world",
    )

    features = result.to_features()

    assert features["transcript_word_count"] == 2
    assert features["summary_input_hashtag_count"] == 1

