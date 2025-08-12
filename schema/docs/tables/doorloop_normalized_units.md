# Table `doorloop_normalized_units`

**Primary Key:** `doorloop_id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `doorloop_id` | `text` | `NO` | `` |
| `name` | `text` | `YES` | `` |
| `property_id` | `text` | `YES` | `` |

## Indexes

- `doorloop_normalized_units_pkey` — `CREATE UNIQUE INDEX doorloop_normalized_units_pkey ON public.doorloop_normalized_units USING btree (doorloop_id)`