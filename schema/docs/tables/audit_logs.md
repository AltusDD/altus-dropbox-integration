# Table `audit_logs`

**Primary Key:** `id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int8` | `NO` | `` |
| `batch_id` | `uuid` | `YES` | `` |
| `status` | `text` | `YES` | `` |
| `entity` | `text` | `YES` | `` |
| `entity_type` | `text` | `YES` | `` |
| `message` | `text` | `YES` | `` |
| `timestamp` | `timestamptz` | `YES` | `now()` |

## Indexes

- `audit_logs_pkey` — `CREATE UNIQUE INDEX audit_logs_pkey ON public.audit_logs USING btree (id)`