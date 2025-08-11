import azure.functions as func
import os, json, httpx
from lib.dropbox_client import get_temp_link

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

def _sb_get_path(asset_id: int) -> str:
    url = f"{SUPABASE_URL}/rest/v1/file_assets?id=eq.{asset_id}&select=dropbox_path"
    headers = {
        "apikey": SUPABASE_SERVICE_ROLE_KEY,
        "Authorization": f"Bearer {SUPABASE_SERVICE_ROLE_KEY}",
    }
    with httpx.Client(timeout=15) as c:
        r = c.get(url, headers=headers)
        r.raise_for_status()
        j = r.json()
        if not j:
            raise ValueError("asset not found")
        return j[0]["dropbox_path"]

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        asset_id = int(req.params.get("id"))
        path = _sb_get_path(asset_id)
        link = get_temp_link(path)
        return func.HttpResponse(json.dumps({"url": link}), mimetype="application/json")
    except Exception as e:
        return func.HttpResponse(str(e), status_code=400)
