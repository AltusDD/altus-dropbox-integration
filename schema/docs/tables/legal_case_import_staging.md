# Table `legal_case_import_staging`

**Primary Key:** `id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `uuid` | `NO` | `gen_random_uuid()` |
| `uploaded_at` | `timestamptz` | `YES` | `now()` |
| `uploaded_by` | `text` | `YES` | `` |
| `original_filename` | `text` | `YES` | `` |
| `row_number` | `int4` | `NO` | `` |
| `raw_data` | `jsonb` | `NO` | `` |
| `status` | `text` | `YES` | `'pending'::text` |
| `validation_errors` | `jsonb` | `YES` | `` |
| `processed_at` | `timestamptz` | `YES` | `` |

## Indexes

- `legal_case_import_staging_pkey` — `CREATE UNIQUE INDEX legal_case_import_staging_pkey ON public.legal_case_import_staging USING btree (id)`