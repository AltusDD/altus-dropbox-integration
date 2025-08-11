-- db/migrations/V3__ownerships.sql
create table if not exists public.property_ownerships (
  id bigserial primary key,
  property_id bigint not null,
  owner_id bigint not null,
  start_date date not null,
  end_date date,
  created_at timestamptz default now()
);
create index if not exists idx_po_prop on public.property_ownerships(property_id);
create index if not exists idx_po_owner on public.property_ownerships(owner_id);

-- helper view: current owner
create or replace view public.v_property_owner_current as
select distinct on (property_id)
  property_id, owner_id, start_date, end_date
from public.property_ownerships
where end_date is null
order by property_id, start_date desc;

-- transfer audit table
create table if not exists public.ownership_transfers (
  id bigserial primary key,
  property_id bigint not null,
  from_owner_id bigint not null,
  to_owner_id bigint not null,
  cutoff_date date not null,
  src_path text not null,
  dst_path text not null,
  moved_count integer default 0,
  created_at timestamptz default now()
);
