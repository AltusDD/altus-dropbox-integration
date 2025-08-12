# Table `vendors`

**Primary Key:** `id, id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int4` | `NO` | `nextval('vendors_id_seq'::regclass)` |
| `doorloop_id` | `varchar` | `NO` | `` |
| `first_name` | `text` | `YES` | `` |
| `last_name` | `text` | `YES` | `` |
| `full_name` | `text` | `YES` | `` |
| `display_name` | `text` | `YES` | `` |
| `company_name` | `text` | `YES` | `` |
| `notes` | `text` | `YES` | `` |
| `active` | `bool` | `YES` | `true` |
| `balance_cents` | `int8` | `YES` | `` |
| `created_at` | `timestamptz` | `YES` | `` |
| `updated_at` | `timestamptz` | `YES` | `` |

## Indexes

- `vendors_doorloop_id_key` — `CREATE UNIQUE INDEX vendors_doorloop_id_key ON public.vendors USING btree (doorloop_id)`
- `vendors_pkey` — `CREATE UNIQUE INDEX vendors_pkey ON public.vendors USING btree (id)`