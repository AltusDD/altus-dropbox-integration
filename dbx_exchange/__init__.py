import os, json
import azure.functions as func
import httpx

REDIRECT_URI = "https://localhost"  # must match your Dropbox app setting

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Accept 'dbx_code' via querystring or JSON; avoid clashing with Azure 'code' (function key)
    dbx_code = req.params.get("dbx_code")
    if not dbx_code:
        try:
            body = req.get_json()
            dbx_code = (body or {}).get("dbx_code") or (body or {}).get("code")
        except Exception:
            dbx_code = None

    app_key = os.getenv("DROPBOX_APP_KEY", "")
    app_secret = os.getenv("DROPBOX_APP_SECRET", "")

    if not dbx_code:
        return func.HttpResponse("Provide Dropbox auth code via ?dbx_code=... or JSON {"dbx_code":"..."}", status_code=400)
    if not app_key or not app_secret:
        return func.HttpResponse("App settings DROPBOX_APP_KEY / DROPBOX_APP_SECRET are missing.", status_code=500)

    try:
        with httpx.Client(timeout=20) as c:
            r = c.post(
                "https://api.dropboxapi.com/oauth2/token",
                data={"code": dbx_code, "grant_type": "authorization_code", "redirect_uri": REDIRECT_URI},
                auth=(app_key, app_secret),
            )
            r.raise_for_status()
            data = r.json()
            out = {
                "ok": True,
                "refresh_token": data.get("refresh_token"),
                "token_type": data.get("token_type"),
                "expires_in": data.get("expires_in"),
                "note": "Copy 'refresh_token' into Azure App Setting DROPBOX_REFRESH_TOKEN, then Save + Restart. You can delete this function after."
            }
            return func.HttpResponse(json.dumps(out, indent=2), mimetype="application/json")
    except httpx.HTTPStatusError as e:
        return func.HttpResponse(f"Token exchange failed: {e.response.status_code} {e.response.text}", status_code=400)
    except Exception as e:
        return func.HttpResponse(f"Token exchange failed: {str(e)}", status_code=400)
