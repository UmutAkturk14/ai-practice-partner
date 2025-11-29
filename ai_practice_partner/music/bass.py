"""Bassline generation spec placeholder per music/bass.md."""

from dataclasses import dataclass, field
from typing import List, Optional

from ai_practice_partner.types import RhythmStep


@dataclass(frozen=True)
class BassNote:
    """Symbolic bass note aligned to the rhythm grid."""

    pitch: int
    start_step: RhythmStep
    duration_steps: RhythmStep
    velocity: int
    articulation: Optional[str] = None
    tags: List[str] = field(default_factory=list)


# TODO: implement pattern selection, passing tones, and alignment with chord roots and grid.
