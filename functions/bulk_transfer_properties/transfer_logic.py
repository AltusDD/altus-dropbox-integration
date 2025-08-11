
import os, json
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

def do_transfer(src, dst, prop, dry):
    src_name = src.get('name'); src_id = src.get('id')
    dst_name = dst.get('name'); dst_id = dst.get('id')
    p_name   = prop.get('name'); p_id  = prop.get('id')

    client = DropboxClient.from_env()
    dbx = client.dbx

    old_root = property_root(src_name, src_id, p_name, p_id)
    new_root = property_root(dst_name, dst_id, p_name, p_id)

    result = {'property_id': p_id, 'old_root': old_root, 'new_root': new_root, 'moved': False, 'updated_rows': 0}

    if not dry:
        try:
            _ensure_owner_folders(dbx, dst_name, dst_id)
            dbx.files_move_v2(from_path=old_root, to_path=new_root, allow_shared_folder=True, autorename=False)
            result['moved'] = True
        except dropbox.exceptions.ApiError as e:
            result['dropbox_error'] = str(e)

        # update file_assets paths
        updated = 0; page = 0
        while True:
            params = {'select':'id,dropbox_path', 'property_id': f'eq.{p_id}', 'dropbox_path': f'ilike.{old_root}%',
                      'limit':'1000', 'offset': str(page*1000)}
            r = httpx.get(f"{SUPABASE_URL}/rest/v1/file_assets", headers=_hdrs(), params=params, timeout=30.0)
            if r.status_code != 200: break
            rows = r.json()
            if not rows: break
            for row in rows:
                newp = row["dropbox_path"].replace(old_root, new_root, 1)
                httpx.patch(f"{SUPABASE_URL}/rest/v1/file_assets", headers=_hdrs(),
                            params={'id': f"eq.{row["id"]}"}, json={'dropbox_path': newp}, timeout=30.0)
                updated += 1
            page += 1
        result['updated_rows'] = updated

    return result
