# Table `file_assets`

**Primary Key:** `id, id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int8` | `NO` | `` |
| `supabase_entity_id` | `int8` | `NO` | `` |
| `entity_type` | `text` | `NO` | `` |
| `dropbox_path` | `text` | `NO` | `` |
| `file_name` | `text` | `NO` | `` |
| `mime_type` | `text` | `YES` | `` |
| `size` | `int8` | `YES` | `` |
| `created_by_user_id` | `int8` | `YES` | `` |
| `shared_link_url` | `text` | `YES` | `` |
| `shared_link_expires_at` | `timestamptz` | `YES` | `` |
| `created_at` | `timestamptz` | `NO` | `now()` |

## Indexes

- `file_assets_pkey` — `CREATE UNIQUE INDEX file_assets_pkey ON public.file_assets USING btree (id)`
- `idx_file_assets_created_at` — `CREATE INDEX idx_file_assets_created_at ON public.file_assets USING btree (created_at)`
- `idx_file_assets_entity` — `CREATE INDEX idx_file_assets_entity ON public.file_assets USING btree (entity_type, supabase_entity_id)`