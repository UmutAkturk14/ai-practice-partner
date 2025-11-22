# Bassline Crafting (Stub)
- Objective: align bass notes to chord roots and rhythm grid groove.

- Pseudocode:
```
function craft_bassline(plan, mood_profile, chord_layer, rhythm_grid):
    bassline = []
    for each bar in chord_layer:
        root = extract_root(bar.chord_symbol)
        pattern = choose_pattern(mood_profile, bar_index)
        notes = map_pattern_to_grid(root, pattern, rhythm_grid)
        bassline.append(notes)
    return bassline
```

- Pattern considerations:
  - `lofi`: long sustains; occasional octave jumps.
  - `blues`: walking-style movement; shuffle grid adherence.
  - `jazz`: chromatic approaches into chord tones; higher variation rate.

- TODO:
  - Add passing tone heuristics and turnarounds.
  - Define articulation placeholders (staccato/legato flags) without playback.
