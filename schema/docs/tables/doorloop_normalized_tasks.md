# Table `doorloop_normalized_tasks`

**Primary Key:** `doorloop_id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `doorloop_id` | `text` | `NO` | `` |
| `property_id` | `text` | `YES` | `` |
| `vendor_id` | `text` | `YES` | `` |

## Indexes

- `doorloop_normalized_tasks_pkey` — `CREATE UNIQUE INDEX doorloop_normalized_tasks_pkey ON public.doorloop_normalized_tasks USING btree (doorloop_id)`