
import json
import os
import azure.functions as func
import requests
from lib.dropbox_client import temp_link

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

def sb_select_asset(asset_id: int):
    url = f"{SUPABASE_URL}/rest/v1/file_assets"
    headers = {
        "apikey": SUPABASE_SERVICE_ROLE_KEY,
        "Authorization": f"Bearer {SUPABASE_SERVICE_ROLE_KEY}"
    }
    params = {"id": f"eq.{asset_id}", "select": "dropbox_path,stored_filename"}
    r = requests.get(url, headers=headers, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()
    return data[0] if data else None

def main(req: func.HttpRequest) -> func.HttpResponse:
    asset_id = req.params.get("id")
    if not asset_id:
        return func.HttpResponse(json.dumps({"ok": False, "error": "id is required"}), status_code=400, mimetype="application/json")
    try:
        aid = int(asset_id)
    except ValueError:
        return func.HttpResponse(json.dumps({"ok": False, "error": "id must be int"}), status_code=400, mimetype="application/json")

    asset = sb_select_asset(aid)
    if not asset:
        return func.HttpResponse(json.dumps({"ok": False, "error": "asset not found"}), status_code=404, mimetype="application/json")

    full_path = f"{asset['dropbox_path']}/{asset['stored_filename']}"
    link = temp_link(full_path)
    return func.HttpResponse(json.dumps({"ok": True, "url": link}), mimetype="application/json")
