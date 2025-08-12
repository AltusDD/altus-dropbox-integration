# Table `doorloop_raw_property_groups`

**Primary Key:** `id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |

## Indexes

- `doorloop_raw_property_groups_pkey` — `CREATE UNIQUE INDEX doorloop_raw_property_groups_pkey ON public.doorloop_raw_property_groups USING btree (id)`