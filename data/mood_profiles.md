# Mood Profiles (Schema & Examples)

## Schema
JSON-like shape describing style presets. Fields are symbolic only (no audio data).
```json
{
  "schema_version": "0.1.0",          // required
  "id": "lofi_chill",                 // required, slug
  "description": "Mellow lofi loop",  // required
  "tempo_bpm": {                      // required
    "default": 80,
    "min": 65,
    "max": 90
  },
  "swing": 0.12,                      // required, 0–1 swing/shuffle amount
  "density": {                        // required, 0–1 per layer
    "chords": 0.4,
    "drums": 0.35,
    "bass": 0.3
  },
  "harmonic_bias": {                  // required
    "extensions": 0.6,                // likelihood of 7/9/11/13 color
    "dissonance": 0.2,                // altered tones/tension
    "complexity": 0.4                 // substitution/turnaround frequency
  },
  "variation_rate": 0.3,              // required, 0–1 (how often to vary patterns)
  "structure": {                      // optional; defaults to loop of 8 bars
    "template": "loop",
    "bars": 8
  },
  "drum_archetype": "lofi-minimal",   // required, named pattern family
  "bass_movement": "sparse",          // required, e.g., sparse/walking/chromatic
  "chord_tendencies": {               // optional; mood-specific transition hints
    "start_states": [{ "id": "i_min7", "weight": 0.6 }],
    "states": {
      "i_min7": { "label": "i-7", "transitions": { "iv_min7": 0.4, "bVIImaj7": 0.3, "v_min7": 0.3 } }
    }
  }
}
```
- Required fields: `schema_version`, `id`, `description`, `tempo_bpm`, `swing`, `density`, `harmonic_bias`, `variation_rate`, `drum_archetype`, `bass_movement`.
- Optional fields: `structure` (default: loop/8 bars), `chord_tendencies` (default: use genre defaults).
- Defaults imply gentle values (moderate density, low dissonance, simple loop) if omitted.

## Examples

### lofi_chill
```json
{
  "schema_version": "0.1.0",
  "id": "lofi_chill",
  "description": "Warm, mellow lofi loop with sparse drums and soft swing.",
  "tempo_bpm": { "default": 80, "min": 65, "max": 90 },
  "swing": 0.12,
  "density": { "chords": 0.4, "drums": 0.35, "bass": 0.3 },
  "harmonic_bias": { "extensions": 0.6, "dissonance": 0.2, "complexity": 0.4 },
  "variation_rate": 0.25,
  "structure": { "template": "loop", "bars": 8 },
  "drum_archetype": "lofi-minimal",
  "bass_movement": "sparse",
  "chord_tendencies": {
    "start_states": [ { "id": "i_min7", "weight": 0.6 }, { "id": "iv_min7", "weight": 0.4 } ],
    "states": {
      "i_min7": { "label": "i-7", "transitions": { "iv_min7": 0.4, "bVIImaj7": 0.3, "v_min7": 0.3 } },
      "iv_min7": { "label": "iv-7", "transitions": { "bVIImaj7": 0.4, "i_min7": 0.4, "v_min7": 0.2 } },
      "bVIImaj7": { "label": "bVIImaj7", "transitions": { "i_min7": 0.7, "iv_min7": 0.3 } },
      "v_min7": { "label": "v-7", "transitions": { "i_min7": 0.6, "bVIImaj7": 0.4 } }
    }
  }
}
```

