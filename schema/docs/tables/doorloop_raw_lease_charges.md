# Table `doorloop_raw_lease_charges`

**Primary Key:** `id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `memo` | `text` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `register` | `jsonb` | `YES` | `` |
| `reference` | `text` | `YES` | `` |
| `lateFeeForLeaseCharge` | `text` | `YES` | `` |
| `batch` | `text` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `totalAmount` | `numeric` | `YES` | `` |
| `isFilesSharedWithTenant` | `bool` | `YES` | `` |
| `date` | `timestamptz` | `YES` | `` |
| `totalBalance` | `numeric` | `YES` | `` |
| `lastLateFeesProcessedDate` | `timestamptz` | `YES` | `` |
| `recurringTransaction` | `text` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `lines` | `jsonb` | `YES` | `` |
| `lease` | `text` | `YES` | `` |

## Indexes

- `doorloop_raw_lease_charges_pkey` — `CREATE UNIQUE INDEX doorloop_raw_lease_charges_pkey ON public.doorloop_raw_lease_charges USING btree (id)`