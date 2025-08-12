# Table `lease_tenants`

**Primary Key:** `lease_id, lease_id, lease_id, tenant_id, tenant_id, tenant_id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `lease_id` | `int8` | `NO` | `` |
| `tenant_id` | `int8` | `NO` | `` |

## Foreign Keys

- **lease_tenants_lease_id_fkey**: lease_id → public.leases(id) [on update a, on delete c]
- **lease_tenants_tenant_id_fkey**: tenant_id → public.tenants(id) [on update a, on delete c]

## Indexes

- `lease_tenants_pkey` — `CREATE UNIQUE INDEX lease_tenants_pkey ON public.lease_tenants USING btree (lease_id, tenant_id)`