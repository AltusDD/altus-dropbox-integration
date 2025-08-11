
-- db/migrations/V7__required_documents.sql

create table if not exists public.required_documents (
  id serial primary key,
  entity_type text not null, -- 'lease' | 'property' | 'unit' | 'owner'
  document_description text not null,
  canonical_folder_name text not null,
  is_mandatory boolean default true
);

-- seed examples
insert into public.required_documents (entity_type, document_description, canonical_folder_name) values
  ('lease', 'Signed Lease Agreement', '02_Lease/Signed'),
  ('lease', 'Tenant Correspondence', '03_Correspondence'),
  ('property', 'Acquisition Docs', '08_Acquisition_Docs')
on conflict do nothing;

-- simple audit view using file_assets
create or replace view public.vw_missing_documents_audit as
with entities as (
  select 'lease'::text as entity_type, id, coalesce(tenant_name,'') as name from public.leases
  union all
  select 'property', id, coalesce(name,'') from public.properties
)
select
  rd.entity_type,
  e.id as entity_id,
  e.name as entity_name,
  rd.document_description as missing_document
from required_documents rd
join entities e on e.entity_type = rd.entity_type
left join file_assets fa
  on (rd.entity_type = 'lease' and fa.lease_id = e.id and fa.dropbox_path like '%' || rd.canonical_folder_name)
  or (rd.entity_type = 'property' and fa.property_id = e.id and fa.dropbox_path like '%' || rd.canonical_folder_name)
where fa.id is null;
