# Table `doorloop_raw_users`

**Primary Key:** `id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `companyName` | `text` | `YES` | `` |
| `firstName` | `text` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `active` | `bool` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `emails` | `jsonb` | `YES` | `` |
| `invitationLastSentAt` | `timestamptz` | `YES` | `` |
| `jobTitle` | `text` | `YES` | `` |
| `fullName` | `text` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `primaryAddress` | `jsonb` | `YES` | `` |
| `lastSeenAt` | `timestamptz` | `YES` | `` |
| `bankAccounts` | `jsonb` | `YES` | `` |
| `propertyGroups` | `jsonb` | `YES` | `` |
| `properties` | `jsonb` | `YES` | `` |
| `e164PhoneMobileNumber` | `text` | `YES` | `` |
| `phones` | `jsonb` | `YES` | `` |
| `role` | `text` | `YES` | `` |
| `intercomContactId` | `text` | `YES` | `` |
| `timezone` | `text` | `YES` | `` |
| `loginEmail` | `text` | `YES` | `` |
| `name` | `text` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `lastName` | `text` | `YES` | `` |
| `status` | `text` | `YES` | `` |
| `owner` | `bool` | `YES` | `` |
| `pictureUrl` | `text` | `YES` | `` |
| `batch` | `text` | `YES` | `` |

## Indexes

- `doorloop_raw_users_pkey` — `CREATE UNIQUE INDEX doorloop_raw_users_pkey ON public.doorloop_raw_users USING btree (id)`