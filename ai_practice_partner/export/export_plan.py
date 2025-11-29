"""Export plan stubs per export/export_outline.md."""

from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class ExportEvent:
    """Canonical event representation (MIDI-ish)."""

    track_id: str
    channel: int
    time_ticks: int
    duration_ticks: int
    velocity: int
    pitch: int | None = None
    drum: int | None = None
    meta: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ExportPlan:
    """Export package with metadata and events."""

    metadata: Dict[str, Any] = field(default_factory=dict)
    ticks_per_quarter: int = 480
    channels: Dict[str, int] = field(default_factory=dict)
    events: List[ExportEvent] = field(default_factory=list)


# TODO: implement mapping from track_package to canonical events and metadata.
