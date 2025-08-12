# Table `damages_claims`

**Primary Key:** `id, id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int8` | `NO` | `` |
| `case_number` | `text` | `YES` | `` |
| `lease_id` | `int8` | `YES` | `` |
| `property_id` | `int8` | `YES` | `` |
| `status` | `text` | `YES` | `` |
| `claim_amount` | `numeric` | `YES` | `` |
| `incident_date` | `date` | `YES` | `` |
| `filing_date` | `date` | `YES` | `` |
| `settlement_amount` | `numeric` | `YES` | `` |
| `notes` | `text` | `YES` | `` |
| `created_at` | `timestamptz` | `NO` | `timezone('utc'::text, now())` |
| `updated_at` | `timestamptz` | `NO` | `timezone('utc'::text, now())` |

## Indexes

- `damages_claims_case_number_key` — `CREATE UNIQUE INDEX damages_claims_case_number_key ON public.damages_claims USING btree (case_number)`
- `damages_claims_pkey` — `CREATE UNIQUE INDEX damages_claims_pkey ON public.damages_claims USING btree (id)`