"""Bassline generation spec placeholder per music/bass.md."""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class BassNote:
    """Symbolic bass note aligned to the rhythm grid."""

    pitch: int
    start_step: int
    duration_steps: int
    velocity: int
    articulation: Optional[str] = None
    tags: List[str] = field(default_factory=list)


# TODO: implement pattern selection, passing tones, and alignment with chord roots and grid.
