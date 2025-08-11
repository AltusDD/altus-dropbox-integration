Altus Empire-Grade Dropbox Integration (Owner → Property → Unit → Lease)

Endpoints
---------
- POST /api/dropbox_provision_folders
- POST /api/upload
- GET  /api/get_temp_link
- GET  /api/health

Environment Settings (in Azure Function App → Configuration):
- DROPBOX_APP_KEY
- DROPBOX_APP_SECRET
- DROPBOX_REFRESH_TOKEN
- SUPABASE_URL (e.g. https://<project>.supabase.co)
- SUPABASE_SERVICE_ROLE_KEY

Notes
-----
- This package preserves your existing property tree under /Altus_Empire_Command_Center/01_Properties
- Adds an Owner namespace at /00_Owners
- Safe to deploy over existing app; functions are idempotent on folder creation.
