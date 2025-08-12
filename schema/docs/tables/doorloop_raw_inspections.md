# Table `doorloop_raw_inspections`

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

- `doorloop_raw_inspections_pkey` — `CREATE UNIQUE INDEX doorloop_raw_inspections_pkey ON public.doorloop_raw_inspections USING btree (id)`