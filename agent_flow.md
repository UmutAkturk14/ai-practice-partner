# Agent Flow (Human-Readable)
- End-to-end steps for generating symbolic backing tracks (chords, drums, bass) for lofi, blues, and jazz. Terminology matches README/DESIGN (session plan, structure blocks, rhythm grid).

## Step 1: Parse and normalize input
- Decisions: coerce BPM, tokenize/canonicalize chord string (optional), normalize mood tag (`lofi`, `blues`, `jazz`), collect warnings/errors.
- Specs: see `agent/input_parser.md` and `utils/helpers.md` for validation plans.

## Step 2: Build session/structure plan
- Decisions: choose structure template (intro/loop/outro vs 12-bar), set bar count/section lengths, pick variation rate, assign deterministic seed, select rhythm grid resolution/feel from mood profile.
- Specs: see `agent/decision_engine.md`, mood profile schema in `data/mood_profiles.md`, grid shapes in `docs/data_schemas.md`.

## Step 3: Generate chords
- Decisions: seed starting state (from user anchors or mood defaults), apply Markov tendencies per mood, enforce cadence/anchor rules, target harmony length from session plan.
- Specs: see `music/chords.md` and mood tendencies in `data/mood_profiles.md`.

## Step 4: Generate drums
- Decisions: build rhythm grid using plan BPM/resolution/feel; apply accent rules, kick/snare/hat archetypes, optional fills at section boundaries.
- Specs: see `music/drums.md` and rhythm/grid notes in `docs/data_schemas.md`.

## Step 5: Generate bass
- Decisions: follow chord roots, choose movement pattern (sparse/walking/chromatic) from mood profile, insert passing/approach tones respecting groove, align to grid/sections.
- Specs: see `music/bass.md` and mood bass behavior in `data/mood_profiles.md`.

## Step 6: Export symbolic result
- Decisions: merge layers on the shared grid; map to symbolic export artifacts (MIDI-ish channels/ticks or JSON event lists); attach metadata (mood_id, bpm, seed, sections).
- Specs: see `export/export_outline.md` and data shapes in `docs/data_schemas.md`.

## Control options
- Seeds: one deterministic seed per session drives Markov sampling and pattern choices for reproducibility (managed via `utils/helpers.md`).
- Mood/style influence: mood profiles choose structure templates, grid feel (swing/shuffle), chord tendencies, drum archetypes, and bass movement heuristics.
- User-provided chords: treated as anchors; gaps are auto-filled by the chord generator, but anchors are preserved unless validation fails.
