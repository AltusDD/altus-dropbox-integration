# Table `doorloop_normalized_tenants`

**Primary Key:** `doorloop_id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `doorloop_id` | `text` | `NO` | `` |
| `name` | `text` | `YES` | `` |

## Indexes

- `doorloop_normalized_tenants_pkey` — `CREATE UNIQUE INDEX doorloop_normalized_tenants_pkey ON public.doorloop_normalized_tenants USING btree (doorloop_id)`