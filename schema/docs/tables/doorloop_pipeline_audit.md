# Table `doorloop_pipeline_audit`

**Primary Key:** `id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `uuid` | `NO` | `gen_random_uuid()` |
| `batch_id` | `uuid` | `NO` | `` |
| `status` | `text` | `NO` | `` |
| `entity` | `text` | `NO` | `` |
| `message` | `text` | `YES` | `` |
| `timestamp` | `timestamptz` | `YES` | `now()` |
| `entity_type` | `text` | `NO` | `'sync'::text` |
| `request_url` | `text` | `YES` | `` |
| `record_count` | `int4` | `YES` | `` |
| `error` | `jsonb` | `YES` | `` |
| `extra` | `jsonb` | `YES` | `` |
| `created_at` | `timestamptz` | `YES` | `now()` |
| `updated_at` | `timestamptz` | `YES` | `now()` |

## Indexes

- `doorloop_pipeline_audit_pkey` — `CREATE UNIQUE INDEX doorloop_pipeline_audit_pkey ON public.doorloop_pipeline_audit USING btree (id)`