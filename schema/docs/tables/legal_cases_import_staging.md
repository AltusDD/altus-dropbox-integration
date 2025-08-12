# Table `legal_cases_import_staging`

**Primary Key:** `id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int8` | `NO` | `nextval('legal_cases_import_staging_id_seq'::regclass)` |
| `tenant_name` | `varchar` | `NO` | `` |
| `property_address` | `varchar` | `YES` | `` |
| `case_type` | `varchar` | `YES` | `` |
| `lease_start` | `date` | `YES` | `` |
| `lease_end` | `date` | `YES` | `` |
| `amount_claimed` | `numeric` | `YES` | `` |
| `notes` | `text` | `YES` | `` |
| `status` | `varchar` | `YES` | `'pending'::character varying` |
| `source_file_name` | `varchar` | `YES` | `` |
| `import_errors` | `jsonb` | `YES` | `` |
| `resolved_property_id` | `int4` | `YES` | `` |
| `resolved_tenant_id` | `int4` | `YES` | `` |
| `resolved_lease_id` | `int4` | `YES` | `` |
| `created_at` | `timestamp` | `YES` | `CURRENT_TIMESTAMP` |
| `updated_at` | `timestamp` | `YES` | `CURRENT_TIMESTAMP` |

## Indexes

- `legal_cases_import_staging_pkey` — `CREATE UNIQUE INDEX legal_cases_import_staging_pkey ON public.legal_cases_import_staging USING btree (id)`