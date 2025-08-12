# Table `lease_credits`

**Primary Key:** `id, id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int4` | `NO` | `nextval('lease_credits_id_seq'::regclass)` |
| `doorloop_id` | `varchar` | `NO` | `` |
| `amount_cents` | `int8` | `YES` | `` |
| `memo` | `text` | `YES` | `` |
| `date` | `date` | `YES` | `` |
| `lease_id_dl` | `varchar` | `YES` | `` |
| `account_id_dl` | `varchar` | `YES` | `` |
| `created_at` | `timestamptz` | `YES` | `` |
| `updated_at` | `timestamptz` | `YES` | `` |

## Indexes

- `lease_credits_doorloop_id_key` — `CREATE UNIQUE INDEX lease_credits_doorloop_id_key ON public.lease_credits USING btree (doorloop_id)`
- `lease_credits_pkey` — `CREATE UNIQUE INDEX lease_credits_pkey ON public.lease_credits USING btree (id)`