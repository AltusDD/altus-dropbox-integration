# Table `collection_actions`

**Primary Key:** `id, id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int8` | `NO` | `` |
| `lease_id` | `int8` | `NO` | `` |
| `tenant_id` | `int8` | `YES` | `` |
| `status` | `text` | `YES` | `` |
| `stage` | `text` | `NO` | `` |
| `due_date` | `date` | `YES` | `` |
| `amount_due` | `numeric` | `YES` | `` |
| `notice_sent_at` | `timestamptz` | `YES` | `` |
| `notes` | `text` | `YES` | `` |
| `created_at` | `timestamptz` | `NO` | `timezone('utc'::text, now())` |
| `updated_at` | `timestamptz` | `NO` | `timezone('utc'::text, now())` |

## Foreign Keys

- **collection_actions_tenant_id_fkey**: tenant_id → public.tenants(id) [on update a, on delete a]

## Indexes

- `collection_actions_pkey` — `CREATE UNIQUE INDEX collection_actions_pkey ON public.collection_actions USING btree (id)`