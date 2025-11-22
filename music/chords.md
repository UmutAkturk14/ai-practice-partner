# Chord Generation (Markov Outline)
- State representation:
  - `state = { chord_symbol, phrase_position_tag }`
  - `chord_symbol`: canonical text (e.g., "Cmaj7", "F7").
  - `phrase_position_tag`: labels like START, MID, CADENCE to bias transitions.

- Markov chain construction (pseudocode):
```
function init_markov_chain(tendencies):
    chain = {}
    for each state in tendencies:
        chain[state] = tendencies[state].transitions  # weighted targets
    return chain
```

- Progression generation (pseudocode):
```
function generate_chord_progression(plan, chain):
    length = plan.harmony_length or default_bars
    progression = []
    current = seed_state_from(plan.chord_seed, chain)
    for bar_index in range(length):
        progression.append(current.chord_symbol)
        current = sample_next_state(chain, current, plan.random_seed)
    return progression
```

- TODO notes:
  - No sampling logic implemented; weights remain descriptive.
  - Add hooks for user-specified anchors (force positions in progression).
  - Extend state with mood-specific color tones (e.g., add9, 13).
