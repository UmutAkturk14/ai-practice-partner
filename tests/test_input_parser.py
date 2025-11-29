"""Type-awareness smoke tests for agent.input_parser dataclasses."""

from ai_practice_partner.agent.input_parser import NormalizedInput, ParseResult
from ai_practice_partner.utils.helpers import Diagnostic


def test_input_parser_dataclasses() -> None:
    normalized = NormalizedInput(mood_id="lofi_chill", tempo=80, bars=8, chords=["Cm7"], seed="seed1")
    result = ParseResult(normalized_input=normalized, warnings=[Diagnostic(code="w", message="warn")], errors=[])
    assert result.normalized_input is normalized
