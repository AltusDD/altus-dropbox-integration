# Table `doorloop_raw_expenses`

**Primary Key:** `id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `isVoidedCheck` | `bool` | `YES` | `` |
| `paymentMethod` | `text` | `YES` | `` |
| `memo` | `text` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `ePayInfo` | `jsonb` | `YES` | `` |
| `register` | `jsonb` | `YES` | `` |
| `reference` | `text` | `YES` | `` |
| `batch` | `text` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `payToResourceId` | `text` | `YES` | `` |
| `totalAmount` | `numeric` | `YES` | `` |
| `checkInfo` | `jsonb` | `YES` | `` |
| `payToResourceType` | `text` | `YES` | `` |
| `date` | `timestamptz` | `YES` | `` |
| `payFromAccount` | `text` | `YES` | `` |
| `totalBalance` | `int8` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `lines` | `jsonb` | `YES` | `` |

## Indexes

- `doorloop_raw_expenses_pkey` — `CREATE UNIQUE INDEX doorloop_raw_expenses_pkey ON public.doorloop_raw_expenses USING btree (id)`