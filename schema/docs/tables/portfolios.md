# Table `portfolios`

**Primary Key:** `id, id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int4` | `NO` | `nextval('portfolios_id_seq'::regclass)` |
| `doorloop_id` | `varchar` | `NO` | `` |
| `name` | `text` | `YES` | `` |
| `created_at` | `timestamptz` | `YES` | `` |
| `updated_at` | `timestamptz` | `YES` | `` |

## Indexes

- `portfolios_doorloop_id_key` — `CREATE UNIQUE INDEX portfolios_doorloop_id_key ON public.portfolios USING btree (doorloop_id)`
- `portfolios_pkey` — `CREATE UNIQUE INDEX portfolios_pkey ON public.portfolios USING btree (id)`