# Table `doorloop_raw_applications`

**Primary Key:** `id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `batch` | `text` | `YES` | `` |
| `data` | `jsonb` | `YES` | `` |
| `createdat` | `timestamptz` | `YES` | `` |
| `updatedat` | `timestamptz` | `YES` | `` |
| `_raw_payload` | `jsonb` | `YES` | `` |

## Indexes

- `doorloop_raw_applications_pkey` — `CREATE UNIQUE INDEX doorloop_raw_applications_pkey ON public.doorloop_raw_applications USING btree (id)`