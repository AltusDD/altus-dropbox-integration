import os, urllib.parse
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    app_key = os.getenv("DROPBOX_APP_KEY")
    if not app_key:
        return func.HttpResponse("App setting DROPBOX_APP_KEY is missing.", status_code=500)
    host = os.getenv("WEBSITE_HOSTNAME","")
    redirect_uri = f"https://{host}/api/dbx/callback"
    params = {
        "client_id": app_key,
        "response_type": "code",
        "token_access_type": "offline",
        "redirect_uri": redirect_uri
    }
    url = "https://www.dropbox.com/oauth2/authorize?" + urllib.parse.urlencode(params)
    html = f"""
    <html><body style='font-family:system-ui;margin:40px'>
      <h2>Connect Dropbox (Altus)</h2>
      <p>Click the button below, approve Dropbox, and you will be sent back here. We will show your <b>refresh_token</b>.</p>
      <p><a href='{url}' style='background:#0b5fff;color:#fff;padding:12px 18px;border-radius:8px;text-decoration:none;'>Continue to Dropbox</a></p>
      <p style='color:#666'>Redirect URI in use: <code>{redirect_uri}</code></p>
    </body></html>"""
    return func.HttpResponse(html, mimetype="text/html")
