# Altus Finishline Pack
Generated: 2025-08-11 20:44:40 UTC

## WHERE TO EXTRACT
Extract this ZIP **into the root of your Azure Functions repo** (same folder as `host.json`, `requirements.txt`, `functions/`, `lib/`). Then commit & push to `main`.

## What’s included
- `functions/get_temp_link` → **GET /api/get_temp_link** (asset_id or path → short-lived Dropbox URL)
- `functions/transfer_property_owner` → **POST /api/transfer_property_owner** (move a property’s entire folder from Owner A to Owner B, update Supabase paths)
- `functions/bulk_transfer_properties` → **POST /api/bulk_transfer_properties** (batch over multiple properties)
- `functions/compliance_audit` → **GET /api/compliance/audit`** (reports missing required docs per business rules)
- `db/migrations/V7__required_documents.sql` → required docs & audit view
- `/samples/` → ready JSON bodies for Code + Test

## Azure App Settings
No new settings required beyond your working DROPBOX_* and SUPABASE_*.

## Test quickly
- In Azure → Function App → Functions → pick function → **Code + Test**.
- Use the bodies under `/samples`.

