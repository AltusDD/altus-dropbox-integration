# Table `doorloop_raw_lease_payments`

**Primary Key:** `id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `depositEntry` | `text` | `YES` | `` |
| `amountNotAppliedToCharges` | `numeric` | `YES` | `` |
| `paymentMethod` | `text` | `YES` | `` |
| `autoApplyPaymentOnCharges` | `bool` | `YES` | `` |
| `reversedPaymentMemo` | `text` | `YES` | `` |
| `memo` | `text` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `ePayInfo` | `jsonb` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `receivedFromTenant` | `text` | `YES` | `` |
| `register` | `jsonb` | `YES` | `` |
| `reference` | `text` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `linkedCharges` | `jsonb` | `YES` | `` |
| `linkedCredits` | `jsonb` | `YES` | `` |
| `checkInfo` | `jsonb` | `YES` | `` |
| `isFilesSharedWithTenant` | `bool` | `YES` | `` |
| `date` | `timestamptz` | `YES` | `` |
| `depositToAccount` | `text` | `YES` | `` |
| `reversedPayment` | `text` | `YES` | `` |
| `amountAppliedToCredits` | `numeric` | `YES` | `` |
| `amountReceived` | `numeric` | `YES` | `` |
| `recurringTransaction` | `text` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `amountAppliedToCharges` | `numeric` | `YES` | `` |
| `depositStatus` | `text` | `YES` | `` |
| `lease` | `text` | `YES` | `` |
| `reversedPaymentDate` | `timestamptz` | `YES` | `` |
| `batch` | `text` | `YES` | `` |

## Indexes

- `doorloop_raw_lease_payments_pkey` — `CREATE UNIQUE INDEX doorloop_raw_lease_payments_pkey ON public.doorloop_raw_lease_payments USING btree (id)`