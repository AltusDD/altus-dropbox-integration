# Table `doorloop_raw_recurring_credits`

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

- `doorloop_raw_recurring_credits_pkey` — `CREATE UNIQUE INDEX doorloop_raw_recurring_credits_pkey ON public.doorloop_raw_recurring_credits USING btree (id)`