# Table `units`

**Primary Key:** `id, id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int8` | `NO` | `` |
| `doorloop_id` | `text` | `YES` | `` |
| `unit_number` | `text` | `YES` | `` |
| `beds` | `numeric` | `YES` | `` |
| `baths` | `numeric` | `YES` | `` |
| `sq_ft` | `numeric` | `YES` | `` |
| `rent_amount` | `numeric` | `YES` | `` |
| `doorloop_property_id` | `text` | `YES` | `` |
| `created_at` | `timestamptz` | `YES` | `now()` |
| `updated_at` | `timestamptz` | `YES` | `now()` |
| `status` | `text` | `YES` | `` |

## Indexes

- `idx_units_doorloop_property` — `CREATE INDEX idx_units_doorloop_property ON public.units USING btree (doorloop_property_id)`
- `uniq_units_doorloop_id` — `CREATE UNIQUE INDEX uniq_units_doorloop_id ON public.units USING btree (doorloop_id) WHERE (doorloop_id IS NOT NULL)`
- `units_doorloop_id_key` — `CREATE UNIQUE INDEX units_doorloop_id_key ON public.units USING btree (doorloop_id)`
- `units_pkey` — `CREATE UNIQUE INDEX units_pkey ON public.units USING btree (id)`