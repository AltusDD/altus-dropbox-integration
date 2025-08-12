# Table `case_history`

**Primary Key:** `id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `uuid` | `NO` | `gen_random_uuid()` |
| `legal_case_id` | `uuid` | `YES` | `` |
| `change_type` | `text` | `NO` | `` |
| `changed_by` | `text` | `YES` | `` |
| `change_details` | `jsonb` | `YES` | `` |
| `created_at` | `timestamptz` | `YES` | `now()` |

## Indexes

- `case_history_pkey` — `CREATE UNIQUE INDEX case_history_pkey ON public.case_history USING btree (id)`
- `idx_case_history_change_type` — `CREATE INDEX idx_case_history_change_type ON public.case_history USING btree (change_type)`
- `idx_case_history_legal_case_id` — `CREATE INDEX idx_case_history_legal_case_id ON public.case_history USING btree (legal_case_id)`