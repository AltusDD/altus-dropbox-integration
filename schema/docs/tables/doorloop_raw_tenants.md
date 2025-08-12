# Table `doorloop_raw_tenants`

**Primary Key:** `id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `dateOfBirth` | `timestamptz` | `YES` | `` |
| `companyName` | `text` | `YES` | `` |
| `firstName` | `text` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `emails` | `jsonb` | `YES` | `` |
| `batch` | `text` | `YES` | `` |
| `fullName` | `text` | `YES` | `` |
| `type` | `text` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `notes` | `text` | `YES` | `` |
| `dependants` | `jsonb` | `YES` | `` |
| `primaryAddress` | `jsonb` | `YES` | `` |
| `e164PhoneMobileNumber` | `text` | `YES` | `` |
| `emergencyContacts` | `jsonb` | `YES` | `` |
| `phones` | `jsonb` | `YES` | `` |
| `company` | `bool` | `YES` | `` |
| `vehicles` | `jsonb` | `YES` | `` |
| `gender` | `text` | `YES` | `` |
| `acceptedOnTOS` | `timestamptz` | `YES` | `` |
| `intercomContactId` | `text` | `YES` | `` |
| `name` | `text` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `portalInfo` | `jsonb` | `YES` | `` |
| `middleName` | `text` | `YES` | `` |
| `otherScreeningService` | `text` | `YES` | `` |
| `stripeCustomerId` | `text` | `YES` | `` |
| `conversationWelcomeSmsSentAt` | `timestamptz` | `YES` | `` |
| `screeningService` | `text` | `YES` | `` |
| `lastName` | `text` | `YES` | `` |
| `prospectInfo` | `jsonb` | `YES` | `` |
| `pets` | `jsonb` | `YES` | `` |

## Indexes

- `doorloop_raw_tenants_pkey` — `CREATE UNIQUE INDEX doorloop_raw_tenants_pkey ON public.doorloop_raw_tenants USING btree (id)`