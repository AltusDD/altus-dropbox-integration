# Table `doorloop_raw_notes`

**Primary Key:** `id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `title` | `text` | `YES` | `` |
| `body` | `text` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `tags` | `jsonb` | `YES` | `` |
| `unit` | `text` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `linkedResource` | `jsonb` | `YES` | `` |
| `property` | `text` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `batch` | `text` | `YES` | `` |

## Indexes

- `doorloop_raw_notes_pkey` — `CREATE UNIQUE INDEX doorloop_raw_notes_pkey ON public.doorloop_raw_notes USING btree (id)`