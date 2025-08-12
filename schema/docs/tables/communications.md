# Table `communications`

**Primary Key:** `id, id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int4` | `NO` | `nextval('communications_id_seq'::regclass)` |
| `doorloop_id` | `varchar` | `NO` | `` |
| `subject` | `text` | `YES` | `` |
| `body_preview` | `text` | `YES` | `` |
| `sent_at` | `timestamptz` | `YES` | `` |
| `type` | `text` | `YES` | `` |
| `status` | `text` | `YES` | `` |
| `thread_id` | `text` | `YES` | `` |
| `created_at` | `timestamptz` | `YES` | `` |
| `updated_at` | `timestamptz` | `YES` | `` |

## Indexes

- `communications_doorloop_id_key` — `CREATE UNIQUE INDEX communications_doorloop_id_key ON public.communications USING btree (doorloop_id)`
- `communications_pkey` — `CREATE UNIQUE INDEX communications_pkey ON public.communications USING btree (id)`