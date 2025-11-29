"""Type-awareness smoke tests for music.bass dataclasses."""

from ai_practice_partner.music.bass import BassNote


def test_bass_note_dataclass() -> None:
    note = BassNote(pitch=48, start_step=0, duration_steps=4, velocity=90, articulation="legato")
    assert note.pitch == 48
