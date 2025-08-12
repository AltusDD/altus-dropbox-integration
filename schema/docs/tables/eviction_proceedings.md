# Table `eviction_proceedings`

**Primary Key:** `id, id, id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int8` | `NO` | `` |
| `case_number` | `text` | `YES` | `` |
| `lease_id` | `int8` | `YES` | `` |
| `tenant_id` | `int8` | `YES` | `` |
| `status` | `text` | `YES` | `` |
| `filing_date` | `date` | `YES` | `` |
| `judgement_date` | `date` | `YES` | `` |
| `judgement_amount` | `numeric` | `YES` | `` |
| `attorney_id` | `text` | `YES` | `` |
| `notes` | `text` | `YES` | `` |
| `created_at` | `timestamptz` | `NO` | `timezone('utc'::text, now())` |
| `updated_at` | `timestamptz` | `NO` | `timezone('utc'::text, now())` |

## Foreign Keys

- **eviction_proceedings_tenant_id_fkey**: tenant_id → public.tenants(id) [on update a, on delete a]

## Indexes

- `eviction_proceedings_case_number_key` — `CREATE UNIQUE INDEX eviction_proceedings_case_number_key ON public.eviction_proceedings USING btree (case_number)`
- `eviction_proceedings_pkey` — `CREATE UNIQUE INDEX eviction_proceedings_pkey ON public.eviction_proceedings USING btree (id)`