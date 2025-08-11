from __future__ import annotations
import os, json, time, math
import httpx

APP_KEY = os.getenv("DROPBOX_APP_KEY", "")
APP_SECRET = os.getenv("DROPBOX_APP_SECRET", "")
REFRESH_TOKEN = os.getenv("DROPBOX_REFRESH_TOKEN", "")
CHUNK = 100 * 1024 * 1024

def _refresh_access_token() -> dict:
    if not (APP_KEY and APP_SECRET and REFRESH_TOKEN):
        raise RuntimeError("Missing Dropbox credentials")
    with httpx.Client(timeout=15) as c:
        r = c.post("https://api.dropboxapi.com/oauth2/token",
                   data={"grant_type":"refresh_token","refresh_token":REFRESH_TOKEN},
                   auth=(APP_KEY, APP_SECRET))
        r.raise_for_status()
        tok = r.json()
        tok["obtained_at"] = int(time.time())
        return tok

_cached = None
def _headers(extra=None):
    global _cached
    if not _cached or (time.time() - _cached.get("obtained_at",0)) > 3*3600+900:
        _cached = _refresh_access_token()
    h = {"Authorization": f"Bearer {_cached['access_token']}"}
    if extra: h.update(extra)
    return h

def ensure_folder(path: str) -> None:
    args = {"path": path, "autorename": False}
    with httpx.Client(timeout=20) as c:
        r = c.post("https://api.dropboxapi.com/2/files/create_folder_v2",
                   headers=_headers({"Content-Type":"application/json"}),
                   content=json.dumps(args))
        # 200 OK or 409 (already exists) are fine
        if r.status_code not in (200,409):
            r.raise_for_status()

def upload(path: str, filename: str, content: bytes) -> dict:
    full = f"{path.rstrip('/')}/{filename}"
    if len(content) <= CHUNK:
        return _upload_simple(full, content)
    return _upload_chunked(full, content)

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
        first = content[:CHUNK]
        r = c.post("https://content.dropboxapi.com/2/files/upload_session/start",
                   headers=_headers({"Dropbox-API-Arg": json.dumps({"close": False}),
                                     "Content-Type":"application/octet-stream"}),
                   content=first)
        r.raise_for_status()
        session_id = r.json()["session_id"]
        offset = len(first)
        while offset < len(content):
            chunk = content[offset: offset+CHUNK]
            r = c.post("https://content.dropboxapi.com/2/files/upload_session/append_v2",
                       headers=_headers({"Dropbox-API-Arg": json.dumps({"cursor":{"session_id":session_id,"offset":offset}}),
                                         "Content-Type": "application/octet-stream"}),
                       content=chunk)
            r.raise_for_status()
            offset += len(chunk)
        r = c.post("https://content.dropboxapi.com/2/files/upload_session/finish",
                   headers=_headers({"Dropbox-API-Arg": json.dumps({"cursor":{"session_id":session_id,"offset":offset},"commit":{"path": full_path, "mode":"overwrite"}}),
                                     "Content-Type": "application/octet-stream"}),
                   content=b"")
        r.raise_for_status()
        return r.json()

def get_temp_link(full_path: str) -> str:
    with httpx.Client(timeout=15) as c:
        r = c.post("https://api.dropboxapi.com/2/files/get_temporary_link",
                   headers=_headers({"Content-Type":"application/json"}),
                   content=json.dumps({"path": full_path}))
        r.raise_for_status()
        return r.json()["link"]
