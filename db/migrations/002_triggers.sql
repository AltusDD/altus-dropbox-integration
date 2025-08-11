
create extension if not exists http with schema extensions;

do $$
declare
  fn_url text := 'https://YOUR_FUNCTION_HOST/api/dropbox_provision_folders?code=YOUR_FUNCTION_CODE';
begin
  execute format($f$
    create or replace function public.notify_dropbox_property()
    returns trigger as $$
    begin
      perform extensions.http((
        'POST', %L,
        array[extensions.http_header('content-type','application/json')],
        json_build_object('entity_type','property','new', row_to_json(NEW))::text
      )::extensions.http_request);
      return NEW;
    end $$ language plpgsql;
  $f$, fn_url);

  drop trigger if exists t_dropbox_property on public.properties;
  create trigger t_dropbox_property after insert on public.properties for each row execute function public.notify_dropbox_property();

  execute format($f$
    create or replace function public.notify_dropbox_unit()
    returns trigger as $$
    begin
      perform extensions.http((
        'POST', %L,
        array[extensions.http_header('content-type','application/json')],
        json_build_object('entity_type','unit','new', row_to_json(NEW))::text
      )::extensions.http_request);
      return NEW;
    end $$ language plpgsql;
  $f$, fn_url);
  drop trigger if exists t_dropbox_unit on public.units;
  create trigger t_dropbox_unit after insert on public.units for each row execute function public.notify_dropbox_unit();

  execute format($f$
    create or replace function public.notify_dropbox_lease()
    returns trigger as $$
    begin
      perform extensions.http((
        'POST', %L,
        array[extensions.http_header('content-type','application/json')],
        json_build_object('entity_type','lease','new', row_to_json(NEW))::text
      )::extensions.http_request);
      return NEW;
    end $$ language plpgsql;
  $f$, fn_url);
  drop trigger if exists t_dropbox_lease on public.leases;
  create trigger t_dropbox_lease after insert on public.leases for each row execute function public.notify_dropbox_lease();
end $$;
