# Export Outline (Symbolic)
- Goal: map generated layers to a canonical symbolic format suitable for later MIDI or WAV rendering.

## Target formats
- Canonical internal format: JSON-like event list describing MIDI-ish data (tracks, channels, ticks, pitch/drum, velocity, duration).
- Optional future: real MIDI file rendering using the canonical format as source. WAV/audio is out of scope for now.

## Canonical event structure
- `event` fields:
  - `track_id`: logical name (`chords`, `drums`, `bass`).
  - `channel`: MIDI-like channel number (drums typically on 10).
  - `time_ticks`: start time in ticks from beginning.
  - `duration_ticks`: length in ticks.
  - `pitch`: MIDI note number (for chords/bass) or `drum` instrument id for percussion.
  - `velocity`: 0–127 placeholder.
  - `meta`: optional tags (e.g., `{"section": "loop", "passing": true}`).
- Ticks are derived from BPM and grid resolution: `ticks_per_quarter` (TPQ) chosen (e.g., 480), then `tick_per_step = TPQ * 4 / resolution` in 4/4.

## Track/channel mapping
- Separate tracks/channels per layer:
  - `chords`: dedicated track; channel assigned (e.g., 1).
  - `bass`: dedicated track; channel assigned (e.g., 2).
  - `drums`: dedicated track; channel 10 (or tagged drum ids).
- All layers use the same tempo and tick resolution derived from the session plan grid.

## Naming and metadata
- Filenames: include mood, seed, timestamp, and format, e.g., `track_{mood}_{seed}_{ts}.json` or `.mid`.
- Metadata fields stored alongside events:
  - `tempo_bpm`, `mood_id`, `style_template` (loop/12-bar/etc.), `seed`, `schema_version`, `generated_at`.
- Export package: `{ metadata, events[], ticks_per_quarter, channels: { chords, bass, drums } }`

## Examples
- JSON-like canonical export
```json
{
  "metadata": { "tempo_bpm": 80, "mood_id": "lofi_chill", "style_template": "loop", "seed": "s1", "schema_version": "0.1.0", "generated_at": "2024-01-01T00:00:00Z" },
  "ticks_per_quarter": 480,
  "channels": { "chords": 1, "bass": 2, "drums": 10 },
  "events": [
    { "track_id": "chords", "channel": 1, "time_ticks": 0, "duration_ticks": 1920, "pitch": 60, "velocity": 90, "meta": { "section": "loop" } },
    { "track_id": "bass",   "channel": 2, "time_ticks": 0, "duration_ticks": 480,  "pitch": 48, "velocity": 100, "meta": {} },
    { "track_id": "drums",  "channel": 10,"time_ticks": 0, "duration_ticks": 120,  "drum": 36, "velocity": 110, "meta": {} }
  ]
}
```
- Future MIDI (not detailed): same events mapped to a `.mid` file using `ticks_per_quarter`; channel 10 reserved for drums; filenames use the same naming convention.
