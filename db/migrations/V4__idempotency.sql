
-- db/migrations/V4__idempotency.sql
create table if not exists public.upload_requests (
  idempotency_key text primary key,
  response jsonb not null,
  created_at timestamptz default now()
);
