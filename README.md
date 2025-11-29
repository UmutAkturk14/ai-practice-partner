# AI Practice Partner

## What this project does
- Symbolic backing-track generator (no audio rendering), focused on practice use.
- Generates chords, drums, and bass only (no melody yet).
- Target genres: lofi loops, 12-bar blues, and jazz ii–V–I flavors.
- Pipeline sketch: user input → validation/decision engine → per-layer generators → symbolic export (MIDI-ish/JSON descriptors).

## Scope and non-goals
- No audio rendering, mixing, or sample playback yet.
- No complex UI; intent is local CLI or simple HTTP API only.
- No user accounts, auth, or multi-user features.

## Current status
- Documentation/spec design only: comments, pseudocode, and architecture notes.
- Implementation will follow once specs and algorithms stabilize.

## Data model
- Mood profiles: tempo ranges, rhythmic density, swing/feel, and harmonic bias (Markov tendencies) stored in `data/` and validated by utilities.
- Grid/events: rhythm grids carry BPM, resolution, swing, bars, and time signature; events include chord symbols with position/duration tags, drum hits per grid step, and bass notes with pitch/duration/velocity placeholders. See `docs/data_schemas.md`.

## Pipeline stages
- Input parsing & validation: normalize BPM, chord sequence, and mood tag; collect warnings/errors. Planned in `agent/input_parser.*`.
- Decision engine: build session plan (structure blocks like intro/loop/outro or 12-bar), harmony length, variation rate, and seed selection based on mood profile. Planned in `agent/decision_engine.*`.
- Layer generators:
  - Chords: Markov-ish progression generator with optional user anchors. See `music/chords.*`.
  - Drums: rhythm-grid builder with swing/shuffle flags and accent/fill rules. See `music/drums.*`.
  - Bass: patterns aligned to chord roots and groove heuristics. See `music/bass.*`.
- Export: convert layers + grid into symbolic export plan (MIDI channel/tick mapping or JSON event lists) for future renderers. See `export/export_outline.*`.

## High-level architecture
- Input/validation: ingest BPM, chord string, mood tag; normalize and report issues.
- Decision engine/session plan: pick structure template, length, variation, and seed; bind to a mood profile.
- Layer generators: chords (Markov), drums (grid with swing/shuffle), bass (root-based patterns with passing tones).
- Export layer: build symbolic descriptors for future MIDI/WAV renderers.
- Interfaces: optional thin HTTP API or CLI around the pipeline.

## Data flow
- User input → normalized input
  - Inputs: raw BPM, chord string (optional), mood tag.
  - Outputs: typed/normalized input object, warnings/errors.
  - Invariants: BPM clamped to allowed range; mood must be known or mapped to default.
- Normalized input → session plan
  - Inputs: normalized input, mood profile.
  - Outputs: session plan (structure blocks, target bars/length, variation rate, seed).
  - Invariants: one global seed; structure must map to grid-friendly bar counts.
- Session plan → chords/drums/bass layers
  - Inputs: plan, mood profile, shared rhythm grid.
  - Outputs: chord events, drum tracks, bass notes on the same grid.
  - Invariants: all layers share grid resolution/BPM/swing; chord anchors respected when provided.
- Layers → export artifacts
  - Inputs: grid + layers + metadata (mood, seed, bpm).
  - Outputs: symbolic export plan (MIDI-ish channels/ticks, JSON event lists).
  - Invariants: no audio payloads; events reference the same grid steps.

## Style presets / moods
- Lofi: swing/loose feel, sparse drums, minor-leaning harmony, loop-friendly structure.
- Blues: 12-bar form bias, shuffle feel, dominant harmony, walking/sparse bass options.
- Jazz: ii–V–I emphasis, extended harmonies, ride/ghost-note drum flavor, chromatic bass approaches.
- Mood profile files encode these biases and feed the decision engine.

## Determinism and randomness
- Deterministic seeds drive Markov sampling and pattern choices for reproducibility; centralized in `utils/`.
- Stochastic choices: chord transitions (weighted), drum accents/fills, bass passing/approach tones—all must honor the seed.

## Error handling
- Warnings: collected during parsing/normalization (e.g., chord canonicalization, mood fallback, BPM clamping).
- Errors: invalid/unknown mood IDs with no fallback, unsupported chord tokens, impossible tempo values. Parsing stops and reports errors before planning.
- Error/warning aggregation should be surfaced by the API/CLI wrappers.

## Testing strategy
- Unit tests: parsing/validation (BPM clamping, mood normalization, chord token checks), grid math, seed handling.
- Property tests: Markov chains stay within allowed states, weighted sampling approximates distributions, illegal transitions are never emitted.
- Consistency tests: chord/drum/bass layers align on the same grid; export plan reflects layer counts and timing.

## Future extensions
- Audio rendering and mixing pipeline (MIDI to synth/sampler or WAV bounce).
- Melody/topline generation and embellishments.
- Smarter variation across sections and user-tunable dynamics.

## How to navigate this repo
- `DESIGN.md`: system architecture overview and goals.
- `docs/architecture_notes.md`: documentation TODOs and diagrams-to-be.
- `agent/*.md`: input parsing, decision engine, and pipeline orchestration stubs.
- `music/*.md`: chord, drum, and bass generation outlines.
- `data/*.md`: mood profile schema and sample set placeholders.
- `export/export_outline.md`: planned MIDI/WAV export staging.
- `api/routes.md`: planned HTTP endpoints and contracts.

## Development setup
- Requires Python 3.10+. Create a virtualenv and install dev tools:
  - `pip install -e .[dev]` (or `pip install -r requirements.txt` for runtime libs only).
- Run tests with `pytest`.
- Code style: `black` + `isort`; type checks with `mypy` (per `pyproject.toml`).
