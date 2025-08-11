import os, json, httpx, math, logging
from typing import List

DBX_API = "https://api.dropboxapi.com/2"
DBX_CONTENT = "https://content.dropboxapi.com/2"

CHUNK = 100 * 1024 * 1024  # 100MB

class DropboxClient:
    def __init__(self, access_token: str):
        self.access_token = access_token

    @classmethod
    def from_env(cls):
        key = os.getenv("DROPBOX_APP_KEY")
        sec = os.getenv("DROPBOX_APP_SECRET")
        ref = os.getenv("DROPBOX_REFRESH_TOKEN")
        if not (key and sec and ref):
            raise RuntimeError("Missing DROPBOX_* settings")
        with httpx.Client(timeout=20) as c:
            r = c.post(
                "https://api.dropboxapi.com/oauth2/token",
                data={"grant_type": "refresh_token", "refresh_token": ref},
                auth=(key, sec),
            )
            r.raise_for_status()
            tok = r.json()["access_token"]
        return cls(tok)

    def _h(self):
        return {"Authorization": f"Bearer {self.access_token}"}

    def _h_json(self):
        return {**self._h(), "Content-Type": "application/json"}

    def ensure_folder(self, path: str):
        # Create each segment if needed, ignoring "already exists" errors
        parts = [p for p in path.split("/") if p]
        cur = ""
        for p in parts:
            cur += "/" + p
            try:
                self._create_folder(cur)
            except httpx.HTTPStatusError as e:
                # 409 path/conflict/folder should be ignored
                if e.response.status_code != 409:
                    raise

    def _create_folder(self, path: str):
        with httpx.Client(timeout=20) as c:
            r = c.post(f"{DBX_API}/files/create_folder_v2", headers=self._h_json(), json={"path": path, "autorename": False})
            if r.status_code not in (200, 409):
                r.raise_for_status()

    def temp_link(self, path: str) -> str:
        with httpx.Client(timeout=20) as c:
            r = c.post(f"{DBX_API}/files/get_temporary_link", headers=self._h_json(), json={"path": path})
            r.raise_for_status()
            return r.json()["link"]

    def upload(self, path: str, content: bytes):
        if len(content) <= CHUNK:
            return self._upload_simple(path, content)
        else:
            return self._upload_chunked(path, content)

    def _upload_simple(self, path: str, content: bytes):
        arg = json.dumps({"path": path, "mode": "overwrite", "mute": True, "autorename": False})
        with httpx.Client(timeout=None) as c:
            r = c.post(f"{DBX_CONTENT}/files/upload", headers={**self._h(), "Dropbox-API-Arg": arg, "Content-Type": "application/octet-stream"}, content=content)
            r.raise_for_status()
            return r.json()

    def _upload_chunked(self, path: str, content: bytes):
        # start
        first = content[:CHUNK]
        with httpx.Client(timeout=None) as c:
            r0 = c.post(f"{DBX_CONTENT}/files/upload_session/start", headers={**self._h(), "Dropbox-API-Arg": json.dumps({"close": False}), "Content-Type": "application/octet-stream"}, content=first)
            r0.raise_for_status()
            session_id = r0.json()["session_id"]
            offset = len(first)

            # append
            while offset < len(content):
                chunk = content[offset: offset + CHUNK]
                arg = {"cursor": {"session_id": session_id, "offset": offset}, "close": False}
                rA = c.post(f"{DBX_CONTENT}/files/upload_session/append_v2", headers={**self._h(), "Dropbox-API-Arg": json.dumps(arg), "Content-Type": "application/octet-stream"}, content=chunk)
                rA.raise_for_status()
                offset += len(chunk)

            # finish
            argF = {"cursor": {"session_id": session_id, "offset": offset}, "commit": {"path": path, "mode": "overwrite", "mute": True}}
            rF = c.post(f"{DBX_CONTENT}/files/upload_session/finish", headers={**self._h(), "Dropbox-API-Arg": json.dumps(argF), "Content-Type": "application/octet-stream"})
            rF.raise_for_status()
            return rF.json()
