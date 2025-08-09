from __future__ import annotations
import os, json
import azure.functions as func
import httpx
from lib.dropbox_client import get_temp_link

SUPABASE_URL = os.environ["SUPABASE_URL"].rstrip("/")
SUPABASE_SERVICE_ROLE_KEY = os.environ["SUPABASE_SERVICE_ROLE_KEY"]

def _sb_get_asset(asset_id: int) -> str:
    url = f"{SUPABASE_URL}/rest/v1/file_assets?id=eq.{asset_id}&select=dropbox_path"
    headers = {
        "apikey": SUPABASE_SERVICE_ROLE_KEY,
        "Authorization": f"Bearer {SUPABASE_SERVICE_ROLE_KEY}",
    }
    with httpx.Client(timeout=15) as c:
        r = c.get(url, headers=headers)
        r.raise_for_status()
        rows = r.json()
        if not rows:
            raise ValueError("asset not found")
        return rows[0]["dropbox_path"]


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        asset_id = int(req.params.get("id"))
        path = _sb_get_asset(asset_id)
        url = get_temp_link(path)
        return func.HttpResponse(json.dumps({"url": url}), mimetype="application/json")
    except Exception as e:
        return func.HttpResponse(str(e), status_code=400)
