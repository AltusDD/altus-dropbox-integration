# Table `properties`

**Primary Key:** `id, id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int8` | `NO` | `` |
| `doorloop_id` | `text` | `YES` | `` |
| `name` | `text` | `YES` | `` |
| `type` | `text` | `YES` | `` |
| `class` | `text` | `YES` | `` |
| `active` | `bool` | `YES` | `` |
| `address_street1` | `text` | `YES` | `` |
| `address_city` | `text` | `YES` | `` |
| `address_state` | `text` | `YES` | `` |
| `address_zip` | `text` | `YES` | `` |
| `created_at` | `timestamptz` | `YES` | `now()` |
| `updated_at` | `timestamptz` | `YES` | `now()` |
| `total_sqft` | `numeric` | `YES` | `` |
| `unit_count` | `int4` | `YES` | `` |
| `occupied_unit_count` | `int4` | `YES` | `` |
| `vacant_unit_count` | `int4` | `YES` | `` |
| `occupancy_rate` | `numeric` | `YES` | `` |

## Indexes

- `properties_doorloop_id_key` — `CREATE UNIQUE INDEX properties_doorloop_id_key ON public.properties USING btree (doorloop_id)`
- `properties_pkey` — `CREATE UNIQUE INDEX properties_pkey ON public.properties USING btree (id)`