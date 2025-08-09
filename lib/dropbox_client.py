from __future__ import annotations
import os, time
import dropbox
from dropbox.exceptions import ApiError, AuthError, RateLimitError
from dropbox.files import WriteMode

DROPBOX_APP_KEY = os.environ["DROPBOX_APP_KEY"]
DROPBOX_APP_SECRET = os.environ["DROPBOX_APP_SECRET"]
DROPBOX_REFRESH_TOKEN = os.environ["DROPBOX_REFRESH_TOKEN"]

def _new_dbx() -> dropbox.Dropbox:
    return dropbox.Dropbox(
        oauth2_refresh_token=DROPBOX_REFRESH_TOKEN,
        app_key=DROPBOX_APP_KEY,
        app_secret=DROPBOX_APP_SECRET,
        timeout=60,
    )

def with_client(fn):
    def wrapper(*args, **kwargs):
        for attempt in range(5):
            try:
                dbx = _new_dbx()
                return fn(dbx, *args, **kwargs)
            except RateLimitError as e:
                ra = getattr(e, "retry_after", None)
                time.sleep(ra or min(2**attempt, 30))
            except AuthError:
                raise
            except ApiError:
                raise
        raise RuntimeError("Dropbox operation failed after retries.")
    return wrapper

@with_client
def ensure_folder_tree(dbx, *paths: str):
    for p in paths:
        if not p.startswith("/"):
            p = "/" + p
        try:
            dbx.files_create_folder_v2(p)
        except ApiError as e:
            if not (e.error.is_path() and e.error.get_path().is_conflict()):
                raise

@with_client
def upload_file(dbx, path: str, data: bytes, mode: WriteMode = WriteMode("add")):
    if not path.startswith("/"):
        path = "/" + path
    res = dbx.files_upload(data, path, mode=mode, mute=True)
    return {
        "path_lower": res.path_lower,
        "id": res.id,
        "rev": res.rev,
        "size": res.size,
        "content_hash": res.content_hash,
    }

@with_client
def get_temp_link(dbx, path: str) -> str:
    if not path.startswith("/"):
        path = "/" + path
    link = dbx.files_get_temporary_link(path)
    return link.link
