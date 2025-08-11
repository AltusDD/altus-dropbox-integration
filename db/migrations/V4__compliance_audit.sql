-- V4__compliance_audit.sql
CREATE TABLE IF NOT EXISTS public.required_documents (
  id BIGSERIAL PRIMARY KEY,
  entity_type TEXT NOT NULL,
  document_description TEXT NOT NULL,
  canonical_folder_name TEXT NOT NULL,
  is_mandatory BOOLEAN DEFAULT TRUE
);

INSERT INTO public.required_documents (entity_type, document_description, canonical_folder_name)
VALUES
  ('lease', 'Signed Lease Agreement', 'Signed_Lease_Agreement'),
  ('lease', 'Tenant Correspondence', 'Tenant_Correspondence')
ON CONFLICT DO NOTHING;

CREATE OR REPLACE VIEW public.vw_missing_documents_audit AS
SELECT
  'lease'::text AS entity_type,
  l.id AS entity_id,
  l.name AS entity_name,
  rd.document_description AS missing_document
FROM public.leases l
CROSS JOIN public.required_documents rd
LEFT JOIN public.file_assets fa
  ON fa.lease_id = l.id
  AND fa.dropbox_path ILIKE '%' || rd.canonical_folder_name || '%'
WHERE rd.entity_type = 'lease' AND fa.id IS NULL;
