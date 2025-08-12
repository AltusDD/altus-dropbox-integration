# Table `doorloop_raw_leases`

**Primary Key:** `id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `currentBalance` | `int8` | `YES` | `` |
| `proofOfInsuranceProvided` | `bool` | `YES` | `` |
| `evictionPending` | `bool` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `totalRecurringRent` | `numeric` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `totalRecurringCharges` | `int8` | `YES` | `` |
| `recurringRentStatus` | `text` | `YES` | `` |
| `totalRecurringCredits` | `int8` | `YES` | `` |
| `proofOfInsuranceProvidedAt` | `timestamptz` | `YES` | `` |
| `reference` | `text` | `YES` | `` |
| `batch` | `text` | `YES` | `` |
| `notes` | `text` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `start` | `timestamptz` | `YES` | `` |
| `end` | `timestamptz` | `YES` | `` |
| `totalDepositsHeld` | `numeric` | `YES` | `` |
| `proofOfInsuranceExpirationDate` | `timestamptz` | `YES` | `` |
| `lastLateFeesProcessedDate` | `timestamptz` | `YES` | `` |
| `renewalInfo` | `jsonb` | `YES` | `` |
| `settings` | `jsonb` | `YES` | `` |
| `outstandingBalance` | `numeric` | `YES` | `` |
| `name` | `text` | `YES` | `` |
| `totalBalanceDue` | `numeric` | `YES` | `` |
| `property` | `text` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `term` | `text` | `YES` | `` |
| `totalRecurringPayments` | `numeric` | `YES` | `` |
| `rolloverToAtWill` | `bool` | `YES` | `` |
| `proofOfInsuranceRequired` | `bool` | `YES` | `` |
| `recurringRentFrequency` | `text` | `YES` | `` |
| `overdueBalance` | `numeric` | `YES` | `` |
| `proofOfInsuranceStatus` | `text` | `YES` | `` |
| `upcomingBalance` | `int8` | `YES` | `` |
| `status` | `text` | `YES` | `` |
| `proofOfInsuranceEffectiveDate` | `timestamptz` | `YES` | `` |
| `units` | `jsonb` | `YES` | `` |

## Indexes

- `doorloop_raw_leases_pkey` — `CREATE UNIQUE INDEX doorloop_raw_leases_pkey ON public.doorloop_raw_leases USING btree (id)`