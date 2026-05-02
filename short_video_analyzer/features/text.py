"""Lightweight optional text features."""

from __future__ import annotations

import re

HASHTAG_RE = re.compile(r"#\w+")
WORD_RE = re.compile(r"\b[\w']+\b")
EMOJI_RE = re.compile(
    "["
    "\U0001f300-\U0001f5ff"
    "\U0001f600-\U0001f64f"
    "\U0001f680-\U0001f6ff"
    "\U0001f700-\U0001f77f"
    "\U0001f780-\U0001f7ff"
    "\U0001f800-\U0001f8ff"
    "\U0001f900-\U0001f9ff"
    "\U0001fa00-\U0001fa6f"
    "\U0001fa70-\U0001faff"
    "]+",
    flags=re.UNICODE,
)


def count_words(text: str | None) -> int:
    return len(WORD_RE.findall(text or ""))


def count_hashtags(text: str | None) -> int:
    return len(HASHTAG_RE.findall(text or ""))


def count_questions(text: str | None) -> int:
    return (text or "").count("?")


def count_emojis(text: str | None) -> int:
    return len(EMOJI_RE.findall(text or ""))


def speaking_rate(transcript: str | None, duration_seconds: float | None) -> float | None:
    if not duration_seconds or duration_seconds <= 0:
        return None
    return count_words(transcript) / duration_seconds


def extract_text_features(
    *,
    summary: str | None = None,
    summary_input: str | None = None,
    transcript: str | None = None,
) -> dict[str, int]:
    """Extract simple optional features from summary artifacts."""

    return {
        "summary_word_count": count_words(summary),
        "summary_input_word_count": count_words(summary_input),
        "transcript_word_count": count_words(transcript),
        "summary_question_count": count_questions(summary),
        "summary_input_hashtag_count": count_hashtags(summary_input),
        "summary_input_emoji_count": count_emojis(summary_input),
    }

