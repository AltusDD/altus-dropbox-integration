import os
import dropbox
from dropbox.exceptions import ApiError

# Pull creds from App Settings (Configuration > Application settings)
APP_KEY = os.environ.get("DROPBOX_APP_KEY")
APP_SECRET = os.environ.get("DROPBOX_APP_SECRET")
REFRESH_TOKEN = os.environ.get("DROPBOX_REFRESH_TOKEN")

def get_dbx() -> dropbox.Dropbox:
    """
    Returns an authenticated Dropbox client using refresh-token flow.
    """
    if not (APP_KEY and APP_SECRET and REFRESH_TOKEN):
        raise RuntimeError("Missing Dropbox env vars: DROPBOX_APP_KEY/SECRET/REFRESH_TOKEN")
    return dropbox.Dropbox(
        app_key=APP_KEY,
        app_secret=APP_SECRET,
        oauth2_refresh_token=REFRESH_TOKEN,
        timeout=30,
    )

def _normalize_path(path: str) -> str:
    if not path:
        return "/"
    path = path.strip()
    if not path.startswith("/"):
        path = "/" + path
    return path

def ensure_folder(path: str) -> dict:
    """
    Ensure a folder exists at `path`. If it doesn't, create it.
    Returns a small dict with the resulting path.
    """
    dbx = get_dbx()
    target = _normalize_path(path)

    try:
        dbx.files_get_metadata(target)
        # Folder exists
        return {"ok": True, "path": target, "created": False}
    except ApiError as e:
        # If it doesn't exist, create it
        if (hasattr(e, "error") and hasattr(e.error, "is_path") and e.error.is_path()):
            dbx.files_create_folder_v2(target, autorename=False)
            return {"ok": True, "path": target, "created": True}
        # Different API error – surface it
        raise
