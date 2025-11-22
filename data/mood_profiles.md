# Mood Profiles (Descriptive Placeholders)
- Structure idea:
```
profile = {
  name: "lofi",
  chord_tendencies: { state: { transitions: { target: weight } } },
  rhythm_resolution: 4 or 8 or 16,
  drum_kick_snare: pattern descriptor,
  drum_hihat: pattern descriptor,
  perc_density: scalar,
  bass_behavior: { movement: "sparse", passing_tones: "rare" }
}
```

- Profiles (conceptual only):
  - `lofi`: mellow; prefer minor 7/9; sparse drums; optional vinyl noise flag (not implemented).
  - `blues`: dominant chords; 12-bar template; shuffle grid; walking bass preference.
  - `jazz`: extended harmonies; ii-V-I bias; ride cymbal pattern; chromatic bass movement.

- TODO:
  - Fill `chord_tendencies` with symbolic weights (no real numbers yet).
  - Add dynamic intensity curves over time (intro vs loop vs outro).
