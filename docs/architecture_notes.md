# Architecture Notes
- Audience: developers implementing and extending the symbolic agent pipeline (chords, drums, bass).
- Scope: medium-level flow, invariants, and testing/handling guidance (no code).

## Data flow
- User input → normalized input
  - Inputs: raw BPM, chord string (optional), mood tag.
  - Outputs: normalized input object (typed BPM, tokenized/canonical chords, normalized mood), warnings/errors.
  - Invariants: BPM clamped to allowed range; mood must resolve to a known profile or fallback.
- Normalized input → session plan
  - Inputs: normalized input, selected mood profile.
  - Outputs: session plan with structure blocks (e.g., intro/loop/outro or 12-bar), harmony length, variation rate, deterministic seed, and rhythm grid config.
  - Invariants: one global seed; structure maps to whole bars; grid resolution/time signature consistent across layers.
- Session plan → chords/drums/bass layers
  - Inputs: session plan, mood profile, shared rhythm grid.
  - Outputs: chord events, drum tracks, bass notes positioned on the same grid; section markers.
  - Invariants: all layers share BPM/resolution/feel; chord anchors are honored; no illegal chord transitions outside profile; fills/accents align to bar boundaries when specified.
- Layers → export artifacts
  - Inputs: grid, generated layers, metadata (mood_id, bpm, seed, schema version).
  - Outputs: symbolic export plan (MIDI-ish channel/tick mapping or JSON event lists), no audio.
  - Invariants: events reference valid grid steps; channel assignments remain consistent; no rendering or samples included.

## Error handling
- Warnings: non-fatal adjustments during parsing/normalization (e.g., BPM clamping, chord canonicalization, mood fallback), optional density/swing defaults applied.
- Errors: invalid/unknown mood with no fallback, unsupported chord tokens, tempo outside safe bounds when clamping is disallowed, malformed input payloads. Errors stop planning/generation.
- Aggregation: collect warnings/errors per stage; surface through API/CLI responses; keep seeds and partial context for debugging when safe.

## Testing strategy
- Unit tests: parsing/validation (BPM, mood normalization, chord token checks), grid math (step counts, timestamps), seed handling utilities.
- Property tests: Markov chains stay within allowed states; weighted sampling approximates declared distributions; illegal transitions never emitted; seed reproducibility yields identical layers.
- Consistency tests: all layers align on the same grid (steps/time signatures match); section boundaries line up across chords/drums/bass; export plan mirrors layer lengths and metadata.

## Notes
- Layer responsibilities: `agent/` (parse/plan/orchestrate), `music/` (chord/drum/bass generation), `data/` (mood profiles, sample templates), `export/` (symbolic mapping), `utils/` (validation, RNG, grid helpers), `api/` (HTTP contracts).
- Sequence diagrams and interaction contracts can be added later to illustrate the above flow once concrete types are defined.
