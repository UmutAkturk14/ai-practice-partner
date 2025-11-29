"""Mood profile loader and schema stubs per data/mood_profiles.md."""

from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class MoodProfile:
    """Structured mood profile."""

    id: str
    description: str
    data: Dict[str, Any] = field(default_factory=dict)


# TODO: implement schema validation, loading from JSON/YAML, and version handling.
