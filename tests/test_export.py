"""Type-awareness smoke tests for export.export_plan dataclasses."""

from ai_practice_partner.export.export_plan import ExportEvent, ExportPlan


def test_export_plan_dataclass() -> None:
    event = ExportEvent(track_id="drums", channel=10, time_ticks=0, duration_ticks=120, velocity=100, drum=36)
    plan = ExportPlan(metadata={"tempo_bpm": 80}, ticks_per_quarter=480, channels={"drums": 10}, events=[event])
    assert plan.events[0].channel == 10
