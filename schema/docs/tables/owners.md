# Table `owners`

**Primary Key:** `id, id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int4` | `NO` | `nextval('owners_id_seq'::regclass)` |
| `doorloop_id` | `varchar` | `NO` | `` |
| `first_name` | `text` | `YES` | `` |
| `last_name` | `text` | `YES` | `` |
| `full_name` | `text` | `YES` | `` |
| `display_name` | `text` | `YES` | `` |
| `company_name` | `text` | `YES` | `` |
| `notes` | `text` | `YES` | `` |
| `active` | `bool` | `YES` | `true` |
| `management_start_date` | `date` | `YES` | `` |
| `management_end_date` | `date` | `YES` | `` |
| `created_at` | `timestamptz` | `YES` | `` |
| `updated_at` | `timestamptz` | `YES` | `` |

## Indexes

- `owners_doorloop_id_key` — `CREATE UNIQUE INDEX owners_doorloop_id_key ON public.owners USING btree (doorloop_id)`
- `owners_pkey` — `CREATE UNIQUE INDEX owners_pkey ON public.owners USING btree (id)`