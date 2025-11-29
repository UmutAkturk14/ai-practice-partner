"""Input parsing and normalization per agent/input_parser.md."""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class NormalizedInput:
    """Structured input after validation and normalization."""

    mood_id: str
    tempo: int
    bars: int
    chords: List[str] = field(default_factory=list)
    seed: Optional[str] = None


@dataclass
class ParseResult:
    """Aggregate result with diagnostics."""

    normalized_input: Optional[NormalizedInput]
    warnings: List[dict] = field(default_factory=list)
    errors: List[dict] = field(default_factory=list)


# TODO: implement parsing, clamping, chord canonicalization, and diagnostics aggregation.
