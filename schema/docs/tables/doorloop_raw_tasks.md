# Table `doorloop_raw_tasks`

**Primary Key:** `id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `createdBy` | `text` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `entryNotes` | `text` | `YES` | `` |
| `reference` | `text` | `YES` | `` |
| `assignedToUsers` | `jsonb` | `YES` | `` |
| `type` | `text` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `completedAt` | `timestamptz` | `YES` | `` |
| `entryPermission` | `text` | `YES` | `` |
| `createdByType` | `text` | `YES` | `` |
| `workOrder` | `jsonb` | `YES` | `` |
| `unit` | `text` | `YES` | `` |
| `dueDate` | `timestamptz` | `YES` | `` |
| `subject` | `text` | `YES` | `` |
| `recurringTransaction` | `text` | `YES` | `` |
| `property` | `text` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `dateType` | `text` | `YES` | `` |
| `requestedByTenant` | `text` | `YES` | `` |
| `requestedByUser` | `text` | `YES` | `` |
| `tenantRequestMaintenanceCategory` | `text` | `YES` | `` |
| `tenantRequestType` | `text` | `YES` | `` |
| `status` | `text` | `YES` | `` |
| `description` | `text` | `YES` | `` |
| `priority` | `text` | `YES` | `` |
| `linkedResource` | `jsonb` | `YES` | `` |
| `requestedByOwner` | `text` | `YES` | `` |
| `batch` | `text` | `YES` | `` |

## Indexes

- `doorloop_raw_tasks_pkey` — `CREATE UNIQUE INDEX doorloop_raw_tasks_pkey ON public.doorloop_raw_tasks USING btree (id)`