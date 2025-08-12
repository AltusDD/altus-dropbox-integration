# Table `tenants`

**Primary Key:** `id, id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int4` | `NO` | `nextval('tenants_id_seq'::regclass)` |
| `doorloop_id` | `varchar` | `NO` | `` |
| `first_name` | `text` | `YES` | `` |
| `last_name` | `text` | `YES` | `` |
| `full_name` | `text` | `YES` | `` |
| `display_name` | `text` | `YES` | `` |
| `date_of_birth` | `date` | `YES` | `` |
| `company_name` | `text` | `YES` | `` |
| `notes` | `text` | `YES` | `` |
| `type` | `text` | `YES` | `` |
| `credit_score` | `int4` | `YES` | `` |
| `created_at` | `timestamptz` | `YES` | `` |
| `updated_at` | `timestamptz` | `YES` | `` |

## Indexes

- `tenants_doorloop_id_key` — `CREATE UNIQUE INDEX tenants_doorloop_id_key ON public.tenants USING btree (doorloop_id)`
- `tenants_pkey` — `CREATE UNIQUE INDEX tenants_pkey ON public.tenants USING btree (id)`