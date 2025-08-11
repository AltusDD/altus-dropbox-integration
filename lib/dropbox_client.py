# lib/dropbox_client.py (empire-grade)
import os, dropbox

class DropboxClient:
    # Wrapper using OAuth2 refresh for short-lived tokens automatically
    def __init__(self, app_key: str, app_secret: str, refresh_token: str):
        self.dbx = dropbox.Dropbox(
            oauth2_refresh_token=refresh_token,
            app_key=app_key,
            app_secret=app_secret,
            timeout=60
        )

    @classmethod
    def from_env(cls):
        key = os.getenv('DROPBOX_APP_KEY')
        sec = os.getenv('DROPBOX_APP_SECRET')
        ref = os.getenv('DROPBOX_REFRESH_TOKEN')
        if not (key and sec and ref):
            raise RuntimeError('Missing DROPBOX_* envs')
        return cls(key, sec, ref)

    def create_folder_if_not_exists(self, path: str):
        try:
            self.dbx.files_create_folder_v2(path, autorename=False)
        except dropbox.exceptions.ApiError as e:
            if 'conflict' in str(e).lower():
                return
            raise

    def upload_bytes(self, dest_path: str, data: bytes):
        return self.dbx.files_upload(data, dest_path, mode=dropbox.files.WriteMode('add'), autorename=True, mute=True)

    def session_start(self, first_chunk: bytes):
        res = self.dbx.files_upload_session_start(first_chunk)
        return res.session_id, len(first_chunk)

    def session_append(self, session_id: str, offset: int, chunk: bytes):
        cursor = dropbox.files.UploadSessionCursor(session_id=session_id, offset=offset)
        self.dbx.files_upload_session_append_v2(chunk, cursor)
        return offset + len(chunk)

    def session_finish(self, session_id: str, offset: int, dest_path: str):
        cursor = dropbox.files.UploadSessionCursor(session_id=session_id, offset=offset)
        commit = dropbox.files.CommitInfo(path=dest_path, mode=dropbox.files.WriteMode.overwrite)
        return self.dbx.files_upload_session_finish(b'', cursor, commit)
