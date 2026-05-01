"""OpenAI summary provider."""

from __future__ import annotations

from pathlib import Path

from ..prompts import VIDEO_SUMMARY_PROMPT


class OpenAISummaryProvider:
    """Generate summaries with OpenAI models.

    The first implementation sends text metadata. Image/keyframe support can be
    enabled by extending `_build_content` for the desired OpenAI API format.
    """

    def __init__(self, model: str = "gpt-4o-mini", client=None) -> None:
        if client is None:
            try:
                from openai import OpenAI
            except ImportError as exc:
                raise ImportError(
                    "Install OpenAI dependencies with `pip install social-video-summarizer[openai]`."
                ) from exc
            client = OpenAI()
        self.client = client
        self.model = model

    def summarize(self, *, summary_input: str, keyframes: list[str | Path], metadata=None) -> str:
        response = self.client.responses.create(
            model=self.model,
            input=[
                {"role": "system", "content": VIDEO_SUMMARY_PROMPT},
                {"role": "user", "content": summary_input},
            ],
        )
        return response.output_text

