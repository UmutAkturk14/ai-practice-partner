# Bassline Generation (Spec)
- Goal: generate bass notes aligned to chord events and the shared rhythm grid, guided by mood/style.

## Bass note representation
- `BassNote` fields:
  - `pitch`: MIDI number or relative interval from chord root (store canonical form).
  - `start_step`: integer grid index.
  - `duration_steps`: integer length on the grid.
  - `velocity`: 0–127 placeholder.
  - `articulation`: optional tags (`staccato`, `legato`, `ghost`).
  - `tags`: optional (e.g., `["passing"]`, `["approach"]`).

## Chord tone extraction
- From each chord event, derive:
  - `root` pitch class.
  - Available chord tones (root, third, fifth, seventh, extensions if present).
  - Function tag (e.g., `ii`, `V`, `I`) to inform approach choices.
- Roots anchor bass patterns; chord tones provide targets for passing/approach notes.

## Pattern families
- `root_only`: sustain or repeated roots; used in very sparse lofi sections.
- `root_fifth`: alternate root and fifth; used for moderate density lofi/blues.
- `walking`: quarter-note movement outlining chord tones; used for blues/jazz higher density.
- `pedal`: hold root or fifth across a bar/section; used for intros/outros.
- `approach`: target upcoming chord with approach tones; used in jazz/blues cadences.
- Selection depends on mood `bass_movement`, `density.bass`, and section context (intro/loop/outro).

## Passing tones
- Allowed intervals (relative to root): `b2`, `2`, `b3`, `3`, `4`, `b5`, `5`, `b7`, `7` as approach; plus chromatic steps into target chord tones for jazz.
- Mood influence:
  - Lofi: low frequency of passing tones; prefer diatonic steps and occasional `b2`/`5` approach.
  - Blues: moderate passing; chromatic walk-ups into V/I; honor shuffle grid.
  - Jazz: higher passing tone usage; chromatic approaches into chord tones (especially into V→I).
- Passing notes tagged for downstream handling; must still align to grid steps.

## Alignment with grid
- Bass notes placed on the same rhythm grid as drums/chords (shared `resolution`, `bars`, `swing` metadata).
- Patterns map to grid indices; durations respect step counts and section boundaries.
- Invariants: no notes outside grid length; start_step/duration_steps align with session plan bars/sections.

## Examples (conceptual)
- Lofi loop (4 bars, `lofi_chill`)
  - Chords: `[i-7, iv-7, bVIImaj7, i-7]`
  - Pattern: root_fifth with sparse passing; notes on beats 1 and 3, occasional approach `b2` into i.
  - Result: roots at steps 0, 32, 64, 96; occasional low-velocity passing into bar starts.
- Blues 12-bar (`blues_gritty`)
  - Chords: standard 12-bar I/IV/V.
  - Pattern: walking quarters; outlines chord tones; passing `#4` into V, `b3` into IV.
  - Result: continuous quarter-note line across bars, swing feel inherited from grid.
- Jazz ii–V–I (`jazz_relaxed`)
  - Chords: `[ii-7, V7, Imaj7, Imaj7]`
  - Pattern: walking with chromatic approaches; target roots on downbeats, use `b2`/`3` into V, `b2`/`7` into I.
  - Result: ii bar outlines ii chord tones, V bar approaches I with chromatic step, I bars settle on root/5/7 with occasional approach back to ii if looping.

## Outputs and invariants
- Output: list of `BassNote` aligned to the shared grid with tags for passing/approach.
- Invariants:
  - Uses session plan seed for any stochastic pattern choices; same input + seed → same bassline.
  - Honors chord roots/anchors; no patterns that ignore chord changes.
  - Respects density/variation guidance from mood profile and section context.
