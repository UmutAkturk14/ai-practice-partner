# Sample Sets (Harmony & Rhythm Sources)
- Purpose: curated symbolic references used to seed generators (Markov transitions, pattern libraries) for chords, drums, and bass. Tagged by mood/style IDs consistent with `data/mood_profiles.md`.
- Format: JSON/YAML files grouped by type, carrying `schema_version` for reproducibility.

## Chord progressions
- Shape of a sample:
```json
{
  "schema_version": "0.1.0",
  "id": "lofi_loop_01",
  "mood_id": "lofi_chill",
  "bars": 4,
  "progression": ["i-7", "iv-7", "bVIImaj7", "i-7"],
  "notes": "4-bar loop-friendly minor progression"
}
```
- Tagging: `mood_id` points to a mood profile (`lofi_chill`, `lofi_dark`, `blues_gritty`, `jazz_relaxed`).
- Examples:
  - Lofi loop (4 bars): `["i-7", "iv-7", "bVIImaj7", "i-7"]`.
  - 12-bar blues template: `["I7","IV7","I7","I7","IV7","IV7","I7","I7","V7","IV7","I7","V7"]` with `mood_id: "blues_gritty"`.
  - Jazz ii–V–I snippet (4 bars): `["ii-7","V7","Imaj7","Imaj7"]` with `mood_id: "jazz_relaxed"`.

## Drum patterns
- Shape of a sample:
```json
{
  "schema_version": "0.1.0",
  "id": "lofi_kick_snare_01",
  "mood_id": "lofi_chill",
  "resolution": 16,
  "bars": 2,
  "tracks": {
    "kick":    [1,0,0,0, 0,0,0,0, 1,0,0,0, 0,0,0,0],
    "snare":   [0,0,0,0, 0,1,0,0, 0,0,0,0, 0,1,0,0],
    "hihat":   [0.5,0.6,0.5,0.6, 0.5,0.6,0.5,0.6, 0.5,0.6,0.5,0.6, 0.5,0.6,0.5,0.6]
  },
  "notes": "Sparse lofi groove"
}
```
- Tagging: `mood_id` aligns to mood profile; archetype names can be mapped from `drum_archetype`.
- Usage examples:
  - Shuffle backbeat for `blues_gritty` at 12 bars, resolution 12/24 for triplet feel.
  - Ride-based pattern for `jazz_relaxed` with light ghost notes encoded as low intensities.

## Bass patterns
- Shape of a sample:
```json
{
  "schema_version": "0.1.0",
  "id": "jazz_walk_ii_V_I",
  "mood_id": "jazz_relaxed",
  "resolution": 4,
  "bars": 2,
  "notes": [
    { "chord": "ii-7", "pitches": [50, 53, 55, 57] },
    { "chord": "V7",   "pitches": [49, 52, 55, 57] }
  ],
  "notes_meta": "Quarter-note walking outlines ii–V"
}
```
- Tagging: `mood_id` ties to bass movement preferences (sparse/walking/chromatic).
- Examples:
  - Lofi sparse root+5th pattern (2 bars) for `lofi_chill`.
  - Blues walk over `I7–IV7` (4 bars) for `blues_gritty`.

## How samples are used
- Build Markov/transition hints: chord progressions feed state transitions; drum/bass patterns contribute archetypes and density/swing cues aligned to mood profiles.
- Seed pattern libraries: provide starting grids and motifs that generators can vary; preserve tagging so the decision engine can select mood-appropriate seeds.
- Consistency: all samples reference mood IDs defined in `data/mood_profiles.md`; resolutions/bars should align with structure templates (loop/8, 12-bar, ii–V–I snippets).
