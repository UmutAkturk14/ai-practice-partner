"""Mood profile loader and schema stubs per data/mood_profiles.md."""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(frozen=True)
class TempoRange:
    """Tempo defaults and bounds."""

    default: int
    minimum: int
    maximum: int


@dataclass(frozen=True)
class Density:
    """Per-layer density hints (0–1)."""

    chords: float
    drums: float
    bass: float


@dataclass(frozen=True)
class HarmonicBias:
    """Harmonic bias weights (0–1)."""

    extensions: float
    dissonance: float
    complexity: float


@dataclass(frozen=True)
class StructureTemplate:
    """Default structure template."""

    template: str
    bars: int


@dataclass(frozen=True)
class MoodProfile:
    """Structured mood profile."""

    schema_version: str
    id: str
    description: str
    tempo_bpm: TempoRange
    swing: float
    density: Density
    harmonic_bias: HarmonicBias
    variation_rate: float
    drum_archetype: str
    bass_movement: str
    structure: Optional[StructureTemplate] = None
    chord_tendencies: Optional[Dict[str, Dict[str, object]]] = None
    start_states: Optional[List[Dict[str, object]]] = None


# TODO: implement schema validation, loading from JSON/YAML, and version handling.
