# Input Parsing (Stub)
- Intent: normalize user-provided BPM, chord sequence string, mood tag.

```
function parse_user_input(raw_bpm, raw_chords, raw_mood):
    TODO: coerce BPM to integer; clamp to allowed range
    tokens = split_chord_string(raw_chords)  # e.g., "Cmaj7,F7,Bb7"
    normalized_chords = canonicalize_symbols(tokens)
    mood = normalize_mood_tag(raw_mood, allowed=["lofi", "blues", "jazz"])
    return { bpm: bpm_value, chords: normalized_chords, mood: mood }
```

- Edge considerations (descriptive):
  - Missing chord string → allow Markov-based generation from mood profile.
  - Unsupported mood → fallback strategy TBD.
  - TODO: collect validation warnings vs hard errors.
