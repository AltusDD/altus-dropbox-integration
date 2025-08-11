-- V3__kpi_files_view.sql
CREATE MATERIALIZED VIEW IF NOT EXISTS public.vw_file_kpis_by_property AS
SELECT
  p.id AS property_id,
  p.name AS property_name,
  COUNT(fa.id) FILTER (WHERE fa.property_id = p.id) AS total_files,
  COUNT(fa.id) FILTER (WHERE fa.property_id = p.id AND fa.created_at > now() - interval '30 days') AS files_last_30d,
  MAX(fa.created_at) FILTER (WHERE fa.property_id = p.id) AS last_upload_at
FROM public.properties p
LEFT JOIN public.file_assets fa ON fa.property_id = p.id
GROUP BY p.id, p.name;

CREATE UNIQUE INDEX IF NOT EXISTS vw_file_kpis_by_property_pk ON public.vw_file_kpis_by_property(property_id);
