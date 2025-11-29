"""Pipeline orchestration per agent/pipeline.md."""

from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass
class PipelineResult:
    """Result wrapper with export plan, track package, and diagnostics."""

    export_plan: Dict[str, Any]
    track_package: Dict[str, Any]
    warnings: List[dict]
    errors: List[dict]


# TODO: wire parse -> plan -> chord/drum/bass generation -> export once components are implemented.
