# Table `tasks`

**Primary Key:** `id, id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int4` | `NO` | `nextval('tasks_id_seq'::regclass)` |
| `doorloop_id` | `varchar` | `NO` | `` |
| `type` | `text` | `YES` | `` |
| `subject` | `text` | `YES` | `` |
| `description` | `text` | `YES` | `` |
| `status` | `text` | `YES` | `` |
| `priority` | `text` | `YES` | `` |
| `due_date` | `date` | `YES` | `` |
| `property_id_dl` | `varchar` | `YES` | `` |
| `unit_id_dl` | `varchar` | `YES` | `` |
| `tenant_id_dl` | `varchar` | `YES` | `` |
| `owner_id_dl` | `varchar` | `YES` | `` |
| `user_id_dl` | `varchar` | `YES` | `` |
| `vendor_id_dl` | `varchar` | `YES` | `` |
| `created_at` | `timestamptz` | `YES` | `` |
| `updated_at` | `timestamptz` | `YES` | `` |

## Indexes

- `tasks_doorloop_id_key` — `CREATE UNIQUE INDEX tasks_doorloop_id_key ON public.tasks USING btree (doorloop_id)`
- `tasks_pkey` — `CREATE UNIQUE INDEX tasks_pkey ON public.tasks USING btree (id)`