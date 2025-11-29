"""Type-awareness smoke tests for agent.decision_engine dataclasses."""

from ai_practice_partner.agent.decision_engine import RhythmGrid, SessionPlan, StructureBlock


def test_session_plan_dataclass() -> None:
    grid = RhythmGrid(bpm=80, resolution=16, bars=8, swing=0.12, time_signature={"beats_per_bar": 4, "beat_unit": 4})
    block = StructureBlock(name="loop", bars=8, style="lofi", intensity=0.6)
    plan = SessionPlan(
        tempo=80,
        mood_id="lofi_chill",
        seed="seed1",
        structure=[block],
        grid=grid,
        variation_rate=0.25,
        density={"chords": 0.4, "drums": 0.35, "bass": 0.3},
        chord_anchors=["i-7"],
    )
    assert plan.structure[0].name == "loop"
