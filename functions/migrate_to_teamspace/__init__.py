
import os, json, httpx, base64
import azure.functions as func
import dropbox
from lib.dropbox_client import DropboxClient

class TeamDropboxClient(DropboxClient):
    @classmethod
    def from_env(cls):
        key = os.getenv('TEAM_DROPBOX_APP_KEY')
        sec = os.getenv('TEAM_DROPBOX_APP_SECRET')
        ref = os.getenv('TEAM_DROPBOX_REFRESH_TOKEN')
        if not (key and sec and ref):
            raise RuntimeError('Missing TEAM_DROPBOX_* envs')
        return cls(key, sec, ref)

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_SERVICE_ROLE_KEY')

def _hdrs():
    return {'apikey': SUPABASE_KEY, 'Authorization': f'Bearer {SUPABASE_KEY}'}

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        body = req.get_json()
    except Exception:
        body = {}

    limit = int(body.get('limit') or 50)
    start_after_id = body.get('start_after_id')

    src = DropboxClient.from_env().dbx
    dst = TeamDropboxClient.from_env().dbx

    migrated = 0
    last_id = None

    with httpx.Client(timeout=60) as c:
        params = {'select':'id, dropbox_path, original_name', 'order':'id.asc', 'limit':str(limit)}
        if start_after_id:
            params['id'] = f'gt.{start_after_id}'

        r = c.get(f'{SUPABASE_URL}/rest/v1/file_assets', headers=_hdrs(), params=params)
        if r.status_code != 200:
            return func.HttpResponse(f'Supabase error: {r.status_code} {r.text}', status_code=500)
        rows = r.json()

        for row in rows:
            last_id = row['id']
            path = row['dropbox_path']
            try:
                tl = src.files_get_temporary_link(path).link
                data = c.get(tl).content
                folder = path.rsplit('/',1)[0]
                try:
                    dst.files_create_folder_v2(folder, autorename=False)
                except dropbox.exceptions.ApiError as e:
                    if 'conflict' not in str(e).lower():
                        raise
                dst.files_upload(data, path, mode=dropbox.files.WriteMode('add'), autorename=True, mute=True)
                migrated += 1
            except Exception as e:
                # skip failures but continue
                pass

    return func.HttpResponse(json.dumps({'ok': True, 'migrated_count': migrated, 'last_id': last_id}), mimetype='application/json')
