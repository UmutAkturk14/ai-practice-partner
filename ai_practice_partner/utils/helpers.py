"""Utility helper stubs per utils/helpers.md."""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class ValidationResult:
    """Generic validation wrapper."""

    value: Any = None
    warnings: List[dict] = field(default_factory=list)
    errors: List[dict] = field(default_factory=list)


# TODO: add time helpers (beats/ms, steps), RNG seeding/weighted choice, validation helpers, and diagnostics aggregation.
