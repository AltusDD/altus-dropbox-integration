
import json
import logging
import os
import base64
import azure.functions as func
import requests
from lib.pathmap import upload_folder_for
from lib.naming import stamped_filename
from lib.dropbox_client import upload_bytes, ensure_folder

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

def sb_insert(table: str, row: dict):
    url = f"{SUPABASE_URL}/rest/v1/{table}"
    headers = {
        "apikey": SUPABASE_SERVICE_ROLE_KEY,
        "Authorization": f"Bearer {SUPABASE_SERVICE_ROLE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    }
    r = requests.post(url, headers=headers, json=row, timeout=15)
    r.raise_for_status()
    data = r.json()
    return data[0] if isinstance(data, list) and data else data

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        body = req.get_json()
    except ValueError:
        return func.HttpResponse(json.dumps({"ok": False, "error": "Invalid JSON"}), status_code=400, mimetype="application/json")

    entity_type = body.get("entity_type")
    meta = body.get("meta") or {}
    original_filename = body.get("original_filename") or "file.bin"
    file_b64 = body.get("file_base64")
    if not (entity_type and file_b64):
        return func.HttpResponse(json.dumps({"ok": False, "error": "Missing entity_type or file_base64"}), status_code=400, mimetype="application/json")

    try:
        binary = base64.b64decode(file_b64)
    except Exception:
        return func.HttpResponse(json.dumps({"ok": False, "error": "Bad base64"}), status_code=400, mimetype="application/json")

    folder = upload_folder_for(entity_type, meta)
    ensure_folder(folder)
    stored_filename = stamped_filename(original_filename)

    res = upload_bytes(folder, stored_filename, binary)

    try:
        sb_insert("file_sync_audit", {
            "action": "upload",
            "entity_type": entity_type,
            "entity_id": int(meta.get("lease_id") or meta.get("unit_id") or meta.get("property_id") or 0),
            "dropbox_path": folder,
            "status": "success",
            "detail": {"original_filename": original_filename, "stored_filename": stored_filename}
        })
        asset = sb_insert("file_assets", {
            "entity_type": entity_type,
            "entity_id": int(meta.get("lease_id") or meta.get("unit_id") or meta.get("property_id") or 0),
            "original_filename": original_filename,
            "stored_filename": stored_filename,
            "dropbox_path": folder,
            "content_hash": res.get("content_hash"),
            "size_bytes": res.get("size"),
            "uploaded_by": str(meta.get("actor") or "system")
        })
    except Exception as ex:
        logging.exception("Supabase insert failed")
        return func.HttpResponse(json.dumps({
            "ok": True,
            "warning": "Upload succeeded, but Supabase insert failed",
            "folder": folder,
            "stored_filename": stored_filename,
            "dropbox": res
        }), mimetype="application/json", status_code=207)

    return func.HttpResponse(json.dumps({
        "ok": True,
        "folder": folder,
        "stored_filename": stored_filename,
        "dropbox": res,
        "asset": asset
    }), mimetype="application/json")
