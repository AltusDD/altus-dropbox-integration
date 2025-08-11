import os, json
import azure.functions as func
import httpx

def main(req: func.HttpRequest) -> func.HttpResponse:
    code = req.params.get("code")
    if not code:
        return func.HttpResponse("Missing 'code' from Dropbox in query string.", status_code=400)

    app_key = os.getenv("DROPBOX_APP_KEY","")
    app_secret = os.getenv("DROPBOX_APP_SECRET","")
    if not app_key or not app_secret:
        return func.HttpResponse("App settings DROPBOX_APP_KEY / DROPBOX_APP_SECRET are missing.", status_code=500)

    host = os.getenv("WEBSITE_HOSTNAME","")
    redirect_uri = f"https://{host}/api/dbx/callback"

    try:
        with httpx.Client(timeout=20) as c:
            r = c.post("https://api.dropboxapi.com/oauth2/token",
                       data={"code": code, "grant_type":"authorization_code", "redirect_uri": redirect_uri},
                       auth=(app_key, app_secret))
            r.raise_for_status()
            data = r.json()
            refresh = data.get("refresh_token")
            if not refresh:
                return func.HttpResponse(f"Token exchange returned no refresh_token: {json.dumps(data)[:400]}", status_code=400)
            html = f"""
            <html><body style='font-family:system-ui;margin:40px'>
              <h2>Dropbox connected</h2>
              <p>Copy your <b>refresh_token</b> and paste it into Azure:</p>
              <pre style='background:#f5f5f7;padding:12px;border-radius:8px'>{refresh}</pre>
              <ol>
                <li>Azure -> Function App -> <b>Configuration</b> -> <b>Application settings</b></li>
                <li>Add or update <code>DROPBOX_REFRESH_TOKEN</code> to the value above</li>
                <li>Click <b>Save</b>, then <b>Restart</b> the Function App</li>
              </ol>
              <p>When done, run your tracer: <code>/api/trace?code=&lt;default key&gt;</code>. You should see <b>dropbox.ok: true</b>.</p>
            </body></html>
            """
            return func.HttpResponse(html, mimetype="text/html")
    except httpx.HTTPStatusError as e:
        return func.HttpResponse(f"Token exchange failed: {e.response.status_code} {e.response.text}", status_code=400)
    except Exception as e:
        return func.HttpResponse(f"Token exchange failed: {str(e)}", status_code=400)
