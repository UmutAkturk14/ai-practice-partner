"""Decision engine building session plans per agent/decision_engine.md."""

from dataclasses import dataclass, field
from typing import Dict, List

from ai_practice_partner.types import Bar, ChordSymbol


@dataclass(frozen=True)
class RhythmGrid:
    """Rhythm grid configuration for the session."""

    bpm: int
    resolution: int
    bars: Bar
    swing: float
    time_signature: Dict[str, int]


@dataclass(frozen=True)
class StructureBlock:
    """Represents a section of the track (intro, loop, outro, etc.)."""

    name: str
    bars: Bar
    style: str
    intensity: float


@dataclass(frozen=True)
class SessionPlan:
    """Session plan driving generation."""

    tempo: int
    mood_id: str
    seed: str
    structure: List[StructureBlock]
    grid: RhythmGrid
    variation_rate: float
    density: Dict[str, float] = field(default_factory=dict)
    chord_anchors: List[ChordSymbol] = field(default_factory=list)


# TODO: implement template selection, block sizing, grid config, and seed handling.
