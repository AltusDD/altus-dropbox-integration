
import os, json
import azure.functions as func
import httpx, dropbox
from lib.dropbox_client import DropboxClient
from lib.pathmap import owner_root, property_root

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_SERVICE_ROLE_KEY')

def _hdrs():
    return {'apikey': SUPABASE_KEY, 'Authorization': f'Bearer {SUPABASE_KEY}', 'content-type': 'application/json'}

def _ensure_owner_folders(dbx, owner_name, owner_id):
    base = owner_root(owner_name, owner_id)
    try:
        dbx.files_create_folder_v2(base, autorename=False)
    except dropbox.exceptions.ApiError as e:
        if 'conflict' not in str(e).lower(): pass
    # We don't need to create subs; moving full property tree includes its subs.

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        body = req.get_json()
    except Exception:
        return func.HttpResponse('Invalid JSON', status_code=400)

    src = body.get('from_owner') or {}
    dst = body.get('to_owner') or {}
    prop = body.get('property') or {}
    dry = bool(body.get('dry_run') or False)

    src_name = src.get('name'); src_id = src.get('id')
    dst_name = dst.get('name'); dst_id = dst.get('id')
    p_name   = prop.get('name'); p_id  = prop.get('id')

    if not (src_name and src_id and dst_name and dst_id and p_name and p_id):
        return func.HttpResponse('Missing owner/property ids or names', status_code=400)

    client = DropboxClient.from_env()
    dbx = client.dbx

    old_root = property_root(src_name, src_id, p_name, p_id)
    new_root = property_root(dst_name, dst_id, p_name, p_id)

    # ensure destination owner base exists
    _ensure_owner_folders(dbx, dst_name, dst_id)

    result = {'ok': True, 'old_root': old_root, 'new_root': new_root, 'moved': False, 'updated_rows': 0}

    if not dry:
        # 1) move in Dropbox
        try:
            dbx.files_move_v2(from_path=old_root, to_path=new_root, allow_shared_folder=True, autorename=False)
            result['moved'] = True
        except dropbox.exceptions.ApiError as e:
            # If already there or not found, report gracefully
            result['moved'] = False
            result['dropbox_error'] = str(e)

        # 2) update Supabase file paths for this property
        # fetch in pages of 1000
        updated = 0
        offset = 0
        page = 0
        while True:
            # get rows for this property_id whose path starts with old_root
            # PostgREST: use ilike for prefix match
            params = {'select':'id,dropbox_path', 'property_id': f'eq.{p_id}', 'dropbox_path': f'ilike.{old_root}%' , 'limit':'1000', 'offset': str(page*1000)}
            r = httpx.get(f"{SUPABASE_URL}/rest/v1/file_assets", headers=_hdrs(), params=params, timeout=30.0)
            if r.status_code != 200:
                break
            rows = r.json()
            if not rows: break
            for row in rows:
                old = row["dropbox_path"]
                new = old.replace(old_root, new_root, 1)
                patch = httpx.patch(f"{SUPABASE_URL}/rest/v1/file_assets", headers=_hdrs(),
                                    params={'id': f'eq.{row["id"]}'}, json={'dropbox_path': new}, timeout=30.0)
                if patch.status_code in (200,204):
                    updated += 1
            page += 1
        result['updated_rows'] = updated

    return func.HttpResponse(json.dumps(result), mimetype='application/json')
