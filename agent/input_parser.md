# Input Parsing & Normalization (Spec)
- Purpose: turn raw user input into a normalized object for the decision engine, with warnings/errors collected.

## Inputs
- Expected fields (external API/CLI payload):
  - `mood_id` (string): e.g., `lofi_chill`, `lofi_dark`, `blues_gritty`, `jazz_relaxed`. Default: fallback to project default (e.g., `lofi_chill`) if missing/unknown (with warning).
  - `tempo` (number): BPM. Valid range: 40–220; default from mood profile if missing.
  - `bars` (integer, optional): desired length. Valid range: 4–64; default: derived from mood structure (e.g., 8-bar loop, 12-bar blues).
  - `chords` (string, optional): comma- or bar-separated chord symbols (e.g., `"Cmaj7,Dm7 | G7,Cmaj7"`). May be omitted to allow auto-generation.
  - `seed` (string, optional): deterministic seed; if missing, generate one.
- Valid ranges/defaults: tempo clamped to 40–220; bars clamped to 4–64; mood must resolve to known profile or fallback.

## Normalization rules
- Tempo: coerce to integer; if outside range, clamp and emit warning.
- Bars: coerce to integer; clamp to allowed range; if missing, use mood structure default.
- Mood: lowercase/trim; if not in allowed set, use default mood and emit warning; if unknown and fallback disallowed, emit error.
- Chord string handling:
  - Tokenize on commas and bar separators (`","`, `"|"`, `";"`); trim whitespace.
  - Canonicalize symbols (enharmonic normalization, standard suffixes).
  - Preserve bar separators as anchor hints if present.
  - Unknown/unsupported chord tokens → errors (skip generation), unless configured to drop them with warnings.
- Seed: if provided, use as-is (string). If missing, generate deterministic seed (e.g., UUID) and note in normalized output.

## Error and warning model
- Hard errors (block progression): unknown mood with no fallback, chord tokens all invalid (no anchors), non-numeric tempo that cannot be coerced.
- Warnings (non-fatal): tempo clamped, bars clamped, mood fallback applied, some chord tokens dropped/canonicalized, seed auto-generated.
- Result shape:
  - `normalized_input`: `{ mood_id, tempo, bars, chords: [tokens/anchors], seed }`
  - `warnings`: array of `{ code, message, field }`
  - `errors`: array of `{ code, message, field }`
- Parsing returns both normalized_input and aggregated diagnostics; decision engine only proceeds if `errors` is empty.

## Examples
- Valid input
  - Raw: `{ mood_id: "jazz_relaxed", tempo: 120, bars: 8, chords: "Dm7,G7,Cmaj7,Cmaj7", seed: "abcd" }`
  - Output: normalized_input identical; warnings/errors empty.
- Clamped tempo with warning
  - Raw: `{ mood_id: "lofi_chill", tempo: 20, chords: "Cm7,Fm7,Bbmaj7" }`
  - Output: `tempo: 40` (clamped), `bars: 8` (from mood), chords canonicalized; warnings include tempo_clamped; errors empty.
- Invalid chords
  - Raw: `{ mood_id: "blues_gritty", tempo: 100, chords: "X1,Y2,Z3" }`
  - Output: `chords: []` (no valid tokens), tempo normalized; errors include invalid_chords; parsing should halt before planning.
