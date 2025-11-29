"""Pipeline orchestration per agent/pipeline.md."""

from dataclasses import dataclass, field
from typing import Any, Dict, List

from ai_practice_partner.agent.decision_engine import SessionPlan
from ai_practice_partner.export.export_plan import ExportPlan
from ai_practice_partner.utils.helpers import Diagnostic


@dataclass(frozen=True)
class TrackPackage:
    """Aggregated layers and metadata ready for export."""

    grid: Dict[str, Any]
    layers: Dict[str, Any]
    sections: List[Dict[str, Any]]
    metadata: Dict[str, Any]


@dataclass(frozen=True)
class PipelineResult:
    """Result wrapper with export plan, track package, and diagnostics."""

    export_plan: ExportPlan
    track_package: TrackPackage
    warnings: List[Diagnostic] = field(default_factory=list)
    errors: List[Diagnostic] = field(default_factory=list)
    session_plan: SessionPlan | None = None


# TODO: wire parse -> plan -> chord/drum/bass generation -> export once components are implemented.
