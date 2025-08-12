# Table `doorloop_raw_portfolios`

**Primary Key:** `id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `properties` | `jsonb` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `name` | `text` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `batch` | `text` | `YES` | `` |

## Indexes

- `doorloop_raw_portfolios_pkey` — `CREATE UNIQUE INDEX doorloop_raw_portfolios_pkey ON public.doorloop_raw_portfolios USING btree (id)`