import json
import logging
import dropbox
import azure.functions as func

from lib.pathmap import (
    owner_root, property_root, unit_root, lease_root,
    OWNER_SUBS, PROPERTY_SUBS, UNIT_SUBS, LEASE_SUBS
)
from lib.dropbox_client import DropboxClient


def _get_int(d: dict, key: str):
    """Safely cast d[key] to int when present."""
    v = (d or {}).get(key)
    try:
        return None if v is None else int(v)
    except (TypeError, ValueError):
        return v


def _ensure_folder(client: DropboxClient, path: str):
    """
    Idempotently ensure a folder exists at `path`.

    We *create first* and treat 'conflict' as success. This avoids tricky
    metadata checks and works even with eventual consistency.
    """
    try:
        client.dbx.files_create_folder_v2(path, autorename=False)
        logging.info("Created folder: %s", path)
    except dropbox.exceptions.ApiError as e:
        msg = str(e).lower()
        if "conflict" in msg:
            # Already there -> OK
            logging.info("Folder already exists (ok): %s", path)
            return
        # If parent is missing, msg often contains 'not_found'
        logging.error("Failed creating folder '%s': %s", path, e)
        raise


def _plan_paths(entity: str, data: dict):
    """
    Compute the base folder and subfolders to create for the given entity.
    Returns (base_path, [subfolder_names]).
    """
    entity = (entity or "").strip().lower()

    if entity == "owner":
        base = owner_root(data.get("name"), _get_int(data, "id"))
        subs = OWNER_SUBS
        return base, subs

    if entity == "property":
        base = property_root(
            data.get("owner_name"), _get_int(data, "owner_id"),
            data.get("name"), _get_int(data, "id"),
        )
        subs = PROPERTY_SUBS
        return base, subs

    if entity == "unit":
        base = unit_root(
            data.get("owner_name"), _get_int(data, "owner_id"),
            data.get("property_name"), _get_int(data, "property_id"),
            data.get("name"), _get_int(data, "id"),
        )
        subs = UNIT_SUBS
        return base, subs

    if entity == "lease":
        base = lease_root(
            data.get("owner_name"), _get_int(data, "owner_id"),
            data.get("property_name"), _get_int(data, "property_id"),
            _get_int(data, "id"),
        )
        subs = LEASE_SUBS
        return base, subs

    raise ValueError(f"unknown entity_type: {entity}")


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("dropbox_provision_folders: start")

    # Parse input JSON
    try:
        body = req.get_json()
    except ValueError:
        return func.HttpResponse("Invalid JSON", status_code=400)

    entity = body.get("entity_type")
    data = body.get("new") or {}

    # Init Dropbox client from env
    try:
        client = DropboxClient.from_env()
    except Exception as e:
        logging.exception("Dropbox client init failed")
        return func.HttpResponse(f"Server config error: {e}", status_code=500)

    # Plan and create folders
    try:
        base, subs = _plan_paths(entity, data)
        created = []

        _ensure_folder(client, base)
        created.append(base)

        for s in subs:
            p = f"{base}/{s}"
            _ensure_folder(client, p)
            created.append(p)

        return func.HttpResponse(
            json.dumps({"ok": True, "created": created}),
            mimetype="application/json"
        )

    except ValueError as ve:
        # unknown entity_type, bad inputs, etc.
        logging.warning("Bad request: %s", ve)
        return func.HttpResponse(str(ve), status_code=400)

    except Exception as e:
        logging.exception("Provision failed")
        return func.HttpResponse(
            json.dumps({"ok": False, "error": str(e)}),
            mimetype="application/json",
            status_code=500
        )
