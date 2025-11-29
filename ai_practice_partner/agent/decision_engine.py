"""Decision engine building session plans per agent/decision_engine.md."""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class StructureBlock:
    """Represents a section of the track (intro, loop, outro, etc.)."""

    name: str
    bars: int
    style: str
    intensity: float


@dataclass
class SessionPlan:
    """Session plan driving generation."""

    tempo: int
    mood_id: str
    seed: str
    structure: List[StructureBlock]
    grid: dict
    variation_rate: float
    density: dict = field(default_factory=dict)
    chord_anchors: List[str] = field(default_factory=list)


# TODO: implement template selection, block sizing, grid config, and seed handling.
