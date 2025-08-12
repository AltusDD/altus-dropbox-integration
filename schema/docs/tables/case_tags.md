# Table `case_tags`

**Primary Key:** `id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `uuid` | `NO` | `gen_random_uuid()` |
| `legal_case_id` | `uuid` | `YES` | `` |
| `tag` | `text` | `NO` | `` |
| `created_at` | `timestamptz` | `YES` | `now()` |

## Indexes

- `case_tags_pkey` — `CREATE UNIQUE INDEX case_tags_pkey ON public.case_tags USING btree (id)`
- `idx_case_tags_legal_case_id` — `CREATE INDEX idx_case_tags_legal_case_id ON public.case_tags USING btree (legal_case_id)`
- `idx_case_tags_tag` — `CREATE INDEX idx_case_tags_tag ON public.case_tags USING btree (tag)`