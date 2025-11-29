"""Shared typed aliases used across the project."""

from typing import Literal

RhythmStep = int
Beat = int
Bar = int
TimeMs = float

TrackType = Literal["chords", "drums", "bass"]

ChordSymbol = str

# TODO: expand with structured types (e.g., RhythmGrid, Section) as implementation evolves.
