# Table `doorloop_raw_lease_reversed_payments`

**Primary Key:** `id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `depositStatus` | `text` | `YES` | `` |
| `processorFee` | `int8` | `YES` | `` |
| `memo` | `text` | `YES` | `` |
| `lease` | `text` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `date` | `timestamptz` | `YES` | `` |
| `leasePayment` | `text` | `YES` | `` |
| `register` | `jsonb` | `YES` | `` |
| `reference` | `text` | `YES` | `` |
| `reason` | `text` | `YES` | `` |
| `batch` | `text` | `YES` | `` |

## Indexes

- `doorloop_raw_lease_reversed_payments_pkey` — `CREATE UNIQUE INDEX doorloop_raw_lease_reversed_payments_pkey ON public.doorloop_raw_lease_reversed_payments USING btree (id)`