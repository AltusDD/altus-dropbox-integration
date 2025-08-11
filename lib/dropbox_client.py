
import os
import dropbox
from dropbox.exceptions import ApiError

APP_KEY = os.getenv("DROPBOX_APP_KEY")
APP_SECRET = os.getenv("DROPBOX_APP_SECRET")
REFRESH_TOKEN = os.getenv("DROPBOX_REFRESH_TOKEN")

def get_dbx() -> dropbox.Dropbox:
    if not (APP_KEY and APP_SECRET and REFRESH_TOKEN):
        raise RuntimeError("Missing Dropbox credentials in env settings.")
    return dropbox.Dropbox(oauth2_refresh_token=REFRESH_TOKEN, app_key=APP_KEY, app_secret=APP_SECRET)

def ensure_folder(path: str) -> None:
    dbx = get_dbx()
    try:
        dbx.files_get_metadata(path)
        return
    except ApiError:
        try:
            dbx.files_create_folder_v2(path, autorename=False)
        except ApiError:
            pass

def upload_bytes(folder: str, filename: str, data: bytes) -> dict:
    dbx = get_dbx()
    ensure_folder(folder)
    full_path = f"{folder}/{filename}"
    res = dbx.files_upload(data, full_path, mode=dropbox.files.WriteMode.add, mute=True, strict_conflict=False)
    return {
        "path_lower": res.path_lower,
        "content_hash": res.content_hash,
        "size": res.size,
        "rev": res.rev,
        "id": res.id,
        "name": res.name,
    }

def temp_link(full_path: str) -> str:
    dbx = get_dbx()
    link = dbx.files_get_temporary_link(full_path)
    return link.link
