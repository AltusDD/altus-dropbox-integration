# Table `users`

**Primary Key:** `id, id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int4` | `NO` | `nextval('users_id_seq'::regclass)` |
| `doorloop_id` | `varchar` | `NO` | `` |
| `first_name` | `text` | `YES` | `` |
| `last_name` | `text` | `YES` | `` |
| `full_name` | `text` | `YES` | `` |
| `email` | `text` | `YES` | `` |
| `role` | `text` | `YES` | `` |
| `active` | `bool` | `YES` | `true` |
| `last_seen_at` | `timestamptz` | `YES` | `` |
| `created_at` | `timestamptz` | `YES` | `` |
| `updated_at` | `timestamptz` | `YES` | `` |

## Indexes

- `users_doorloop_id_key` — `CREATE UNIQUE INDEX users_doorloop_id_key ON public.users USING btree (doorloop_id)`
- `users_pkey` — `CREATE UNIQUE INDEX users_pkey ON public.users USING btree (id)`