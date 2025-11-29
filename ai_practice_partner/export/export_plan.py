"""Export plan stubs per export/export_outline.md."""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from ai_practice_partner.types import TrackType


@dataclass(frozen=True)
class ExportEvent:
    """Canonical event representation (MIDI-ish)."""

    track_id: TrackType
    channel: int
    time_ticks: int
    duration_ticks: int
    velocity: int
    pitch: Optional[int] = None
    drum: Optional[int] = None
    meta: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class ExportPlan:
    """Export package with metadata and events."""

    metadata: Dict[str, Any] = field(default_factory=dict)
    ticks_per_quarter: int = 480
    channels: Dict[TrackType, int] = field(default_factory=dict)
    events: List[ExportEvent] = field(default_factory=list)


# TODO: implement mapping from track_package to canonical events and metadata.
