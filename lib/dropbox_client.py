from __future__ import annotations
import os, json, time, math, logging
import httpx

# ---- Config from environment ----
APP_KEY = os.getenv("DROPBOX_APP_KEY", "")
APP_SECRET = os.getenv("DROPBOX_APP_SECRET", "")
REFRESH_TOKEN = os.getenv("DROPBOX_REFRESH_TOKEN", "")

# 100 MB chunks; Dropbox upload session supports up to 150MB per call
CHUNK = 100 * 1024 * 1024

class DropboxError(RuntimeError):
    pass

def _token_cache_path() -> str:
    # ephemeral cache path inside the function filesystem
    return "/tmp/dbx_token.json"

def _save_token(token: dict) -> None:
    try:
        with open(_token_cache_path(), "w") as f:
            json.dump(token, f)
    except Exception:
        pass

def _load_token() -> dict | None:
    try:
        with open(_token_cache_path(), "r") as f:
            return json.load(f)
    except Exception:
        return None

def _refresh_access_token() -> dict:
    if not (APP_KEY and APP_SECRET and REFRESH_TOKEN):
        raise DropboxError("Missing Dropbox credentials in App Settings.")
    data = {
        "grant_type": "refresh_token",
        "refresh_token": REFRESH_TOKEN,
    }
    # Basic auth header via httpx auth
    auth = (APP_KEY, APP_SECRET)
    with httpx.Client(timeout=15) as c:
        r = c.post("https://api.dropboxapi.com/oauth2/token", data=data, auth=auth)
        r.raise_for_status()
        token = r.json()
        token["obtained_at"] = int(time.time())
        _save_token(token)
        return token

def _get_access_token() -> str:
    # try cache, refresh if missing or close to expiry
    tok = _load_token()
    if not tok:
        tok = _refresh_access_token()
    # Dropbox tokens typically last 4 hours; refresh if older than ~3.5h
    if int(time.time()) - int(tok.get("obtained_at", 0)) > 3 * 3600 + 1800:
        tok = _refresh_access_token()
    return tok["access_token"]

def _headers(extra: dict | None = None) -> dict:
    h = {"Authorization": f"Bearer {_get_access_token()}"}
    if extra:
        h.update(extra)
    return h

def ensure_folder(path: str) -> None:
    """Create folder if not exists (idempotent)."""
    args = {"path": path, "autorename": False}
    with httpx.Client(timeout=20) as c:
        r = c.post("https://api.dropboxapi.com/2/files/create_folder_v2",
                   headers=_headers({"Content-Type": "application/json"}),
                   content=json.dumps(args))
        if r.status_code in (200, 409):
            # 409 path/conflict if already exists
            return
        r.raise_for_status()

def upload(path: str, filename: str, content: bytes) -> dict:
    """Upload a file under a folder path. Returns Dropbox file metadata dict."""
    full_path = f"{path.rstrip('/')}/{filename}"
    if len(content) <= CHUNK:
        return _upload_simple(full_path, content)
    else:
        return _upload_chunked(full_path, content)

def _upload_simple(full_path: str, content: bytes) -> dict:
    with httpx.Client(timeout=None) as c:
        r = c.post("https://content.dropboxapi.com/2/files/upload",
                   headers=_headers({
                       "Dropbox-API-Arg": json.dumps({"path": full_path, "mode": "overwrite"}),
                       "Content-Type": "application/octet-stream"
                   }),
                   content=content)
        r.raise_for_status()
        return r.json()

def _upload_chunked(full_path: str, content: bytes) -> dict:
    with httpx.Client(timeout=None) as c:
        # start
        first = content[:CHUNK]
        r = c.post("https://content.dropboxapi.com/2/files/upload_session/start",
                   headers=_headers({"Dropbox-API-Arg": json.dumps({"close": False}),
                                     "Content-Type": "application/octet-stream"}),
                   content=first)
        r.raise_for_status()
        session_id = r.json()["session_id"]
        offset = len(first)

        # append
        while offset < len(content):
            chunk = content[offset: offset + CHUNK]
            r = c.post("https://content.dropboxapi.com/2/files/upload_session/append_v2",
                       headers=_headers({
                           "Dropbox-API-Arg": json.dumps({"cursor": {"session_id": session_id, "offset": offset}, "close": False}),
                           "Content-Type": "application/octet-stream"
                       }),
                       content=chunk)
            r.raise_for_status()
            offset += len(chunk)

        # finish
        r = c.post("https://content.dropboxapi.com/2/files/upload_session/finish",
                   headers=_headers({
                       "Dropbox-API-Arg": json.dumps({"cursor": {"session_id": session_id, "offset": offset},
                                                       "commit": {"path": full_path, "mode": "overwrite"}}),
                       "Content-Type": "application/octet-stream"
                   }),
                   content=b"")
        r.raise_for_status()
        return r.json()

def get_temp_link(path: str) -> str:
    args = {"path": path}
    with httpx.Client(timeout=15) as c:
        r = c.post("https://api.dropboxapi.com/2/files/get_temporary_link",
                   headers=_headers({"Content-Type": "application/json"}),
                   content=json.dumps(args))
        r.raise_for_status()
        return r.json()["link"]
