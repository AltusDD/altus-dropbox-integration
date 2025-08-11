
import os, json, base64, re
import azure.functions as func
import dropbox
from lib.dropbox_client import DropboxClient
from lib.pathmap import property_root, unit_root

def _slug(s):
    return re.sub(r'[^a-z0-9]+','-', (s or '').strip().lower()).strip('-') or 'file'

def _path_for(meta, category):
    owner_name   = meta.get('owner_name');   owner_id   = meta.get('owner_id')
    property_nm  = meta.get('property_name');property_id= meta.get('property_id')
    unit_name    = meta.get('unit_name');    unit_id    = meta.get('unit_id')

    prop_root = property_root(owner_name, owner_id, property_nm, property_id)
    unit_base = unit_root(owner_name, owner_id, property_nm, property_id, unit_name, unit_id)

    if category == 'media-unit': return f'{unit_base}/06_Media'
    if category == 'media-property': return f'{prop_root}/11_Media'
    if category == 'inspection': return f'{unit_base}/03_Inspections'
    if category == 'workorder': return f'{unit_base}/04_Work_Orders'
    return f'{unit_base}/06_Media'

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        body = req.get_json()
    except Exception:
        return func.HttpResponse('Invalid JSON', status_code=400)

    source  = (body.get('source') or '').lower()
    payload = body.get('payload') or {}

    meta = {}
    filename = None
    raw_b64 = None
    category = 'media-unit'

    if source == 'fieldapp':
        meta = {
            'owner_id': payload.get('owner_id'),
            'owner_name': payload.get('owner_name'),
            'property_id': payload.get('property_id'),
            'property_name': payload.get('property_name'),
            'unit_id': payload.get('unit_id'),
            'unit_name': payload.get('unit_name'),
            'actor_id': payload.get('actor_id'),
        }
        filename = payload.get('file_name') or 'fieldapp.bin'
        raw_b64  = payload.get('file_base64')
        category = payload.get('category') or 'media-unit'

    elif source == 'dealroom':
        meta = {
            'owner_id': payload.get('owner_id'),
            'owner_name': payload.get('owner_name'),
            'property_id': payload.get('property_id'),
            'property_name': payload.get('property_name'),
        }
        filename = payload.get('file_name') or 'dealroom.bin'
        raw_b64  = payload.get('file_base64')
        category = payload.get('category') or 'media-property'

    else:
        return func.HttpResponse('Unknown source', status_code=400)

    if not raw_b64:
        return func.HttpResponse('Missing file_base64', status_code=400)

    data = base64.b64decode(raw_b64)
    client = DropboxClient.from_env()

    folder = _path_for(meta, category)
    try:
        client.create_folder_if_not_exists(folder)
    except Exception:
        pass

    safe = re.sub(r'[\\/:*?"<>|]+', '-', filename).strip() or 'file.bin'
    path = f'{folder}/{safe}'
    res = client.upload_bytes(path, data)

    return func.HttpResponse(json.dumps({'ok': True, 'path': getattr(res, 'path_display', None) or path}), mimetype='application/json')
