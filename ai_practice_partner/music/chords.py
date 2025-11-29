"""Chord generation spec placeholder per music/chords.md."""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ChordEvent:
    """Symbolic chord event aligned to the rhythm grid."""

    symbol: str
    function: Optional[str]
    bar: int
    beat: float
    duration_steps: int
    tags: List[str] = field(default_factory=list)


# TODO: implement state/transition model, anchor handling, cadence rules, and seed-driven sampling.
