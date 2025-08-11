import os, json
import azure.functions as func
import httpx

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Body: {"code":"<auth_code_from_dropbox>"}
    try:
        body = req.get_json()
    except Exception:
        return func.HttpResponse("Send JSON body like {\"code\":\"...\"}", status_code=400)

    code = body.get("code")
    app_key = os.getenv("DROPBOX_APP_KEY", "")
    app_secret = os.getenv("DROPBOX_APP_SECRET", "")
    if not code:
        return func.HttpResponse("Missing 'code' in JSON body.", status_code=400)
    if not app_key or not app_secret:
        return func.HttpResponse("App settings DROPBOX_APP_KEY / DROPBOX_APP_SECRET are missing.", status_code=500)

    try:
        with httpx.Client(timeout=20) as c:
            r = c.post("https://api.dropboxapi.com/oauth2/token",
                       data={"code": code, "grant_type": "authorization_code"},
                       auth=(app_key, app_secret))
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
    except httpx.HTTPError as e:
        return func.HttpResponse(f"Token exchange failed: {str(e)}", status_code=400)
