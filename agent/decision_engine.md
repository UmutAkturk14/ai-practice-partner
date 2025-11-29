# Decision Engine / Session Plan (Spec)
- Purpose: build a deterministic session plan that drives chord/drum/bass generators based on normalized input and mood profile.

## What is a session plan?
- Structured object describing the track layout and generation parameters:
  - `tempo`: BPM.
  - `mood_id`: selected style (e.g., `lofi_chill`, `blues_gritty`, `jazz_relaxed`).
  - `seed`: deterministic seed for reproducibility.
  - `structure`: ordered blocks with names, bar counts, style tags, and intensity.
  - `grid`: rhythm grid config (resolution, swing/feel, time signature, bars).
  - `variation_rate`: 0–1 scalar guiding how often to vary patterns.
  - `density`: per-layer density hints carried from mood profile.
  - `chord_anchors`: user-provided chord symbols with optional bar anchors.

## How the engine makes choices
- Choose template by mood/style:
  - `lofi`: loop template (intro + loop + outro), moderate swing; uses `structure.template = loop`.
  - `blues`: 12-bar template with shuffle feel; uses `structure.template = 12-bar`.
  - `jazz`: ii–V–I bias with looped sections; uses `structure.template = loop` with ii–V–I anchors.
- Determine block lengths:
  - Intro: 2–4 bars (mood-dependent).
  - Loop/core: 8 bars for lofi/jazz; 12 bars for blues.
  - Outro: 2–4 bars.
  - Total bars must align with grid resolution and time signature.
- Apply mood parameters:
  - `density` and `variation_rate` pulled from mood profile to guide layer generators.
  - `swing/feel` and `resolution` set grid feel.
  - `drum_archetype` and `bass_movement` stored as hints for downstream modules.

## Random seed usage
- One seed per session governs stochastic choices (structure variants when applicable, Markov sampling, fills/accents, bass passing tones).
- Invariant: same normalized input + same seed → identical session plan and downstream layer choices.
- Seed generation occurs during parsing if not provided; decision engine must carry it through unchanged.

## Example session plans (JSON-like)
- Lofi loop
```json
{
  "tempo": 80,
  "mood_id": "lofi_chill",
  "seed": "sess-001",
  "structure": [
    { "name": "intro", "bars": 2, "style": "lofi", "intensity": 0.4 },
    { "name": "loop", "bars": 8, "style": "lofi", "intensity": 0.6 },
    { "name": "outro", "bars": 2, "style": "lofi", "intensity": 0.3 }
  ],
  "grid": { "resolution": 16, "swing": 0.12, "time_signature": { "beats_per_bar": 4, "beat_unit": 4 }, "bars": 12 },
  "variation_rate": 0.25,
  "density": { "chords": 0.4, "drums": 0.35, "bass": 0.3 },
  "chord_anchors": ["i-7", "iv-7", "bVIImaj7", "i-7"]
}
```
- Blues 12-bar
```json
{
  "tempo": 105,
  "mood_id": "blues_gritty",
  "seed": "sess-002",
  "structure": [
    { "name": "12-bar", "bars": 12, "style": "blues", "intensity": 0.6 },
    { "name": "outro", "bars": 2, "style": "blues", "intensity": 0.4 }
  ],
  "grid": { "resolution": 12, "swing": 0.22, "time_signature": { "beats_per_bar": 4, "beat_unit": 4 }, "bars": 14 },
  "variation_rate": 0.35,
  "density": { "chords": 0.5, "drums": 0.55, "bass": 0.55 },
  "chord_anchors": ["I7","IV7","I7","I7","IV7","IV7","I7","I7","V7","IV7","I7","V7"]
}
```
- Jazz ii–V–I loop
```json
{
  "tempo": 120,
  "mood_id": "jazz_relaxed",
  "seed": "sess-003",
  "structure": [
    { "name": "intro", "bars": 2, "style": "jazz", "intensity": 0.5 },
    { "name": "loop", "bars": 8, "style": "jazz", "intensity": 0.65 },
    { "name": "outro", "bars": 2, "style": "jazz", "intensity": 0.35 }
  ],
  "grid": { "resolution": 16, "swing": 0.2, "time_signature": { "beats_per_bar": 4, "beat_unit": 4 }, "bars": 12 },
  "variation_rate": 0.45,
  "density": { "chords": 0.55, "drums": 0.5, "bass": 0.5 },
  "chord_anchors": ["ii-7","V7","Imaj7","Imaj7"]
}
```

## Consumption by generators
- Chord generator uses `structure`, `chord_anchors`, `variation_rate`, and mood `chord_tendencies`.
- Drum generator uses `grid`, `structure` (for fills), mood `drum_archetype`, `density`, and `variation_rate`.
- Bass generator uses `structure`, `chord_anchors` (roots), mood `bass_movement`, `density`, and `variation_rate`.
- Export uses `grid`, `structure`, and `seed`/`mood_id` to attach metadata and ensure alignment across layers.
