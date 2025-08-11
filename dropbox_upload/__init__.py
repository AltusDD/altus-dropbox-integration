import azure.functions as func
import os, json, base64, httpx, hashlib
from lib.pathmap import folder_for
from lib.dropbox_client import ensure_folder, upload

SUPABASE_URL = os.getenv("SUPABASE_URL")
KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

def sb_insert(table: str, row: dict):
    headers={"apikey":KEY,"Authorization":f"Bearer {KEY}","Content-Type":"application/json","Prefer":"return=representation"}
    with httpx.Client(timeout=20) as c:
        r = c.post(f"{SUPABASE_URL}/rest/v1/{table}", headers=headers, json=row)
        r.raise_for_status()
        return r.json()[0]

def main(req: func.HttpRequest):
    b = req.get_json()
    et = b["entity_type"]
    meta = b.get("meta", {})
    name = b["original_filename"]
    data = base64.b64decode(b["file_base64"])
    folder = folder_for(et, meta)
    ensure_folder(folder)
    meta_dbx = upload(folder, name, data)
    row = {
        "entity_type": et,
        "entity_id": int(meta.get("lease_id") or meta.get("unit_id") or meta.get("property_id") or 0),
        "original_filename": name,
        "stored_filename": meta_dbx.get("name", name),
        "dropbox_path": meta_dbx.get("path_display", f"{folder}/{name}"),
        "content_hash": hashlib.sha256(data).hexdigest(),
        "size_bytes": len(data),
        "uploaded_by": meta.get("actor","api")
    }
    saved = sb_insert("file_assets", row)
    return func.HttpResponse(json.dumps({"ok": True, "asset": saved}), mimetype="application/json")
