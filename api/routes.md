# API Endpoints (Stub Only)
- No server code; only request/response sketches.

- Planned endpoints:
  - `POST /generate`
    - Accepts: BPM, chord sequence, mood.
    - Returns: placeholder export payload (midi_plan, wav_plan) with symbolic data only.
  - `GET /profiles`
    - Returns: available mood profiles and descriptors.

- TODO:
  - Define error schema and validation responses.
  - Add authentication/ratelimiting considerations.
