# API Contract (Spec)
- Scope: HTTP interface for the symbolic generator. Contract-level only; no framework details.

## Routes

### POST /generate-track
- Request body (JSON):
  - `mood_id` (string, optional): e.g., `lofi_chill`, `blues_gritty`, `jazz_relaxed`.
  - `tempo` (number, optional): BPM, 40–220.
  - `bars` (integer, optional): 4–64; defaults from mood/structure.
  - `chords` (string, optional): comma/bar-separated chord symbols.
  - `seed` (string, optional): deterministic seed; auto-generated if missing.
- Responses:
  - 200 OK:
    ```json
    {
      "track_package": { /* grid, layers, sections, metadata */ },
      "export_plan": { /* canonical events, metadata */ },
      "warnings": [ { "code": "tempo_clamped", "message": "...", "field": "tempo" } ]
    }
    ```
  - 400 Bad Request:
    ```json
    { "errors": [ { "code": "invalid_chords", "message": "...", "field": "chords" } ], "warnings": [] }
    ```
  - 500 Internal Server Error: unexpected failures.

### GET /tracks/{id}
- Purpose: retrieve a previously generated track/export by ID (if persistence is added).
- Path params: `id` (string).
- Responses:
  - 200 OK:
    ```json
    { "track_package": { ... }, "export_plan": { ... }, "metadata": { "id": "..." } }
    ```
  - 404 Not Found: unknown ID.

### GET /profiles
- Purpose: list available mood/style profiles.
- Responses:
  - 200 OK:
    ```json
    { "profiles": [ { "id": "lofi_chill", "description": "..." }, ... ] }
    ```

### GET /health
- Purpose: health probe.
- Responses:
  - 200 OK: `{ "status": "ok" }`

## Auth and rate limiting
- Default: local development, unauthenticated, no rate limiting.
- Future: optional API key header (e.g., `x-api-key`) for hosted scenarios; simple rate limits per key/IP can be added later. Contract should allow 401/429 responses if enabled.
