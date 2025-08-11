# lib/dropbox_client.py
import os
import httpx
import dropbox

class DropboxClient:
    def __init__(self, dbx: dropbox.Dropbox):
        self.dbx = dbx

    @classmethod
    def from_env(cls) -> "DropboxClient":
        app_key = os.getenv("DROPBOX_APP_KEY")
        app_secret = os.getenv("DROPBOX_APP_SECRET")
        refresh = os.getenv("DROPBOX_REFRESH_TOKEN")
        if not (app_key and app_secret and refresh):
            raise RuntimeError("Missing Dropbox env settings")

        with httpx.Client(timeout=20) as c:
            r = c.post(
                "https://api.dropboxapi.com/oauth2/token",
                data={"grant_type": "refresh_token", "refresh_token": refresh},
                auth=(app_key, app_secret),
            )
            r.raise_for_status()
            token = r.json()["access_token"]

        dbx = dropbox.Dropbox(token)  # short-lived access token
        return cls(dbx)
