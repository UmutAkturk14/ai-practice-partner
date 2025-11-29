"""Drum pattern generation spec placeholder per music/drums.md."""

from dataclasses import dataclass, field
from typing import Dict, List

from ai_practice_partner.types import Bar, RhythmStep


@dataclass(frozen=True)
class DrumLayer:
    """Drum tracks aligned to the shared rhythm grid."""

    resolution: RhythmStep
    bars: Bar
    tracks: Dict[str, List[float]] = field(default_factory=dict)
    swing: float = 0.0


# TODO: implement archetype application, density mapping, swing/shuffle handling, and fills.
