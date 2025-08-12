# Table `doorloop_raw_communications`

**Primary Key:** `id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `externalId` | `text` | `YES` | `` |
| `conversationMessage` | `text` | `YES` | `` |
| `subjectType` | `text` | `YES` | `` |
| `intercomReceiptId` | `text` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `cc` | `jsonb` | `YES` | `` |
| `bodyPreview` | `text` | `YES` | `` |
| `to` | `jsonb` | `YES` | `` |
| `announcement` | `text` | `YES` | `` |
| `type` | `text` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `openedAt` | `jsonb` | `YES` | `` |
| `sentAt` | `timestamptz` | `YES` | `` |
| `bouncedAt` | `timestamptz` | `YES` | `` |
| `conversation` | `text` | `YES` | `` |
| `failedReason` | `text` | `YES` | `` |
| `bcc` | `jsonb` | `YES` | `` |
| `subject` | `text` | `YES` | `` |
| `intercomContactId` | `text` | `YES` | `` |
| `from` | `jsonb` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `clickedAt` | `jsonb` | `YES` | `` |
| `intercomTemplateId` | `int8` | `YES` | `` |
| `status` | `text` | `YES` | `` |
| `batch` | `text` | `YES` | `` |

## Indexes

- `doorloop_raw_communications_pkey` — `CREATE UNIQUE INDEX doorloop_raw_communications_pkey ON public.doorloop_raw_communications USING btree (id)`