# Table `sql_execution_logs`

**Primary Key:** `id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int8` | `NO` | `` |
| `executed_at` | `timestamptz` | `NO` | `now()` |
| `sql_file` | `text` | `YES` | `` |
| `sql_content` | `text` | `NO` | `` |
| `execution_time_ms` | `float8` | `YES` | `` |
| `status` | `text` | `NO` | `` |
| `error_message` | `text` | `YES` | `` |
| `error_detail` | `text` | `YES` | `` |

## Indexes

- `sql_execution_logs_pkey` — `CREATE UNIQUE INDEX sql_execution_logs_pkey ON public.sql_execution_logs USING btree (id)`