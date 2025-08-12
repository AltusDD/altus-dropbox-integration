# Table `file_sync_audit`

**Primary Key:** `id, id, id, id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int8` | `NO` | `` |
| `timestamp` | `timestamptz` | `NO` | `now()` |
| `event_type` | `text` | `NO` | `` |
| `dropbox_path` | `text` | `NO` | `` |
| `status` | `text` | `NO` | `` |
| `error_message` | `text` | `YES` | `` |
| `triggered_by` | `text` | `NO` | `` |

## Indexes

- `file_sync_audit_pkey` — `CREATE UNIQUE INDEX file_sync_audit_pkey ON public.file_sync_audit USING btree (id)`
- `idx_file_sync_audit_event` — `CREATE INDEX idx_file_sync_audit_event ON public.file_sync_audit USING btree (event_type)`
- `idx_file_sync_audit_ts` — `CREATE INDEX idx_file_sync_audit_ts ON public.file_sync_audit USING btree ("timestamp")`