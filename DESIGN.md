# System Architecture (Abstract)
- Goal: agentic pipeline that converts user intent (BPM, chord sequence, mood) into layered backing tracks (chords, drums, bass) with export hooks.
- Constraints: no runtime logic; only structural placeholders and pseudocode.

## Modules
- `agent/`: orchestrates flow from input parsing to asset assembly. Maintains context (BPM, mood profile, structural decisions).
- `music/`: algorithmic generation stubs (Markov chords, rhythm grids, bass heuristics).
- `data/`: placeholder datasets and mood profile definitions (symbolic descriptions only).
- `export/`: outlines for MIDI/WAV renderers; no synthesis code.
- `utils/`: shared helpers (validation, tokenization, time-grid utilities) in pseudocode.
- `api/`: future backend endpoints; request/response contracts only.

## Data Flow (planned)
1. Receive user input (BPM, chord sequence, mood tag).
2. Normalize/validate → create `SessionPlan` object (conceptual).
3. Agent evaluates mood profile → selects chord transition model (Markov chain) and rhythm grid config.
4. Generate chord progression sketch (states = chord symbols; transitions weighted by mood).
5. Generate drum pattern on time grid (e.g., 16 steps per bar; accent rules vary by mood).
6. Generate bassline tied to chord roots and groove hints.
7. Merge layers into track structure (intro, loop, outro) with dynamic variation hooks.
8. Export adapter prepares symbolic data for MIDI/WAV rendering (not implemented).

## Markov Chain Notes
- State: chord symbol + position-in-phrase context tag.
- Transition weights: derived from mood profile tendencies (e.g., ii→V heavy in jazz).
- Generation loop: seed from user chord input when provided; otherwise sample from mood defaults with reproducible RNG.

## Rhythm Grid
- Temporal resolution: configurable (e.g., 1/16 per beat) stored in grid metadata.
- Drum slots: kick/snare/hh/perc arrays parallel to grid; values are hit-intensity placeholders.
- Swing/feel: mood profile may shift off-beat timing; only described, not applied.

## Mood Profiles
- Define chord tendencies, rhythmic density, instrumentation hints.
- Lofi: sparse drums, extended chords, mellow bass movement.
- Blues: shuffle grid, dominant transitions, walking bass bias.
- Jazz: extended ii-V-I loops, ride cymbal emphasis, chromatic bass passing tones.

## Export Outline
- MIDI: map symbolic events to tracks/channels; preserve velocity placeholders.
- WAV: plan for future synth/sample rendering pipeline (requires audio engine).

## TODO (implementation later)
- Concrete data structures and serializers.
- Deterministic seeding and reproducibility tools.
- CLI/API wiring and persistence.