### lofi_dark
```json
{
  "schema_version": "0.1.0",
  "id": "lofi_dark",
  "description": "Moody lofi with darker harmony and slightly heavier drums.",
  "tempo_bpm": { "default": 78, "min": 60, "max": 88 },
  "swing": 0.16,
  "density": { "chords": 0.45, "drums": 0.45, "bass": 0.35 },
  "harmonic_bias": { "extensions": 0.5, "dissonance": 0.35, "complexity": 0.45 },
  "variation_rate": 0.3,
  "structure": { "template": "loop", "bars": 8 },
  "drum_archetype": "lofi-dusted",
  "bass_movement": "sparse",
  "chord_tendencies": {
    "start_states": [ { "id": "i_min7", "weight": 0.7 }, { "id": "bVImaj7", "weight": 0.3 } ],
    "states": {
      "i_min7": { "label": "i-7", "transitions": { "bVImaj7": 0.35, "iv_min7": 0.35, "v_min7": 0.3 } },
      "bVImaj7": { "label": "bVImaj7", "transitions": { "i_min7": 0.6, "iv_min7": 0.4 } },
      "iv_min7": { "label": "iv-7", "transitions": { "bVImaj7": 0.3, "i_min7": 0.5, "bVIImaj7": 0.2 } },
      "v_min7": { "label": "v-7", "transitions": { "i_min7": 0.7, "bVImaj7": 0.3 } }
    }
  }
}
```

### blues_gritty
```json
{
  "schema_version": "0.1.0",
  "id": "blues_gritty",
  "description": "Shuffly 12-bar blues with dominant harmony and walking bass bias.",
  "tempo_bpm": { "default": 105, "min": 85, "max": 125 },
  "swing": 0.22,
  "density": { "chords": 0.5, "drums": 0.55, "bass": 0.55 },
  "harmonic_bias": { "extensions": 0.35, "dissonance": 0.25, "complexity": 0.3 },
  "variation_rate": 0.35,
  "structure": { "template": "12-bar", "bars": 12 },
  "drum_archetype": "blues-shuffle",
  "bass_movement": "walking",
  "chord_tendencies": {
    "start_states": [ { "id": "I7", "weight": 0.8 }, { "id": "IV7", "weight": 0.2 } ],
    "states": {
      "I7": { "label": "I7", "transitions": { "IV7": 0.35, "V7": 0.25, "I7": 0.4 } },
      "IV7": { "label": "IV7", "transitions": { "I7": 0.4, "V7": 0.3, "IV7": 0.3 } },
      "V7": { "label": "V7", "transitions": { "IV7": 0.4, "I7": 0.6 } }
    }
  }
}
```

### jazz_relaxed
```json
{
  "schema_version": "0.1.0",
  "id": "jazz_relaxed",
  "description": "Laid-back jazz with ii–V–I bias, ride cymbal feel, and chromatic bass approaches.",
  "tempo_bpm": { "default": 120, "min": 95, "max": 140 },
  "swing": 0.2,
  "density": { "chords": 0.55, "drums": 0.5, "bass": 0.5 },
  "harmonic_bias": { "extensions": 0.75, "dissonance": 0.35, "complexity": 0.6 },
  "variation_rate": 0.45,
  "structure": { "template": "loop", "bars": 8 },
  "drum_archetype": "jazz-ride",
  "bass_movement": "chromatic",
  "chord_tendencies": {
    "start_states": [ { "id": "ii_min7", "weight": 0.5 }, { "id": "Imaj7", "weight": 0.5 } ],
    "states": {
      "ii_min7": { "label": "ii-7", "transitions": { "V7": 0.6, "ii_min7": 0.2, "Imaj7": 0.2 } },
      "V7": { "label": "V7", "transitions": { "Imaj7": 0.7, "ii_min7": 0.3 } },
      "Imaj7": { "label": "Imaj7", "transitions": { "ii_min7": 0.5, "IVmaj7": 0.25, "vi_min7": 0.25 } },
      "IVmaj7": { "label": "IVmaj7", "transitions": { "ii_min7": 0.6, "V7": 0.4 } },
      "vi_min7": { "label": "vi-7", "transitions": { "ii_min7": 0.5, "V7": 0.5 } }
    }
  }
}
```

## Versioning
- Include `schema_version` in every profile. Current version: `0.1.0`.
- Evolution approach: bump `schema_version` on breaking schema changes; keep loader/validator backward-compatible where feasible and provide migration notes when fields are renamed or added.
