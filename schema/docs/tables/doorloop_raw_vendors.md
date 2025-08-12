# Table `doorloop_raw_vendors`

**Primary Key:** `id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `outgoingEPay` | `jsonb` | `YES` | `` |
| `companyName` | `text` | `YES` | `` |
| `firstName` | `text` | `YES` | `` |
| `active` | `bool` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `services` | `jsonb` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `emails` | `jsonb` | `YES` | `` |
| `batch` | `text` | `YES` | `` |
| `fullName` | `text` | `YES` | `` |
| `jobTitle` | `text` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `balance` | `numeric` | `YES` | `` |
| `primaryAddress` | `jsonb` | `YES` | `` |
| `properties` | `jsonb` | `YES` | `` |
| `e164PhoneMobileNumber` | `text` | `YES` | `` |
| `phones` | `jsonb` | `YES` | `` |
| `company` | `bool` | `YES` | `` |
| `alternateAddress` | `jsonb` | `YES` | `` |
| `name` | `text` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `accounts` | `jsonb` | `YES` | `` |
| `conversationWelcomeSmsSentAt` | `timestamptz` | `YES` | `` |
| `lastName` | `text` | `YES` | `` |

## Indexes

- `doorloop_raw_vendors_pkey` — `CREATE UNIQUE INDEX doorloop_raw_vendors_pkey ON public.doorloop_raw_vendors USING btree (id)`