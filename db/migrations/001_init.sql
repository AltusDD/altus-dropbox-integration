
create table if not exists public.file_sync_audit (
  id bigserial primary key,
  action text not null,
  entity_type text not null,
  entity_id bigint not null,
  dropbox_path text not null,
  status text not null,
  detail jsonb,
  created_at timestamptz default now()
);

create table if not exists public.file_assets (
  id bigserial primary key,
  entity_type text not null,
  entity_id bigint not null,
  original_filename text not null,
  stored_filename text not null,
  dropbox_path text not null,
  content_hash text,
  size_bytes bigint,
  uploaded_by text,
  created_at timestamptz default now()
);

create index if not exists file_assets_entity_idx on public.file_assets (entity_type, entity_id);
