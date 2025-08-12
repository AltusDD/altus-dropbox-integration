# Table `lease_payments`

**Primary Key:** `id, id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int4` | `NO` | `nextval('lease_payments_id_seq'::regclass)` |
| `doorloop_id` | `varchar` | `NO` | `` |
| `amount_cents` | `int8` | `YES` | `` |
| `payment_date` | `date` | `YES` | `` |
| `status` | `text` | `YES` | `` |
| `payment_method` | `text` | `YES` | `` |
| `lease_id_dl` | `varchar` | `YES` | `` |
| `tenant_id_dl` | `varchar` | `YES` | `` |
| `account_id_dl` | `varchar` | `YES` | `` |
| `created_at` | `timestamptz` | `YES` | `` |
| `updated_at` | `timestamptz` | `YES` | `` |

## Indexes

- `lease_payments_doorloop_id_key` — `CREATE UNIQUE INDEX lease_payments_doorloop_id_key ON public.lease_payments USING btree (doorloop_id)`
- `lease_payments_pkey` — `CREATE UNIQUE INDEX lease_payments_pkey ON public.lease_payments USING btree (id)`