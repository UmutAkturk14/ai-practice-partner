# Decision Engine (Abstract)
- Purpose: choose generation strategies and parameters based on mood and user intent.

```
function draft_session_plan(parsed_input):
    plan = {}
    plan.bpm = parsed_input.bpm
    plan.mood = parsed_input.mood
    plan.chord_seed = parsed_input.chords
    plan.random_seed = TODO_assign_seed()

    plan.structure = select_structure(mood=plan.mood)  # e.g., intro + 8-bar loop + outro
    plan.harmony_length = estimate_length(plan.chord_seed, plan.structure)
    plan.variation_rate = pick_variation_rate(mood=plan.mood)
    return plan
```

- Selection heuristics (descriptive):
  - `lofi`: low variation_rate; loop-friendly structure.
  - `blues`: 12-bar bias; shuffle grid flag.
  - `jazz`: ii-V-I emphasis; more harmonic substitutions allowed.

- TODO:
  - Deterministic seed injection.
  - Configurable structure templates per user skill level.
