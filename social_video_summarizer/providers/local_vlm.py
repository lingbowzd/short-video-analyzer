"""Placeholder for local vision-language model providers."""

from __future__ import annotations


class LocalVLMSummaryProvider:
    """Adapter placeholder for local VLM summarization.

    Users can subclass this adapter or pass any object with a compatible
    `.summarize(summary_input=..., keyframes=..., metadata=...)` method.
    """

    def summarize(self, *, summary_input: str, keyframes: list[str], metadata=None) -> str:
        raise NotImplementedError(
            "Local VLM support depends on the selected model. Pass a custom provider "
            "or subclass LocalVLMSummaryProvider."
        )

