# Altus Empire Dropbox Rollout — Implementation Pack

## Quick start
1) Run the builder:
   ```bash
   python build_altus_pack_fixed.py
   ```
2) Upload `altus_dropbox_pack.zip` to Replit (Create Repl → Import from ZIP),
   or push the `altus_dropbox_pack/` folder to GitHub.
3) In Supabase, run `db/migrations/001_init.sql` (edit `YOUR_FUNCTION_HOST`).
4) In Azure Function App, set app settings for `DROPBOX_*`, `SUPABASE_*`, and `AzureWebJobsStorage`.

**Endpoints**
- `POST /api/dropbox_provision_folders`
- `POST /api/upload`
- `GET  /api/get_temp_link?id=<asset_id>`
