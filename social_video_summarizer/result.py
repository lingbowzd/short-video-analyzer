"""Structured summary results."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

from .features.text import extract_text_features


@dataclass
class SummaryResult:
    """Output object returned by `SocialVideoSummarizer.summarize`."""

    summary: str | None
    summary_input: str
    transcript: str | None = None
    keyframes: list[str] = field(default_factory=list)
    metadata_used: dict[str, bool] = field(default_factory=dict)
    processing: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Return the result as a JSON-serializable dictionary."""

        return asdict(self)

    def to_features(self) -> dict[str, Any]:
        """Return optional lightweight text features derived from the result."""

        return extract_text_features(
            summary=self.summary,
            summary_input=self.summary_input,
            transcript=self.transcript,
        )

    def save_json(self, path: str | Path) -> Path:
        """Save the result as JSON."""

        import json

        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.to_dict(), indent=2), encoding="utf-8")
        return path

