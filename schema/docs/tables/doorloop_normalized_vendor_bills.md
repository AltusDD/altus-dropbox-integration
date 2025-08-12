# Table `doorloop_normalized_vendor_bills`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `YES` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `` |
| `totalAmount` | `int8` | `YES` | `` |
| `lines` | `jsonb` | `YES` | `` |
| `vendor` | `text` | `YES` | `` |
| `workOrder` | `text` | `YES` | `` |
| `totalBalance` | `numeric` | `YES` | `` |
| `batch` | `text` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `dueDate` | `timestamptz` | `YES` | `` |
| `memo` | `text` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `date` | `timestamptz` | `YES` | `` |
| `recurringTransaction` | `text` | `YES` | `` |
| `register` | `jsonb` | `YES` | `` |
| `reference` | `text` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `amount` | `numeric` | `YES` | `` |