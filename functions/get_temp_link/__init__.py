
import os, json
import azure.functions as func
import httpx
from lib.dropbox_client import DropboxClient

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_SERVICE_ROLE_KEY')

def _hdrs():
    return {'apikey': SUPABASE_KEY, 'Authorization': f'Bearer {SUPABASE_KEY}'}

def _lookup_path_by_asset_id(asset_id: int):
    with httpx.Client(timeout=10) as c:
        r = c.get(f"{SUPABASE_URL}/rest/v1/file_assets", headers=_hdrs(), params={'id': f'eq.{asset_id}', 'select': 'dropbox_path'})
        if r.status_code == 200 and r.json():
            return r.json()[0]['dropbox_path']
    return None

def main(req: func.HttpRequest) -> func.HttpResponse:
    if req.method == 'GET':
        asset_id = req.params.get('asset_id')
        path = req.params.get('path')
    else:
        try:
            body = req.get_json()
        except Exception:
            body = {}
        asset_id = body.get('asset_id')
        path = body.get('path')

    if asset_id and not path:
        try:
            path = _lookup_path_by_asset_id(int(asset_id))
        except Exception:
            path = None

    if not path:
        return func.HttpResponse('Provide asset_id or path', status_code=400)

    client = DropboxClient.from_env()
    link = client.dbx.files_get_temporary_link(path).link
    return func.HttpResponse(json.dumps({'ok': True, 'path': path, 'link': link}), mimetype='application/json')
