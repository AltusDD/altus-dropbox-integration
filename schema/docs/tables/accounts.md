# Table `accounts`

**Primary Key:** `id, id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int4` | `NO` | `nextval('accounts_id_seq'::regclass)` |
| `doorloop_id` | `varchar` | `NO` | `` |
| `name` | `text` | `YES` | `` |
| `type` | `text` | `YES` | `` |
| `active` | `bool` | `YES` | `true` |
| `description` | `text` | `YES` | `` |
| `created_at` | `timestamptz` | `YES` | `` |
| `updated_at` | `timestamptz` | `YES` | `` |

## Indexes

- `accounts_doorloop_id_key` — `CREATE UNIQUE INDEX accounts_doorloop_id_key ON public.accounts USING btree (doorloop_id)`
- `accounts_pkey` — `CREATE UNIQUE INDEX accounts_pkey ON public.accounts USING btree (id)`