# Empire Command Center — Schema Pack

This folder is the **canonical source of truth** for the database schema.

- `schema.sql` — auto-generated DDL snapshot (CI keeps this fresh)
- `manifest.json` — machine-readable schema manifest (CI keeps this fresh)
- `DATA_DICTIONARY.md` — human-readable overview
- `docs/tables/*.md` — per-table details

## CI: Schema Sync & Drift Guard
- `.github/workflows/schema-sync.yml` creates/updates `schema.sql` + `manifest.json` via PR on every push.
- `.github/workflows/schema-guards.yml` fails CI when required views or baseline data are missing.

To enable:
1. Add `SUPABASE_DB_URL` to GitHub Actions secrets.
2. Commit both workflows.
