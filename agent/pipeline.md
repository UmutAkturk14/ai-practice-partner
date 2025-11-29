# Agent Pipeline (Orchestration Spec)
- Function: raw request → export-ready symbolic track. Documentation only; no executable code.

## Steps
- `parse_and_normalize_input`
  - Inputs: raw request `{ mood_id?, tempo?, bars?, chords?, seed? }`.
  - Outputs: `{ normalized_input, warnings[], errors[] }`.
  - Errors/warnings: see `agent/input_parser.md` (clamping warnings, invalid chords, unknown mood).
- `build_session_plan`
  - Inputs: `normalized_input`, loaded `mood_profile`.
  - Outputs: `session_plan` (blocks, grid, variation_rate, density, seed, chord anchors), warnings/errors propagated.
  - Errors/warnings: missing mood profile, conflicting bar counts vs template.
- `generate_chord_layer`
  - Inputs: `session_plan`, `mood_profile`.
  - Outputs: `chord_layer` (events on grid), warnings/errors propagated.
  - Errors/warnings: illegal transitions, empty anchors after validation.
- `generate_drum_layer`
  - Inputs: `session_plan`, `mood_profile`, shared grid.
  - Outputs: `drum_layer` (tracks per instrument), warnings/errors propagated.
  - Errors/warnings: pattern/archetype missing, fill placement conflicts.
- `generate_bass_layer`
  - Inputs: `session_plan`, `mood_profile`, `chord_layer`, shared grid.
  - Outputs: `bass_layer` (notes on grid), warnings/errors propagated.
  - Errors/warnings: missing roots from chords, movement pattern unavailable.
- `assemble_track`
  - Inputs: grid + layers + session metadata.
  - Outputs: `track_package` (grid, layers, sections, metadata), accumulated warnings/errors.
  - Errors/warnings: misaligned lengths, section boundary mismatches.
- `prepare_export`
  - Inputs: `track_package`, `mood_profile`.
  - Outputs: `export_plan` (symbolic MIDI-ish channels/ticks or JSON events) + metadata.
  - Errors/warnings: none expected beyond propagation; ensures no audio rendering is attempted.

## Determinism
- A single seed from normalized input flows through every step; all stochastic choices (Markov transitions, fills, passing tones) must use this seed to ensure identical output for the same request + seed.

## End-to-end examples (pseudocode)
- Clean request
```
req = { mood_id: "lofi_chill", tempo: 80, chords: "Cm7,Fm7,Bbmaj7,Cm7", seed: "s1" }
parse → normalized_input (warnings=[])
plan → session_plan (loop template, 12 bars with intro/loop/outro)
chords/drums/bass → layers on shared grid (warnings=[])
assemble → track_package
export → export_plan
return { export_plan, track_package, warnings: [], errors: [] }
```
- Clamped tempo with warning
```
req = { mood_id: "lofi_chill", tempo: 20, chords: "Cm7,Fm7,Bbmaj7" }
parse → normalized_input { tempo: 40 } + warning: tempo_clamped
plan → session_plan using default seed/bars
generation → layers
return with warnings: [tempo_clamped], errors: []
```
- Invalid chords error
```
req = { mood_id: "blues_gritty", tempo: 100, chords: "X1,Y2,Z3" }
parse → errors: invalid_chords (no valid tokens), normalized_input.chords = []
pipeline halts; return errors populated; no plan/layers/export produced
```
