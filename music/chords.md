# Chord Generation (Spec)
- Goal: generate a chord progression aligned to the session plan and mood profile, honoring user anchors and style-specific cadence rules.

## Chord event representation
- `ChordEvent` fields:
  - `symbol`: canonical chord text (e.g., `Cmaj7`, `Dm7b5`).
  - `function`: optional roman numeral/functional tag (e.g., `ii-7`, `V7`, `Imaj7`).
  - `bar`: integer bar index (0-based).
  - `beat`: float beat offset within bar.
  - `duration_steps`: integer length on the rhythm grid.
  - `tags`: optional (e.g., `["cadence"]`, `["anchor"]`).

## State and transitions
- State representation: `state = { function_label, position_tag }`
  - `function_label`: canonical function/degree (e.g., `i-7`, `IV7`, `ii-7`, `V7`, `Imaj7`).
  - `position_tag`: optional context (`START`, `MID`, `CADENCE`).
- Transition probabilities:
  - Derived from mood profile `chord_tendencies` and augmented by sample sets in `data/sample_sets.md` (progressions inform weights).
  - Mood/style modifies distributions: e.g., jazz increases weights for extended ii–V–I, blues emphasizes I7/IV7/V7 loop, lofi favors minor i → iv → bVII.
  - Normalization ensures weights sum to 1 for eligible next states.

## Anchor handling and filling
- User-provided chords become anchors:
  - Tokenize and map to functions where possible; place at specified bars (via separators) or sequentially.
  - Anchors are fixed unless invalid; invalid anchors produce errors and are dropped.
- Filling missing sections:
  - For bars without anchors, sample from the Markov chain respecting position tags (start/cadence).
  - If anchors exist at boundaries, fill in-between segments with transitions that lead into the next anchor (bridge logic may bias towards approach chords).
- Cadence enforcement:
  - Jazz: enforce ii–V–I cadence at ends of sections/phrases; increase weight for ii→V and V→I on cadence tags.
  - Blues: keep 12-bar form; maintain I7/IV7/V7 placements; optional V→IV turnaround at bar 12.
  - Lofi: allow loop closure with bVIImaj7→i or v-7→i; softer cadence bias.

## Examples (conceptual)
- Lofi (8-bar loop, mood `lofi_chill`)
  - Anchors: none.
  - Generated: `[i-7, iv-7, bVIImaj7, i-7, iv-7, v-7, bVIImaj7, i-7]`
  - Notes: swing feel implied by mood; cadence uses bVII→i.
- Blues (12-bar, mood `blues_gritty`)
  - Anchors: full 12-bar template respected.
  - Generated (with slight variation): `[I7, IV7, I7, I7, IV7, IV7, I7, I7, V7, IV7, I7, V7]`
  - Notes: anchors override sampling; only minor variation allowed if enabled.
- Jazz (8-bar loop, mood `jazz_relaxed`)
  - Anchors: user provides `Dm7,G7,Cmaj7` at bars 0–2.
  - Generated (fill bars 3–7 with ii–V–I bias and approach chords):
    - `[ii-7, V7, Imaj7, vi-7, ii-7, V7, Imaj7, Imaj7]`
  - Notes: cadence enforcement at bar 7 with V→I; anchors preserved.

## Outputs and invariants
- Outputs: ordered list of `ChordEvent` aligned to rhythm grid (bar/beat/duration), plus any anchor tags.
- Invariants:
  - Uses shared grid from session plan (BPM, resolution, feel).
  - Respects section boundaries from session plan (intro/loop/outro or 12-bar).
  - Seed from session plan drives all random sampling; same seed + input yields identical progression.
  - No transitions outside allowed mood-specific state set unless explicitly permitted.
