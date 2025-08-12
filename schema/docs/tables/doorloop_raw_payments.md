# Table `doorloop_raw_payments`

**Primary Key:** `id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int8` | `NO` | `` |
| `created_at` | `timestamptz` | `YES` | `now()` |
| `data` | `jsonb` | `YES` | `` |

## Indexes

- `doorloop_raw_payments_pkey` — `CREATE UNIQUE INDEX doorloop_raw_payments_pkey ON public.doorloop_raw_payments USING btree (id)`