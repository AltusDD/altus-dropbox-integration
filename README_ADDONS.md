# Altus Add-ons Pack (V1)
Generated: 2025-08-11 20:15:58 UTC

This pack adds:
1) **GET /api/get_temp_link** — Get a short-lived Dropbox URL for a file.
2) **POST /api/bulk_transfer_properties** — Run multiple owner transfers in one shot.
3) **POST /api/doorloop_writeback** — Create a Note + Communication in DoorLoop after a transfer.

## Install (Copy/Paste Agent Mode)
1. Extract this ZIP into the **repo root** (it adds new folders under `functions/` and new samples & readme).
2. Commit and push to `main`. Wait for your GitHub Actions deploy to finish (green).
3. In **Azure → Function App → Configuration → Application settings**, add (or confirm) these:
   - `SUPABASE_URL` (already set)
   - `SUPABASE_SERVICE_ROLE_KEY` (already set)
   - `DROPBOX_APP_KEY`, `DROPBOX_APP_SECRET`, `DROPBOX_REFRESH_TOKEN` (already set)
   - **NEW (optional for bulk):** `SELF_TRANSFER_URL` — your own function URL for transfer, e.g. `https://<app>.azurewebsites.net/api/transfer_property_owner?code=<KEY>`
   - **NEW (optional for DoorLoop writeback):** `DOORLOOP_API_KEY` — your DoorLoop API key (Bearer token)

4. Test each function from **Functions → Code + Test** in the Azure portal using the provided JSON samples in `/samples`.

---

## Endpoints

### 1) GET /api/get_temp_link
**Query params:**
- `asset_id` (preferred): The `file_assets.id` in Supabase.
- OR `path`: A full Dropbox path starting with `/Altus_Empire_Command_Center/...`

**Returns:** `{ "ok": true, "path": "...", "temp_link": "https://..." }`

**Auth:** function key (?code=...)

**Notes:** If `asset_id` is provided, we look up the path from Supabase first to prevent typos.

### 2) POST /api/bulk_transfer_properties
Batch wrapper around your existing `/api/transfer_property_owner` function.
It invokes your own transfer endpoint for each item.

**Body:**
```
{ "transfers": [ {
      "property_id": 201,
      "property_name": "Sunset Villas",
      "from_owner_id": 101,
      "from_owner_name": "Sunset Capital Partners",
      "to_owner_id": 555,
      "to_owner_name": "Rising Tide Holdings",
      "cutoff_date": "2025-08-15",
      "leave_marker": true
} ] }
```

**Where it calls:** The environment variable `SELF_TRANSFER_URL` (must include `?code=...` already).

**Returns:** A per-item status list.

### 3) POST /api/doorloop_writeback
Creates a **Note** and a **Communication** entry in DoorLoop to document the transfer event.
(Per DoorLoop docs: `/api/notes` and `/api/communications` exist. We use a minimal payload; tailor later if needed.)

**Body:**
```
{
  "property_id": 201,
  "from_owner_id": 101,
  "to_owner_id": 555,
  "cutoff_date": "2025-08-15",
  "message": "Ownership transferred from Owner A to Owner B effective 2025-08-15."
}
```

**Auth:** function key (?code=...). Requires `DOORLOOP_API_KEY` app setting.

**Caveat:** DoorLoop's public API does **not** currently expose an endpoint to reassign a property's owner.
This endpoint **logs** the event (note + communication) to keep the systems in sync, but the actual reassignment likely needs to be done in DoorLoop's UI. We can automate it later if DoorLoop adds an API for it.

---

## Samples
See `/samples/` for JSON bodies you can paste directly into Azure's **Code + Test**.

