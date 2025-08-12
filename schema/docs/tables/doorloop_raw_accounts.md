# Table `doorloop_raw_accounts`

**Primary Key:** `id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `leaseChargeItem` | `bool` | `YES` | `` |
| `active` | `bool` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `outgoingEPayEnabled` | `bool` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `type` | `text` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `parentAccount` | `text` | `YES` | `` |
| `systemAccount` | `bool` | `YES` | `` |
| `openingBalanceEntry` | `text` | `YES` | `` |
| `class` | `text` | `YES` | `` |
| `name` | `text` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `leaseDepositItem` | `bool` | `YES` | `` |
| `fullyQualifiedName` | `text` | `YES` | `` |
| `cashFlowActivity` | `text` | `YES` | `` |
| `taxable` | `bool` | `YES` | `` |
| `description` | `text` | `YES` | `` |
| `defaultAccountFor` | `jsonb` | `YES` | `` |
| `batch` | `text` | `YES` | `` |

## Indexes

- `doorloop_raw_accounts_pkey` — `CREATE UNIQUE INDEX doorloop_raw_accounts_pkey ON public.doorloop_raw_accounts USING btree (id)`