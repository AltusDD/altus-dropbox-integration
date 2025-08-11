-- V2__file_assets_fk_and_indexes.sql
-- Safe additive FKs; keep legacy columns if present

DO $$ BEGIN
  IF NOT EXISTS (SELECT 1 FROM information_schema.columns
                 WHERE table_schema='public' AND table_name='file_assets' AND column_name='property_id') THEN
    ALTER TABLE public.file_assets ADD COLUMN property_id BIGINT;
  END IF;
  IF NOT EXISTS (SELECT 1 FROM information_schema.columns
                 WHERE table_schema='public' AND table_name='file_assets' AND column_name='unit_id') THEN
    ALTER TABLE public.file_assets ADD COLUMN unit_id BIGINT;
  END IF;
  IF NOT EXISTS (SELECT 1 FROM information_schema.columns
                 WHERE table_schema='public' AND table_name='file_assets' AND column_name='lease_id') THEN
    ALTER TABLE public.file_assets ADD COLUMN lease_id BIGINT;
  END IF;
END $$;

-- FKs (defer errors if parent tables not present)
DO $$ BEGIN
  IF EXISTS (SELECT 1 FROM pg_class WHERE relname='properties') AND NOT EXISTS (
    SELECT 1 FROM pg_constraint WHERE conname='file_assets_property_fk'
  ) THEN
    ALTER TABLE public.file_assets ADD CONSTRAINT file_assets_property_fk FOREIGN KEY (property_id) REFERENCES public.properties(id) ON DELETE SET NULL;
  END IF;
  IF EXISTS (SELECT 1 FROM pg_class WHERE relname='units') AND NOT EXISTS (
    SELECT 1 FROM pg_constraint WHERE conname='file_assets_unit_fk'
  ) THEN
    ALTER TABLE public.file_assets ADD CONSTRAINT file_assets_unit_fk FOREIGN KEY (unit_id) REFERENCES public.units(id) ON DELETE SET NULL;
  END IF;
  IF EXISTS (SELECT 1 FROM pg_class WHERE relname='leases') AND NOT EXISTS (
    SELECT 1 FROM pg_constraint WHERE conname='file_assets_lease_fk'
  ) THEN
    ALTER TABLE public.file_assets ADD CONSTRAINT file_assets_lease_fk FOREIGN KEY (lease_id) REFERENCES public.leases(id) ON DELETE SET NULL;
  END IF;
END $$;

CREATE INDEX IF NOT EXISTS file_assets_property_idx ON public.file_assets(property_id);
CREATE INDEX IF NOT EXISTS file_assets_unit_idx ON public.file_assets(unit_id);
CREATE INDEX IF NOT EXISTS file_assets_lease_idx ON public.file_assets(lease_id);
CREATE INDEX IF NOT EXISTS file_assets_hash_idx ON public.file_assets(content_hash);
