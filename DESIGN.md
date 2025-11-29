# System Architecture (Abstract)

## Overview
- Agentic pipeline that converts user intent (BPM, chord sequence, mood) into symbolic backing tracks (chords, drums, bass) with export hooks.
- No runtime logic yet; this document is conceptual guidance for upcoming implementation.
- All output is symbolic (grids/events/MIDI-ish descriptors), not audio rendering.

## Data model
- Mood profiles: tempo ranges, rhythmic density, swing/feel, harmonic bias (transition tendencies), drum archetypes, and bass movement hints. Planned storage in `data/` (JSON/YAML) with validation utilities.
- Grid/events: rhythm grid carries BPM, resolution, bars, time signature, swing/feel. Events include chord symbols with position/duration tags, drum hits per grid step/track, and bass notes with pitch/duration/velocity placeholders. See `docs/data_schemas.md` for shapes.

## Pipeline stages
- Input parsing & validation: ingest BPM, chord sequence, mood tag; normalize, clamp, canonicalize, and collect warnings/errors. Implementation will live in `agent/input_parser.*`.
- Decision engine: build a session plan with structure blocks (intro/loop/outro or 12-bar), harmony length, variation rate, and deterministic seed selection based on mood profile. Implementation will live in `agent/decision_engine.*`.
- Per-layer generators:
  - Chords: Markov-ish progression using mood tendencies and optional user anchors. See `music/chords.*`.
  - Drums: rhythm-grid patterns with swing/shuffle flags, accent rules, and optional fills. See `music/drums.*`.
  - Bass: patterns aligned to chord roots and groove heuristics (passing/approach tones). See `music/bass.*`.
- Export: map layers + grid to symbolic artifacts (MIDI channel/tick plans or JSON event lists) for future rendering. Implementation notes in `export/export_outline.*`.

## Style presets / moods
- Lofi: swing/loose feel, sparse drums, minor-leaning harmony, loop-friendly structure.
- Blues: 12-bar bias, shuffle feel, dominant harmony, walking/sparse bass options.
- Jazz: ii–V–I emphasis, extended harmonies, ride/ghost-note flavor, chromatic bass approaches.
- Mood profile files encode these biases and drive the decision engine.

## Determinism and randomness
- Deterministic seeds govern Markov sampling and pattern choices for reproducible tracks; seed utilities will live in `utils/`.
- Stochastic elements include chord transitions (weighted), drum accent/fill placement, and bass passing tones; all must honor the seed for repeatability.

## Future extensions
- Audio rendering/mixing pipeline (MIDI to synth/sampler or WAV bounce).
- Melody/topline generation and embellishments.
- Persistence, richer API/CLI tooling, and user-tunable dynamics.

## Notes for implementation
- Concrete data structures and serializers will be added alongside code.
- Deterministic seeding and reproducibility tools belong in `utils/`.
- CLI/API wiring will wrap the agent pipeline once core generation is in place.
