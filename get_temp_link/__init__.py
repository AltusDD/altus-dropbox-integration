import azure.functions as func, os, json, httpx
from lib.dropbox_client import get_temp_link

SUPABASE_URL = os.getenv("SUPABASE_URL")
KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

def sb_get_asset(aid: int):
    headers={"apikey":KEY,"Authorization":f"Bearer {KEY}"}
    with httpx.Client(timeout=15) as c:
        r = c.get(f"{SUPABASE_URL}/rest/v1/file_assets", headers=headers, params={"id": f"eq.{aid}", "select":"dropbox_path,stored_filename"})
        r.raise_for_status()
        j = r.json()
        if not j: raise ValueError("asset not found")
        return j[0]

def main(req: func.HttpRequest):
    aid = req.params.get("id")
    if not aid: return func.HttpResponse("id required", status_code=400)
    asset = sb_get_asset(int(aid))
    full = f"{asset['dropbox_path']}"
    url = get_temp_link(full)
    return func.HttpResponse(json.dumps({"ok": True, "url": url}), mimetype="application/json")
