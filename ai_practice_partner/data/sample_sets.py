"""Sample set loader stubs per data/sample_sets.md."""

from dataclasses import dataclass, field
from typing import Dict, List

from ai_practice_partner.types import ChordSymbol


@dataclass(frozen=True)
class ChordSample:
    """Chord progression sample."""

    schema_version: str
    id: str
    mood_id: str
    bars: int
    progression: List[ChordSymbol]
    notes: str | None = None


@dataclass(frozen=True)
class DrumSample:
    """Drum pattern sample."""

    schema_version: str
    id: str
    mood_id: str
    resolution: int
    bars: int
    tracks: Dict[str, List[float]]
    notes: str | None = None


@dataclass(frozen=True)
class BassSample:
    """Bass pattern sample."""

    schema_version: str
    id: str
    mood_id: str
    resolution: int
    bars: int
    notes: List[Dict[str, object]]
    notes_meta: str | None = None


# TODO: implement loading of chord/drum/bass samples and mapping to mood profiles.
