import json, logging
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

    paths = []

    if entity == "owner":
        base = owner_root(data.get("name"), _get_int(data, "id"))
        paths.append(base)
        paths += [f"{base}/{s}" for s in OWNER_SUBS]

    elif entity == "property":
        base = property_root(
            data.get("owner_name"), _get_int(data, "owner_id"),
            data.get("name"), _get_int(data, "id")
        )
        paths.append(base)
        paths += [f"{base}/{s}" for s in PROPERTY_SUBS]

    elif entity == "unit":
        base = unit_root(
            data.get("owner_name"), _get_int(data, "owner_id"),
            data.get("property_name"), _get_int(data, "property_id"),
            data.get("name"), _get_int(data, "id")
        )
        paths.append(base)
        paths += [f"{base}/{s}" for s in UNIT_SUBS]

    elif entity == "lease":
        base = lease_root(
            data.get("owner_name"), _get_int(data, "owner_id"),
            data.get("property_name"), _get_int(data, "property_id"),
            _get_int(data, "id")
        )
        paths.append(base)
        paths += [f"{base}/{s}" for s in LEASE_SUBS]

    else:
        return func.HttpResponse("unknown entity_type", status_code=400)

    created = []
    try:
        for p in paths:
            client.create_folder_if_not_exists(p)
            created.append(p)
    except Exception as e:
        logging.exception("Folder create failed")
        return func.HttpResponse(
            json.dumps({"ok": False, "failed_path": p, "created": created, "error": str(e)}),
            mimetype="application/json", status_code=500
        )

    return func.HttpResponse(json.dumps({"ok": True, "created": created}), mimetype="application/json")
