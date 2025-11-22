# Agent Flow (Step-by-Step, Abstract)
1) Accept user input
   - BPM number
   - Chord sequence string (optional; comma-separated symbols)
   - Mood tag (`lofi`, `blues`, `jazz`)

2) Validate + normalize
   - Pseudocode: parse BPM → ensure numeric; tokenize chords → canonicalize; verify mood in known set.
   - TODO: add error collection strategy.

3) Build session context
   - Create conceptual `SessionPlan` with tempo, chord seed, selected mood profile, and random seed placeholder.

4) Analyze samples (symbolic)
   - Stub: reference `data/` mood profiles; no real audio.
   - Derive chord transition weights and rhythm density factors from profile.

5) Generate chord progression (Markov)
   - If user provided chords: use as anchors; fill gaps via Markov transitions.
   - Else: sample start state from mood defaults; iterate transitions to target length.

6) Assemble drum pattern
   - Choose rhythm grid resolution from mood (e.g., 16 steps).
   - Apply mood accent rules to kick/snare/hh slots.

7) Assemble bassline
   - Follow chord roots; insert passing notes depending on mood complexity level.
   - Sync to rhythm grid; respect groove offsets if specified.

8) Merge layers
   - Align chord, drum, bass sequences on shared grid; adjust bar counts.
   - TODO: add intro/outro shaping plan.

9) Prepare export payload
   - Build symbolic event lists for MIDI/WAV adapters.
   - No rendering code; only describe channel assignments and tempo metadata.

10) Return track package
   - Return structured placeholder with layer data and export-ready descriptors.
