
import os, re, json, base64
import azure.functions as func
from lib.dropbox_client import DropboxClient
from lib.pathmap import property_root, unit_root

def _slug(s: str):
    import re
    s = (s or '').strip().lower()
    return re.sub(r'[^a-z0-9]+','-',s).strip('-') or 'file'

def _path(meta, filename):
    owner_name   = meta.get('owner_name')
    owner_id     = meta.get('owner_id')
    property_nm  = meta.get('property_name')
    property_id  = meta.get('property_id')
    unit_name    = meta.get('unit_name')
    unit_id      = meta.get('unit_id')

    prop_root = property_root(owner_name, owner_id, property_nm, property_id)
    if unit_id:
        base = unit_root(owner_name, owner_id, property_nm, property_id, unit_name, unit_id) + '/06_Media'
    else:
        base = prop_root + '/11_Media'
    safe = re.sub(r'[\\/:*?"<>|]+', '-', filename).strip() or 'file.bin'
    return f'{base}/{safe}'

def main(req: func.HttpRequest) -> func.HttpResponse:
    action = (req.route_params.get('action') or '').lower()
    try:
        body = req.get_json()
    except Exception:
        return func.HttpResponse('Invalid JSON', status_code=400)

    client = DropboxClient.from_env()

    if action == 'start':
        meta = body.get('meta') or {}
        filename = body.get('filename') or 'file.bin'
        first_b64 = body.get('first_chunk_base64') or ''
        try:
            first = base64.b64decode(first_b64) if first_b64 else b''
        except Exception:
            return func.HttpResponse('invalid first_chunk_base64', status_code=400)

        dest = _path(meta, filename)
        if first:
            session_id, offset = client.session_start(first)
        else:
            session_id, offset = client.session_start(b'')
        return func.HttpResponse(json.dumps({'ok': True, 'session_id': session_id, 'offset': offset, 'dest_path': dest}), mimetype='application/json')

    elif action == 'append':
        sid = body.get('session_id'); off = int(body.get('offset') or 0)
        try:
            chunk = base64.b64decode(body.get('chunk_base64') or '')
        except Exception:
            return func.HttpResponse('invalid chunk_base64', status_code=400)
        new_off = client.session_append(sid, off, chunk)
        return func.HttpResponse(json.dumps({'ok': True, 'offset': new_off}), mimetype='application/json')

    elif action == 'finish':
        sid = body.get('session_id'); off = int(body.get('offset') or 0); dest = body.get('dest_path')
        res = client.session_finish(sid, off, dest)
        return func.HttpResponse(json.dumps({'ok': True, 'path': getattr(res, 'path_display', None) or dest, 'rev': getattr(res, 'rev', None)}), mimetype='application/json')

    else:
        return func.HttpResponse('Unknown action. Use start|append|finish', status_code=400)
