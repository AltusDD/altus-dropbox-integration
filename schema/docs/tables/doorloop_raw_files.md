# Table `doorloop_raw_files`

**Primary Key:** `id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `rank` | `int8` | `YES` | `` |
| `createdByType` | `text` | `YES` | `` |
| `notes` | `text` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `tags` | `jsonb` | `YES` | `` |
| `metadata` | `jsonb` | `YES` | `` |
| `unit` | `text` | `YES` | `` |
| `mimeType` | `text` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `isSharedWithTenant` | `bool` | `YES` | `` |
| `createdByName` | `text` | `YES` | `` |
| `downloadUrl` | `text` | `YES` | `` |
| `size` | `int8` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `name` | `text` | `YES` | `` |
| `linkedResource` | `jsonb` | `YES` | `` |
| `property` | `text` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `batch` | `text` | `YES` | `` |

## Indexes

- `doorloop_raw_files_pkey` — `CREATE UNIQUE INDEX doorloop_raw_files_pkey ON public.doorloop_raw_files USING btree (id)`