
import json
import logging
import os
import azure.functions as func
from lib.pathmap import canonical_folders_for
from lib.dropbox_client import ensure_folder
import requests

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

def supabase_insert_audit(payload: dict):
    try:
        url = f"{SUPABASE_URL}/rest/v1/file_sync_audit"
        headers = {
            "apikey": SUPABASE_SERVICE_ROLE_KEY,
            "Authorization": f"Bearer {SUPABASE_SERVICE_ROLE_KEY}",
            "Content-Type": "application/json",
            "Prefer": "return=representation"
        }
        requests.post(url, headers=headers, json=payload, timeout=10)
    except Exception as ex:
        logging.warning("Supabase audit insert failed: %s", ex)

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        body = req.get_json()
    except ValueError:
        return func.HttpResponse(json.dumps({"ok": False, "error": "Invalid JSON"}), status_code=400, mimetype="application/json")

    entity_type = str(body.get("entity_type", "")).lower()
    new_obj = body.get("new") or {}
    folders = canonical_folders_for(entity_type, new_obj)

    created = []
    for f in folders:
        try:
            ensure_folder(f)
            created.append(f)
            supabase_insert_audit({
                "action": "create_folder",
                "entity_type": entity_type,
                "entity_id": int(new_obj.get("id", 0)),
                "dropbox_path": f,
                "status": "success",
                "detail": None
            })
        except Exception as ex:
            supabase_insert_audit({
                "action": "create_folder",
                "entity_type": entity_type,
                "entity_id": int(new_obj.get("id", 0)),
                "dropbox_path": f,
                "status": "error",
                "detail": {"error": str(ex)}
            })
            logging.exception("Folder create failed for %s", f)

    return func.HttpResponse(json.dumps({"ok": True, "created": created}), mimetype="application/json")
