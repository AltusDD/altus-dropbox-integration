import os, json, azure.functions as func, httpx
from lib.dropbox_client import DropboxClient

def main(req: func.HttpRequest) -> func.HttpResponse:
    path = req.params.get("path")
    asset_id = req.params.get("id")
    link = None
    client = DropboxClient.from_env()

    if path:
        link = client.temp_link(path)
    elif asset_id:
        # best-effort Supabase lookup
        url = os.getenv("SUPABASE_URL"); key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
        try:
            with httpx.Client(timeout=20) as c:
                r = c.get(f"{url}/rest/v1/file_assets", headers={"apikey": key, "Authorization": f"Bearer {key}"}, params={"id":"eq."+asset_id,"select":"dropbox_path","limit":"1"})
                if r.status_code == 200 and r.json():
                    path = r.json()[0]["dropbox_path"]
                    link = client.temp_link(path)
        except Exception:
            pass

    if not link:
        return func.HttpResponse("Not found", status_code=404)
    return func.HttpResponse(json.dumps({"ok": True, "link": link}), mimetype="application/json")
