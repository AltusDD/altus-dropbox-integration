# Table `notes`

**Primary Key:** `id, id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int4` | `NO` | `nextval('notes_id_seq'::regclass)` |
| `doorloop_id` | `varchar` | `NO` | `` |
| `title` | `text` | `YES` | `` |
| `body` | `text` | `YES` | `` |
| `resource_id_dl` | `varchar` | `YES` | `` |
| `resource_type` | `text` | `YES` | `` |
| `created_by_dl` | `varchar` | `YES` | `` |
| `created_at` | `timestamptz` | `YES` | `` |
| `updated_at` | `timestamptz` | `YES` | `` |

## Indexes

- `notes_doorloop_id_key` — `CREATE UNIQUE INDEX notes_doorloop_id_key ON public.notes USING btree (doorloop_id)`
- `notes_pkey` — `CREATE UNIQUE INDEX notes_pkey ON public.notes USING btree (id)`