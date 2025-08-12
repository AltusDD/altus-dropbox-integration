# Table `doorloop_raw_vendor_bills`

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
| `vendor` | `text` | `YES` | `` |
| `workOrder` | `text` | `YES` | `` |
| `totalBalance` | `numeric` | `YES` | `` |
| `batch` | `text` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `dueDate` | `timestamptz` | `YES` | `` |
| `memo` | `text` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `date` | `timestamptz` | `YES` | `` |
| `recurringTransaction` | `text` | `YES` | `` |
| `register` | `jsonb` | `YES` | `` |
| `reference` | `text` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `amount` | `numeric` | `YES` | `` |

## Indexes

- `doorloop_raw_vendor_bills_pkey` — `CREATE UNIQUE INDEX doorloop_raw_vendor_bills_pkey ON public.doorloop_raw_vendor_bills USING btree (id)`