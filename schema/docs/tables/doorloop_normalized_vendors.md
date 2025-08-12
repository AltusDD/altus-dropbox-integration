# Table `doorloop_normalized_vendors`

**Primary Key:** `doorloop_id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `doorloop_id` | `text` | `NO` | `` |
| `name` | `text` | `YES` | `` |
| `balance` | `numeric` | `YES` | `` |

## Indexes

- `doorloop_normalized_vendors_pkey` — `CREATE UNIQUE INDEX doorloop_normalized_vendors_pkey ON public.doorloop_normalized_vendors USING btree (doorloop_id)`