from __future__ import annotations
import os, json, base64, logging, datetime as dt
from typing import Tuple, Optional
import azure.functions as func
import httpx
from requests_toolbelt.multipart.decoder import MultipartDecoder
from lib.dropbox_client import upload_file
from lib.pathmap import upload_target
from lib.naming import canonical_filename

SUPABASE_URL = os.environ["SUPABASE_URL"].rstrip("/")
SUPABASE_SERVICE_ROLE_KEY = os.environ["SUPABASE_SERVICE_ROLE_KEY"]

def _sb_insert(table: str, row: dict):
    url = f"{SUPABASE_URL}/rest/v1/{table}"
    headers = {
        "apikey": SUPABASE_SERVICE_ROLE_KEY,
        "Authorization": f"Bearer {SUPABASE_SERVICE_ROLE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=representation",
    }
    with httpx.Client(timeout=30) as c:
        r = c.post(url, headers=headers, json=row)
        r.raise_for_status()
        return r.json()


def _parse_multipart(req: func.HttpRequest) -> Tuple[str, dict, bytes, str]:
    ct = req.headers.get("content-type") or req.headers.get("Content-Type")
    if not ct or "multipart/form-data" not in ct:
        raise ValueError("Not multipart")
    dec = MultipartDecoder(req.get_body(), ct)

    entity_type: Optional[str] = None
    meta: dict = {}
    file_bytes: Optional[bytes] = None
    original_filename: Optional[str] = None

    for part in dec.parts:
        cd = part.headers.get(b"Content-Disposition", b"").decode("utf-8", "ignore")
        def _extract(name: str):
            key = f'{name}="'
            if key in cd:
                after = cd.split(key, 1)[1]
                return after.split('"', 1)[0]
            return None
        field_name = _extract("name")
        if field_name == "entity_type":
            entity_type = part.text
        elif field_name == "meta":
            try:
                meta = json.loads(part.text or "{}")
            except Exception:
                meta = {}
        elif field_name == "file":
            file_bytes = part.content
            original_filename = _extract("filename") or "upload.bin"

    if not entity_type or file_bytes is None or original_filename is None:
        raise ValueError("Missing multipart fields: entity_type/meta/file")
    return entity_type, meta, file_bytes, original_filename


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        ct = (req.headers.get("content-type") or "").lower()
        if "multipart/form-data" in ct:
            entity_type, meta, file_bytes, original_filename = _parse_multipart(req)
        else:
            body = req.get_json()
            entity_type = body["entity_type"]
            meta = body.get("meta", {})
            original_filename = body["original_filename"]
            file_bytes = base64.b64decode(body["file_base64"])  # raises on invalid

        today = dt.date.today()
        name_no_ext, sep, ext = original_filename.rpartition(".")
        ext = ext if sep else "bin"
        base_desc = name_no_ext or "file"
        stored_name = canonical_filename(today, entity_type, base_desc, ext)

        target_folder = upload_target(entity_type, meta)
        full_path = f"{target_folder}/{stored_name}"

        res = upload_file(full_path, file_bytes)

        file_row = {
            "entity_type": entity_type,
            "entity_id": meta.get("lease_id") or meta.get("unit_id") or meta.get("property_id"),
            "original_filename": original_filename,
            "stored_filename": stored_name,
            "dropbox_path": res["path_lower"],
            "content_hash": res["content_hash"],
            "size_bytes": res["size"],
            "uploaded_by": meta.get("actor"),
        }
        _sb_insert("file_assets", file_row)

        return func.HttpResponse(
            json.dumps({"ok": True, "path": res["path_lower"]}),
            status_code=200,
            mimetype="application/json",
        )
    except Exception as e:
        logging.exception("upload error")
        return func.HttpResponse(str(e), status_code=500)
