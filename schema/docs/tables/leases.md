# Table `leases`

**Primary Key:** `id, id, id, id, id, id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int8` | `NO` | `` |
| `property_id` | `int8` | `NO` | `` |
| `unit_id` | `int8` | `YES` | `` |
| `primary_tenant_id` | `int8` | `YES` | `` |
| `start_date` | `date` | `NO` | `` |
| `end_date` | `date` | `NO` | `` |
| `rent_cents` | `int4` | `NO` | `` |
| `deposit_cents` | `int4` | `YES` | `0` |
| `status` | `text` | `NO` | `` |
| `doorloop_id` | `text` | `YES` | `` |
| `created_at` | `timestamptz` | `NO` | `now()` |
| `updated_at` | `timestamptz` | `NO` | `now()` |

## Foreign Keys

- **fk_leases_primary_tenant_id**: primary_tenant_id → public.tenants(id) [on update a, on delete n]
- **fk_leases_property_id**: property_id → public.properties(id) [on update a, on delete r]
- **fk_leases_unit_id**: unit_id → public.units(id) [on update a, on delete n]

## Indexes

- `idx_leases_active_lookup` — `CREATE INDEX idx_leases_active_lookup ON public.leases USING btree (status, unit_id, start_date, end_date) WHERE (status = ANY (ARRAY['active'::text, 'renewal'::text]))`
- `idx_leases_dates` — `CREATE INDEX idx_leases_dates ON public.leases USING btree (start_date, end_date)`
- `idx_leases_primary_tenant` — `CREATE INDEX idx_leases_primary_tenant ON public.leases USING btree (primary_tenant_id)`
- `idx_leases_property` — `CREATE INDEX idx_leases_property ON public.leases USING btree (property_id)`
- `idx_leases_status` — `CREATE INDEX idx_leases_status ON public.leases USING btree (status)`
- `idx_leases_status_unit` — `CREATE INDEX idx_leases_status_unit ON public.leases USING btree (status, unit_id)`
- `idx_leases_unit` — `CREATE INDEX idx_leases_unit ON public.leases USING btree (unit_id)`
- `leases_doorloop_id_key` — `CREATE UNIQUE INDEX leases_doorloop_id_key ON public.leases USING btree (doorloop_id)`
- `leases_pkey` — `CREATE UNIQUE INDEX leases_pkey ON public.leases USING btree (id)`