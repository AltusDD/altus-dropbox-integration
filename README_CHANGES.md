# Altus Dropbox Integration — Patch 2025-08-11

This drop-in patch gives you:
- **OIDC deployment** workflow (`.github/workflows/blessed-deploy.yml`) — no publish profiles, no `az webapp deploy`.
- Clean **Dropbox client** with refresh-token + **chunked uploads** (100MB pieces).
- New **Functions**: `dbx_health`, `dropbox_provision_folders`, `dropbox_upload`, `get_temp_link` (fully wired).
- **SQL migrations** to add safe FKs + KPI materialized view + compliance audit view.

## How to use (copy–paste simple)

1. **Download the ZIP** from ChatGPT and extract it.
2. Drop the contents into the **root of your repo** (it will create/overwrite these paths):
   - `.github/workflows/blessed-deploy.yml`
   - `lib/` (replaces `dropbox_client.py`, adds `naming.py`, `pathmap.py` if missing)
   - `functions/dbx_health/`
   - `functions/dropbox_provision_folders/`
   - `functions/dropbox_upload/`
   - `functions/get_temp_link/`
   - `db/migrations/V2__*.sql`, `V3__*.sql`, `V4__*.sql`
   - `host.json` (safe to overwrite)
   - `requirements.txt` (minimal for Functions; if your repo has extras, keep them)
3. **Commit & push** to `main`.
4. In GitHub → **Actions** → select **Deploy Python Function App to Azure (OIDC)** → **Run workflow**.
5. In Azure Portal → Function App → **Configuration**, ensure these are set:
   - `DROPBOX_APP_KEY`, `DROPBOX_APP_SECRET`, `DROPBOX_REFRESH_TOKEN`
   - `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`
6. **Smoke tests** (Portal → Functions → Code + Test):
   - GET `/api/health` → expect `{"ok": true}`.
   - POST `/api/dropbox_provision_folders` with:
     ```json
     {"entity_type":"property","new":{"id":101,"name":"Sunset Villas"}}
     ```
   - POST `/api/upload` with:
     ```json
     {
       "entity_type": "PropertyPhoto",
       "meta": {"property_name":"Sunset Villas","property_id":101,"actor":"smoke-test"},
       "original_filename": "hello.txt",
       "file_base64": "SGVsbG8sIERyb3Bib3gh"
     }
     ```
   - GET `/api/get_temp_link?id=1` (after insert) → returns a short-lived link.

If anything fails, ping me the error text verbatim and I'll ship a one-line fix.
