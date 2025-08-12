# Table `doorloop_raw_lease_credits`

**Primary Key:** `id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `totalAmount` | `int8` | `YES` | `` |
| `lines` | `jsonb` | `YES` | `` |
| `batch` | `text` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `totalBalance` | `int8` | `YES` | `` |
| `lease` | `text` | `YES` | `` |
| `isFilesSharedWithTenant` | `bool` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `date` | `timestamptz` | `YES` | `` |
| `register` | `jsonb` | `YES` | `` |
| `reference` | `text` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `amount` | `numeric` | `YES` | `` |

## Indexes

- `doorloop_raw_lease_credits_pkey` — `CREATE UNIQUE INDEX doorloop_raw_lease_credits_pkey ON public.doorloop_raw_lease_credits USING btree (id)`