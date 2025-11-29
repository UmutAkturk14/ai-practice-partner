# Drum Pattern Generation (Spec)
- Goal: produce drum tracks (kick, snare, hats, optional perc) on a shared rhythm grid, guided by mood/style and density.

## Grid representation
- `resolution`: steps per beat (e.g., 4, 8, 12 for shuffle, or 16).
- `bars`: number of bars to generate; total steps = `bars * beats_per_bar * resolution` (assume 4/4 unless specified).
- `tracks`: map of instrument → array of hit intensities (0–1) sized to total steps.
- Supported instruments: `kick`, `snare`, `hihat` (open/closed can be tags), `perc` (optional).
- Swing/shuffle: represented as timing offset metadata on off-beat steps (e.g., `swing = 0.0–0.3`), inherited from mood/grid.

## Style bases
- Lofi backbeat:
  - Resolution: 16, swing modest (0.1–0.16).
  - Backbeat snare on beats 2 and 4; sparse kicks (beats 1 and 3 variants); hats with low density and slight dynamics.
- Blues shuffle:
  - Resolution: 12 (triplet subdivision) or 24 for finer detail; swing ~0.2–0.25.
  - Backbeat snare; shuffle hats (on triplet off-beats); occasional pickup kicks.
- Jazz ride/comping:
  - Resolution: 16, swing ~0.18–0.22.
  - Ride pattern bias (spang-spang-a-lang feel on hats/ride); light snare comping/ghosts; soft feathered kick optional.

## Density mapping
- Mood `density.drums` scales hit probabilities and ghost note insertion:
  - Low density: fewer kicks, softer hats, minimal fills.
  - Higher density: more syncopation, added ghost notes, occasional extra hats.
- Ghost notes represented as low-intensity hits (e.g., 0.2–0.3) on snare/perc tracks.

## Swing/shuffle handling
- Swing factor from mood/grid applies to off-beats:
  - For straight grids (16th), delay every second 8th by swing percentage.
  - For shuffle (triplet) grids, emphasize first+third triplet, de-emphasize middle.
- Stored as metadata; no audio rendering, but timing offsets carried to export.

## Fills
- Placement: near section transitions (last bar before a new block) or every N bars based on variation_rate.
- Differences from regular bars: increased snare/tom/perc activity, denser hats, optional kick pickups.
- Controlled by mood density/variation_rate; tagged in track data to signal variation.

## Example patterns (conceptual)
- Lofi (4 bars, resolution 16, swing 0.12)
  - Kick: hits on 1, 3; occasional offbeat at 3e.
  - Snare: hits on 2, 4; ghost on 4e at low intensity.
  - Hats: steady 8ths with slight dynamics (0.5–0.6).
- Blues shuffle (2 bars, resolution 12, swing 0.22)
  - Kick: on 1 and 3; pickups on 2+ (triplet-off).
  - Snare: on 2 and 4; occasional flam/ghost on triplet preceding 4.
  - Hats: shuffle (hits on triplet 1 and 3; middle triplet softer or absent).
- Jazz ride + comping (4 bars, resolution 16, swing 0.2)
  - Ride/Hat: spang-spang-a-lang (on beats 1, the “and” swung, and beat 3), dynamics varied.
  - Snare: light comps on “and” of 2/4 with ghost notes.
  - Kick: feathered on quarter notes at low intensity (optional).

## Outputs and invariants
- Outputs: drum layer with tracks aligned to the shared grid; fills tagged where applied.
- Invariants:
  - Uses grid resolution/feel from session plan/mood.
  - Length matches session structure (bars).
  - Seed-driven randomness for hit placement and fills; same seed + inputs → same pattern.
  - Intensities stay within 0–1; supported instruments only unless extended explicitly.
