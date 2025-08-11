# functions/dropbox_provision_folders/__init__.py
import json, logging, dropbox
import azure.functions as func
from lib.pathmap import (
    owner_root, property_root, unit_root, lease_root, tenancy_root,
    OWNER_SUBS, PROPERTY_SUBS, UNIT_SUBS, LEASE_SUBS, TENANCY_SUBS
)
from lib.dropbox_client import DropboxClient

def _get(d, k): return d.get(k)
def _get_int(d, k):
    v = d.get(k)
    try: return None if v is None else int(v)
    except (TypeError, ValueError): return v

def _ensure_folder(client: DropboxClient, path: str):
    try:
        client.dbx.files_create_folder_v2(path, autorename=False)
        logging.info("created %s", path)
    except dropbox.exceptions.ApiError as e:
        m = str(e).lower()
        if "conflict" in m:
            logging.info("exists %s", path)
            return
        logging.error("create failed %s :: %s", path, e)
        raise

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("dropbox_provision_folders starting")
    try:
        body = req.get_json()
    except ValueError:
        return func.HttpResponse("Invalid JSON", status_code=400)

    entity = (body.get("entity_type") or "").strip().lower()
    data = body.get("new") or {}

    try:
        client = DropboxClient.from_env()
    except Exception as e:
        logging.exception("Dropbox client init failed")
        return func.HttpResponse(f"Server config error: {e}", status_code=500)

    created = []
    try:
        if entity == "owner":
            base = owner_root(_get(data,"name"), _get_int(data,"id"))
            _ensure_folder(client, base); created.append(base)
            for s in OWNER_SUBS: _ensure_folder(client, f"{base}/{s}"); created.append(f"{base}/{s}")

        elif entity == "property":
            base = property_root(_get(data,"owner_name"), _get_int(data,"owner_id"),
                                 _get(data,"name"), _get_int(data,"id"))
            _ensure_folder(client, base); created.append(base)
            for s in PROPERTY_SUBS: _ensure_folder(client, f"{base}/{s}"); created.append(f"{base}/{s}")

        elif entity == "unit":
            base = unit_root(_get(data,"owner_name"), _get_int(data,"owner_id"),
                             _get(data,"property_name"), _get_int(data,"property_id"),
                             _get(data,"name"), _get_int(data,"id"))
            _ensure_folder(client, base); created.append(base)
            for s in UNIT_SUBS: _ensure_folder(client, f"{base}/{s}"); created.append(f"{base}/{s}")

        elif entity in ("tenancy","tenant"):
            unit_base = unit_root(_get(data,"owner_name"), _get_int(data,"owner_id"),
                                  _get(data,"property_name"), _get_int(data,"property_id"),
                                  _get(data,"unit_name"), _get_int(data,"unit_id"))
            _ensure_folder(client, unit_base)
            _ensure_folder(client, f"{unit_base}/02_Tenancies")

            base = tenancy_root(_get(data,"owner_name"), _get_int(data,"owner_id"),
                                _get(data,"property_name"), _get_int(data,"property_id"),
                                _get(data,"unit_name"), _get_int(data,"unit_id"), data)
            _ensure_folder(client, base); created.append(base)
            for s in TENANCY_SUBS: _ensure_folder(client, f"{base}/{s}"); created.append(f"{base}/{s}")

        elif entity == "lease_legacy":
            base = lease_root(_get(data,"owner_name"), _get_int(data,"owner_id"),
                              _get(data,"property_name"), _get_int(data,"property_id"),
                              _get_int(data,"id"))
            _ensure_folder(client, base); created.append(base)
            for s in LEASE_SUBS: _ensure_folder(client, f"{base}/{s}"); created.append(f"{base}/{s}")

        else:
            return func.HttpResponse("unknown entity_type", status_code=400)

        return func.HttpResponse(json.dumps({"ok": True, "created": created}), mimetype="application/json")

    except Exception as e:
        logging.exception("Provision failed")
        return func.HttpResponse(json.dumps({"ok": False, "error": str(e)}),
                                 mimetype="application/json", status_code=500)
