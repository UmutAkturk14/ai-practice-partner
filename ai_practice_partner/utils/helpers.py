"""Utility helper stubs per utils/helpers.md."""

from dataclasses import dataclass, field
from typing import Any, Generic, List, Optional, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class Diagnostic:
    """Structured warning/error message."""

    code: str
    message: str
    field: Optional[str] = None


@dataclass(frozen=True)
class ValidationResult(Generic[T]):
    """Generic validation wrapper."""

    value: Optional[T] = None
    warnings: List[Diagnostic] = field(default_factory=list)
    errors: List[Diagnostic] = field(default_factory=list)


# TODO: add time helpers (beats/ms, steps), RNG seeding/weighted choice, validation helpers, and diagnostics aggregation.
