"""Chord generation spec placeholder per music/chords.md."""

from dataclasses import dataclass, field
from typing import List, Optional

from ai_practice_partner.types import Bar, Beat, ChordSymbol, RhythmStep


@dataclass(frozen=True)
class ChordEvent:
    """Symbolic chord event aligned to the rhythm grid."""

    symbol: ChordSymbol
    function: Optional[str]
    bar: Bar
    beat: Beat
    duration_steps: RhythmStep
    tags: List[str] = field(default_factory=list)


@dataclass(frozen=True)
class ChordState:
    """Markov state representation for chord generation."""

    function_label: str
    position_tag: Optional[str] = None


# TODO: implement state/transition model, anchor handling, cadence rules, and seed-driven sampling.
