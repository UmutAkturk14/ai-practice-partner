"""Type-awareness smoke tests for music.drums dataclasses."""

from ai_practice_partner.music.drums import DrumLayer


def test_drum_layer_dataclass() -> None:
    layer = DrumLayer(resolution=16, bars=4, tracks={"kick": [1.0, 0.0]}, swing=0.12)
    assert layer.resolution == 16
