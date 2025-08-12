# Table `doorloop_raw_work_orders`

**Primary Key:** `id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |

## Indexes

- `doorloop_raw_work_orders_pkey` — `CREATE UNIQUE INDEX doorloop_raw_work_orders_pkey ON public.doorloop_raw_work_orders USING btree (id)`