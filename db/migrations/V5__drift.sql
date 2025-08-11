
-- db/migrations/V5__drift.sql
create table if not exists public.drift_audit (
  id bigserial primary key,
  entity text not null,
  key text not null,
  action text not null, -- created|exists|error
  detail text,
  created_at timestamptz default now()
);
