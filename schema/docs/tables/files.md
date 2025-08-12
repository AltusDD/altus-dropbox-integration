# Table `files`

**Primary Key:** `id, id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int4` | `NO` | `nextval('files_id_seq'::regclass)` |
| `doorloop_id` | `varchar` | `NO` | `` |
| `name` | `text` | `YES` | `` |
| `notes` | `text` | `YES` | `` |
| `resource_id_dl` | `varchar` | `YES` | `` |
| `resource_type` | `text` | `YES` | `` |
| `size_bytes` | `int8` | `YES` | `` |
| `mime_type` | `text` | `YES` | `` |
| `download_url` | `text` | `YES` | `` |
| `created_by_dl` | `varchar` | `YES` | `` |
| `created_at` | `timestamptz` | `YES` | `` |
| `updated_at` | `timestamptz` | `YES` | `` |

## Indexes

- `files_doorloop_id_key` — `CREATE UNIQUE INDEX files_doorloop_id_key ON public.files USING btree (doorloop_id)`
- `files_pkey` — `CREATE UNIQUE INDEX files_pkey ON public.files USING btree (id)`