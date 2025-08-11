import azure.functions as func
import os, json, base64, httpx, hashlib, time
from lib.pathmap import canonical_folder
from lib.dropbox_client import ensure_folder, upload

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

def _sb_insert_file_asset(row: dict) -> dict:
    url = f"{SUPABASE_URL}/rest/v1/file_assets"
    headers = {
        "apikey": SUPABASE_SERVICE_ROLE_KEY,
        "Authorization": f"Bearer {SUPABASE_SERVICE_ROLE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    }
    with httpx.Client(timeout=20) as c:
        r = c.post(url, headers=headers, json=row)
        r.raise_for_status()
        return r.json()[0]

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        body = req.get_json()
        entity_type = body["entity_type"]
        meta = body.get("meta", {})
        original_filename = body["original_filename"]
        file_b64 = body["file_base64"]
        content = base64.b64decode(file_b64)

        folder = canonical_folder(entity_type, meta)
        ensure_folder(folder)
        dbx_meta = upload(folder, original_filename, content)

        # persistent metadata (keep old columns if present in your DB)
        sha = hashlib.sha256(content).hexdigest()
        row = {
            "entity_type": entity_type,
            "entity_id": int(meta.get("lease_id") or meta.get("unit_id") or meta.get("property_id") or 0),
            "original_filename": original_filename,
            "stored_filename": dbx_meta.get("name", original_filename),
            "dropbox_path": dbx_meta.get("path_display", f"{folder}/{original_filename}"),
            "content_hash": sha,
            "size_bytes": len(content),
            "uploaded_by": meta.get("actor", "api")
        }
        saved = _sb_insert_file_asset(row)

        return func.HttpResponse(json.dumps({"ok": True, "asset": saved}), mimetype="application/json")
    except Exception as e:
        return func.HttpResponse(str(e), status_code=400)
