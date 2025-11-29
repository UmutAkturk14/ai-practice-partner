# Utility Helpers (Spec)
- Purpose: shared helper functions across parsing, planning, generation, and export. Documentation only; no implementation here.

## Time helpers
- `beats_to_ms(bpm, beats) -> milliseconds`
  - Purpose: convert beat count to elapsed milliseconds for scheduling/export metadata.
  - Invariants: monotonic; invertible with `ms_to_beats` up to rounding.
- `ms_to_beats(bpm, milliseconds) -> beats`
  - Purpose: convert elapsed time back to beats.
- `bars_to_steps(bars, beats_per_bar, resolution) -> steps`
  - Purpose: derive total grid steps; assume fixed time signature.
  - Invariants: steps = bars * beats_per_bar * resolution.
- `bar_beat_to_step(bar_index, beat_offset, resolution) -> step_index`
  - Purpose: map musical position to grid step index; beat_offset can be fractional.
- `step_to_timestamp(step_index, bpm, resolution) -> milliseconds`
  - Purpose: map grid step to wall-clock time for export.

Usage (pseudocode):
```
grid_steps = bars_to_steps(bars=4, beats_per_bar=4, resolution=16)  # 256
step_ts = step_to_timestamp(step_index=8, bpm=80, resolution=16)    # ~150ms
```

## Randomness helpers
- `seed_rng(seed_string) -> rng`
  - Purpose: initialize deterministic RNG shared across samplers.
  - Invariants: same seed yields identical sequences across runs.
- `weighted_choice(weights_map, rng) -> key`
  - Purpose: pick a key based on weighted probabilities (e.g., Markov transitions).
  - Invariants: only keys with positive weight are selectable; honors seed.
- `shuffle_with_seed(list, rng) -> list`
  - Purpose: reproducible shuffles for variation ordering.

Usage (pseudocode):
```
rng = seed_rng("session-123")
next_state = weighted_choice({"A": 0.6, "B": 0.4}, rng)
```

## Validation helpers
- `validate_bpm(value, min=40, max=220) -> { bpm, warnings[], errors[] }`
  - Purpose: coerce/clamp BPM and report issues.
- `normalize_mood_tag(raw, allowed_list) -> { mood, warnings[], errors[] }`
  - Purpose: canonicalize mood tag or flag unknown moods.
- `validate_chords(tokens, vocabulary) -> { chords, warnings[], errors[] }`
  - Purpose: ensure chord symbols are known/canonical.
- `validate_profile(profile_obj, schema) -> { ok, warnings[], errors[] }`
  - Purpose: enforce required/optional fields per `data/mood_profiles.md` schema.
- Invariants: return values do not raise; errors array non-empty signals failure; warnings are non-fatal.

Usage (pseudocode):
```
result = validate_bpm(user_bpm, min=60, max=180)
if result.errors: abort()
if result.warnings: log(result.warnings)
```

## Logging / diagnostics
- `collect_warning(message, scope)` / `collect_error(message, scope)`
  - Purpose: aggregate issues by stage (parse/plan/generate/export).
- `debug_dump(label, obj)` 
  - Purpose: capture intermediate data for testing; no external IO in production path.
- Invariants: warnings/errors are structured (message, code, scope); aggregation should preserve order.
