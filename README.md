
# Altus Dropbox Integration (Azure Functions)

**Endpoints** (use `?code=...`):
- POST `/api/dropbox_provision_folders`
- POST `/api/upload`
- GET  `/api/get_temp_link?id=...`
- GET  `/api/health`

## Deploy (fast)
1) Push these files to your GitHub repo (main branch).
2) Add repo **Secrets**: `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`, `AZURE_RESOURCE_GROUP`, `AZURE_FUNCTIONAPP_NAME`.
3) In Azure → Function App → **Configuration** add: `DROPBOX_APP_KEY`, `DROPBOX_APP_SECRET`, `DROPBOX_REFRESH_TOKEN`, `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY` → Save + Restart.
4) GitHub → **Actions** → **Deploy to Azure (OIDC)** → Run workflow.
5) Test `dbx_health` function URL.

## Supabase SQL
Run `db/migrations/001_init.sql` to create `file_sync_audit` and `file_assets`.
Optionally run `db/migrations/002_triggers.sql` after deploy (fill in your host + function key).
