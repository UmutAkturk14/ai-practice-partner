"""Type-awareness smoke tests for utils.helpers dataclasses."""

from ai_practice_partner.utils.helpers import Diagnostic, ValidationResult


def test_diagnostic_and_validation_result_instantiation() -> None:
    diag = Diagnostic(code="sample", message="test", field="tempo")
    result: ValidationResult[int] = ValidationResult(value=120, warnings=[diag], errors=[])
    assert result.value == 120
