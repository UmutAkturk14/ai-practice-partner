"""Type-awareness smoke tests for data layer dataclasses."""

from ai_practice_partner.data.mood_profiles import (
    Density,
    HarmonicBias,
    MoodProfile,
    StructureTemplate,
    TempoRange,
)
from ai_practice_partner.data.sample_sets import BassSample, ChordSample, DrumSample


def test_mood_profile_dataclass() -> None:
    profile = MoodProfile(
        schema_version="0.1.0",
        id="lofi_chill",
        description="test",
        tempo_bpm=TempoRange(default=80, minimum=65, maximum=90),
        swing=0.12,
        density=Density(chords=0.4, drums=0.35, bass=0.3),
        harmonic_bias=HarmonicBias(extensions=0.6, dissonance=0.2, complexity=0.4),
        variation_rate=0.25,
        drum_archetype="lofi-minimal",
        bass_movement="sparse",
        structure=StructureTemplate(template="loop", bars=8),
    )
    assert profile.id == "lofi_chill"


def test_sample_dataclasses() -> None:
    chord_sample = ChordSample(schema_version="0.1.0", id="lofi_loop_01", mood_id="lofi_chill", bars=4, progression=["i-7"])
    drum_sample = DrumSample(schema_version="0.1.0", id="lofi_kick_snare_01", mood_id="lofi_chill", resolution=16, bars=2, tracks={"kick": [1.0]})
    bass_sample = BassSample(schema_version="0.1.0", id="jazz_walk", mood_id="jazz_relaxed", resolution=4, bars=2, notes=[{"chord": "ii-7", "pitches": [50]}])
    assert chord_sample.bars == 4 and drum_sample.resolution == 16 and bass_sample.notes_meta is None
