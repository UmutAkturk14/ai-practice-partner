# Export Module Outline (MIDI/WAV Future Work)
- Goal: translate symbolic track data into MIDI files or WAV renders (later).

- Export staging pseudocode:
```
function stage_export(track, plan, mood_profile):
    midi_plan = map_layers_to_midi_channels(track)
    wav_plan = plan_audio_rendering(track, mood_profile)
    return { midi: midi_plan, wav: wav_plan, bpm: plan.bpm }
```

- MIDI plan (descriptive):
  - Assign channels: chords, bass, drums.
  - Convert grid steps to ticks using BPM and resolution.
  - Velocity placeholders derived from mood dynamics.

- WAV plan (descriptive):
  - Reference to future synth/sample choices (not implemented).
  - Render order: chords → bass → drums → post-process.
  - TODO: offline bounce vs real-time rendering decision.

- TODO:
  - Define file naming conventions.
  - Add metadata tags (mood, BPM, generated_at timestamp).
