# Drum Pattern Design (Rhythm Grid Concept)
- Grid definition:
  - `resolution`: steps per beat (e.g., 4 or 8 or 16).
  - `bars`: number of bars to generate.
  - Data structure concept: arrays per instrument aligned to grid indices.

- Rhythm grid builder (pseudocode):
```
function build_rhythm_grid(bpm, resolution, bars):
    grid = { bpm: bpm, resolution: resolution, bars: bars }
    grid.steps = bars * 4 * resolution  # assuming 4/4; abstract only
    grid.tracks = { kick: [], snare: [], hihat: [], perc: [] }
    return grid
```

- Pattern sketcher (pseudocode):
```
function design_drum_pattern(plan, mood_profile, grid):
    apply_accent_rules(grid, mood_profile)
    add_kick_snare(grid, pattern=mood_profile.drum_kick_snare)
    add_hihat(grid, pattern=mood_profile.drum_hihat)
    maybe_add_perc(grid, density=mood_profile.perc_density)
    return grid
```

- Mood influences (descriptive):
  - `lofi`: soft kicks, off-grid swing flag, sparse hats.
  - `blues`: shuffle feel; backbeat snare emphasis.
  - `jazz`: ride pattern bias; light ghost notes (symbolic).

- TODO:
  - Encode swing offsets as fractional step shifts.
  - Support fills at phrase boundaries.
