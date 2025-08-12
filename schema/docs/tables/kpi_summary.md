# Table `kpi_summary`

**Primary Key:** `id`

## Columns

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int8` | `NO` | `` |
| `kpis` | `jsonb` | `NO` | `` |
| `updated_at` | `timestamptz` | `NO` | `now()` |

## Indexes

- `kpi_summary_pkey` — `CREATE UNIQUE INDEX kpi_summary_pkey ON public.kpi_summary USING btree (id)`