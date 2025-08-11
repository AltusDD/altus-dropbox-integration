
Altus Transfer Pack (Owner → Owner, ID-stable)

What this adds
- New Azure Function: POST /api/transfer_property_owner
- DB migration for property ownership legs & transfer audit

How to install
1) Extract into your repo root (it will create:
   - functions/transfer_property_owner/
   - db/migrations/V3__ownerships.sql
)
2) Commit & push to main. Wait for the Deploy workflow to go green.
3) In Supabase → SQL, run db/migrations/V3__ownerships.sql once.

How to run a transfer (example)
POST https://<your-func>.azurewebsites.net/api/transfer_property_owner?code=<KEY>
Body:
{
  "property_id": 201,
  "property_name": "Sunset Villas",
  "from_owner_id": 101,
  "from_owner_name": "Sunset Capital Partners",
  "to_owner_id": 555,
  "to_owner_name": "Rising Tide Holdings",
  "cutoff_date": "2025-08-15",
  "leave_marker": true
}

What it does
- Moves the ENTIRE property folder tree from Owner A to Owner B path in Dropbox
- Updates all matching file_assets.dropbox_path from old prefix to new prefix
- Closes existing property_ownerships leg for Owner A (end_date = cutoff - 1s)
- Opens new leg for Owner B (start_date = cutoff_date)
- Creates an optional marker file under Owner A/99_Dispositions/<property>/

Idempotency
- If destination property path already exists, the move is treated as already done.
- DB relinking is done by prefix replacement for rows where dropbox_path LIKE 'src%'
