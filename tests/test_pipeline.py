"""Type-awareness smoke tests for agent.pipeline dataclasses."""

from ai_practice_partner.agent.decision_engine import RhythmGrid, SessionPlan, StructureBlock
from ai_practice_partner.agent.pipeline import PipelineResult, TrackPackage
from ai_practice_partner.export.export_plan import ExportEvent, ExportPlan
from ai_practice_partner.utils.helpers import Diagnostic


def test_pipeline_result_dataclass() -> None:
    grid = RhythmGrid(bpm=80, resolution=16, bars=8, swing=0.12, time_signature={"beats_per_bar": 4, "beat_unit": 4})
    block = StructureBlock(name="loop", bars=8, style="lofi", intensity=0.6)
    plan = SessionPlan(
        tempo=80,
        mood_id="lofi_chill",
        seed="seed1",
        structure=[block],
        grid=grid,
        variation_rate=0.25,
        density={},
        chord_anchors=[],
    )
    export_plan = ExportPlan(
        metadata={"tempo_bpm": 80},
        ticks_per_quarter=480,
        channels={"chords": 1, "bass": 2, "drums": 10},
        events=[ExportEvent(track_id="chords", channel=1, time_ticks=0, duration_ticks=480, velocity=90, pitch=60)],
    )
    track_package = TrackPackage(grid={"resolution": 16}, layers={}, sections=[], metadata={})
    result = PipelineResult(export_plan=export_plan, track_package=track_package, warnings=[Diagnostic(code="w", message="warn")], errors=[], session_plan=plan)
    assert result.export_plan.ticks_per_quarter == 480
