# Table `property_owners`

**Primary Key:** `property_id, property_id, property_id, owner_id, owner_id, owner_id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `property_id` | `int8` | `NO` | `` |
| `owner_id` | `int8` | `NO` | `` |

## Foreign Keys

- **property_owners_owner_id_fkey**: owner_id → public.owners(id) [on update a, on delete c]
- **property_owners_property_id_fkey**: property_id → public.properties(id) [on update a, on delete c]

## Indexes

- `property_owners_pkey` — `CREATE UNIQUE INDEX property_owners_pkey ON public.property_owners USING btree (property_id, owner_id)`