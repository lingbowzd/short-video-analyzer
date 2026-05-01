"""Prompt templates for short-form social video summarization."""

VIDEO_SUMMARY_PROMPT = """Your task is to generate a summary paragraph for a short-form social media video based on extracted text, available social metadata, and image data.
The summary must be a holistic description of the full video.
Avoid inferences or assumptions beyond the provided information.
If a field is empty, omit references to it rather than stating its absence.
Do not mention TikTok logos, platform watermarks, or usernames unless they are substantively relevant to the content.
Write one concise paragraph of approximately 50-100 words."""


def build_summary_input(
    *,
    duration: float | None = None,
    description: str | None = None,
    hashtags: list[str] | None = None,
    subtitle: str | None = None,
    sticker_text: str | None = None,
    transcript: str | None = None,
    music_title: str | None = None,
    music_author: str | None = None,
) -> str:
    """Format available social-video metadata for summary providers."""

    hashtag_text = None
    if hashtags:
        hashtag_text = ", ".join(tag.lstrip("#") for tag in hashtags)

    fields = [
        ("Duration", None if duration is None else f"{duration} seconds"),
        ("Creator description", description),
        ("Hashtags", hashtag_text),
        ("Subtitle", subtitle),
        ("Text stickers", sticker_text),
        ("Audio transcript", transcript),
        ("Background music", music_title),
        ("Background music artist", music_author),
    ]
    return "\n".join(f"{name}: {value}" for name, value in fields if value)
