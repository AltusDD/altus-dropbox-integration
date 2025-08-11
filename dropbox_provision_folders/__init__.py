import json, logging, dropbox
import azure.functions as func

from lib.pathmap import (
    owner_root, property_root, unit_root, lease_root,
    OWNER_SUBS, PROPERTY_SUBS, UNIT_SUBS, LEASE_SUBS
)
from lib.dropbox_client import DropboxClient

def _get_int(d, k):
    v = d.get(k)
    try:
        return None if v is None else int(v)
    except (TypeError, ValueError):
        return v

def _ensure_folder(client: DropboxClient, path: str):
    """
    Idempotently ensure a folder exists at `path` using the Dropbox SDK.
    """
    try:
        md = client.dbx.files_get_metadata(path)
        if isinstance(md, dropbox.files.FolderMetadata):
            return
        raise RuntimeError(f"Path exists but is not a folder: {path}")
    except dropbox.exceptions.ApiError as e:
        # create if not_found
        try:
            if e.error.is_path() and e.error.get_path().is_not_found():
                client.dbx.files_create_folder_v2(path, autorename=False)
                return
        except Exception:
            pass
        # if it's a conflict, treat as ok/idempotent
        if "conflict" in str(e).lower():
            return
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
            base = owner_root(data.get("name"), _get_int(data, "id"))
            _ensure_folder(client, base);  created.append(base)
            for s in OWNER_SUBS:
                p = f"{base}/{s}"
                _ensure_folder(client, p);  created.append(p)

        elif entity == "property":
            base = property_root(
                data.get("owner_name"), _get_int(data, "owner_id"),
                data.get("name"), _get_int(data, "id")
            )
            _ensure_folder(client, base);  created.append(base)
            for s in PROPERTY_SUBS:
                p = f"{base}/{s}"
                _ensure_folder(client, p);  created.append(p)

        elif entity == "unit":
            base = unit_root(
                data.get("owner_name"), _get_int(data, "owner_id"),
                data.get("property_name"), _get_int(data, "property_id"),
                data.get("name"), _get_int(data, "id")
            )
            _ensure_folder(client, base);  created.append(base)
            for s in UNIT_SUBS:
                p = f"{base}/{s}"
                _ensure_folder(client, p);  created.append(p)

        elif entity == "lease":
            base = lease_root(
                data.get("owner_name"), _get_int(data, "owner_id"),
                data.get("property_name"), _get_int(data, "property_id"),
                _get_int(data, "id")
            )
            _ensure_folder(client, base);  created.append(base)
            for s in LEASE_SUBS:
                p = f"{base}/{s}"
                _ensure_folder(client, p);  created.append(p)

        else:
            return func.HttpResponse("unknown entity_type", status_code=400)

        return func.HttpResponse(
            json.dumps({"ok": True, "created": created}),
            mimetype="application/json"
        )

    except Exception as e:
        logging.exception("Provision failed")
        return func.HttpResponse(
            json.dumps({"ok": False, "error": str(e)}),
            mimetype="application/json",
            status_code=500
        )
