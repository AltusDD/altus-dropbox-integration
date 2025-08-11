# Altus Empire-grade Pack (1–5)
Generated: 2025-08-11 20:24:14 UTC

## IMPORTANT – WHERE TO EXTRACT
Extract this ZIP **into the root of your existing Azure Functions repo** — the same folder that already contains:
- `host.json`
- `requirements.txt`
- `.github/`
- `lib/`
- `functions/`

After extraction, your tree will gain/replace files under `lib/`, `functions/`, and `db/migrations/`.
Then **commit & push to `main`**. Your GitHub Actions deploy will package and publish automatically.

---

This pack includes the 5 upgrades:

1) **Idempotent uploads** (drop-in replacement)
   - Replaces `functions/dropbox_upload/__init__.py` to support an `Idempotency-Key` header.
   - Adds a Supabase table `upload_requests` to store/return prior results (prevents duplicate uploads on retries).

2) **Drift Detector** (Timer trigger)
   - New function `functions/drift_detector` that runs nightly (5 AM UTC) to heal missing folders for Owners/Properties/Units/Tenancies based on Supabase reference tables.
   - Logs findings to `drift_audit` table.

3) **Large-file Upload Sessions**
   - New function `functions/upload_session` with actions: `start`, `append`, `finish`.
   - Clients use this for >150MB files without base64-ing entire file in one request.

4) **Dropbox Team Space Migration Helper**
   - New function `functions/migrate_to_teamspace` that copies files from the current App Folder to a Team Space app using a **second Dropbox credential** set.
   - You add new app settings: `TEAM_DROPBOX_APP_KEY`, `TEAM_DROPBOX_APP_SECRET`, `TEAM_DROPBOX_REFRESH_TOKEN`.

5) **Deal Room / Field App Ingest Endpoint**
   - New function `functions/ingest_upload` that accepts `source = "dealroom" | "fieldapp"` and maps their native payloads to our canonical upload (then writes file & file_assets).

## One-time DB migrations (run in Supabase → SQL editor)
Run these, in order:
- `db/migrations/V4__idempotency.sql`
- `db/migrations/V5__drift.sql`
- `db/migrations/V6__teamspace.sql`

## New/Updated App Settings (Azure → Function App → Configuration)
- **Existing**: `DROPBOX_APP_KEY`, `DROPBOX_APP_SECRET`, `DROPBOX_REFRESH_TOKEN`, `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`
- **New (Team Space migration only)**: `TEAM_DROPBOX_APP_KEY`, `TEAM_DROPBOX_APP_SECRET`, `TEAM_DROPBOX_REFRESH_TOKEN`
- **Optional (ingest)**: none required beyond existing

## Quick Tests (Azure → Function → Code + Test)
- `drift_detector` → Run (no body). See logs & `drift_audit` in Supabase.
- `upload_session` → `POST /api/upload_session/start` with the sample in `/samples/upload_session_start.json`.
- `ingest_upload` → Paste `/samples/ingest_fieldapp.json` or `/samples/ingest_dealroom.json`.
