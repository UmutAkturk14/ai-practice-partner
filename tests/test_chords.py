"""Type-awareness smoke tests for music.chords dataclasses."""

from ai_practice_partner.music.chords import ChordEvent, ChordState


def test_chord_event_dataclass() -> None:
    event = ChordEvent(symbol="Cmaj7", function="Imaj7", bar=0, beat=0, duration_steps=16)
    state = ChordState(function_label="Imaj7", position_tag="START")
    assert event.symbol == "Cmaj7"
    assert state.position_tag == "START"
