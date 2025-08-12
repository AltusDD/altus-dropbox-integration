# Table `doorloop_raw_properties`

**Primary Key:** `id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `active` | `bool` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `boardMembers` | `jsonb` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `amenities` | `jsonb` | `YES` | `` |
| `petsPolicy` | `jsonb` | `YES` | `` |
| `address` | `jsonb` | `YES` | `` |
| `batch` | `text` | `YES` | `` |
| `type` | `text` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `owners` | `jsonb` | `YES` | `` |
| `settings` | `jsonb` | `YES` | `` |
| `numActiveUnits` | `int8` | `YES` | `` |
| `class` | `text` | `YES` | `` |
| `name` | `text` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `pictures` | `jsonb` | `YES` | `` |
| `description` | `text` | `YES` | `` |
| `typeDescription` | `text` | `YES` | `` |

## Indexes

- `doorloop_raw_properties_pkey` — `CREATE UNIQUE INDEX doorloop_raw_properties_pkey ON public.doorloop_raw_properties USING btree (id)`