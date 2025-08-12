# Table `doorloop_raw_units`

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
| `inEviction` | `bool` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `amenities` | `jsonb` | `YES` | `` |
| `baths` | `numeric` | `YES` | `` |
| `address` | `jsonb` | `YES` | `` |
| `batch` | `text` | `YES` | `` |
| `addressSameAsProperty` | `bool` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `listed` | `bool` | `YES` | `` |
| `name` | `text` | `YES` | `` |
| `property` | `text` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `rentalApplicationListing` | `jsonb` | `YES` | `` |
| `pictures` | `jsonb` | `YES` | `` |
| `listing` | `jsonb` | `YES` | `` |
| `size` | `int8` | `YES` | `` |
| `description` | `text` | `YES` | `` |
| `beds` | `int8` | `YES` | `` |
| `marketRent` | `int8` | `YES` | `` |

## Indexes

- `doorloop_raw_units_pkey` — `CREATE UNIQUE INDEX doorloop_raw_units_pkey ON public.doorloop_raw_units USING btree (id)`