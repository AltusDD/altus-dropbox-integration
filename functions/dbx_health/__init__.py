import os, json, httpx, azure.functions as func

def _mask(s: str):
    if not s: return None
    s = str(s)
    if len(s) <= 6: return "*"*len(s)
    return s[:3] + "*"*(len(s)-6) + s[-3:]

def _check_dropbox():
    key = os.getenv("DROPBOX_APP_KEY"); sec = os.getenv("DROPBOX_APP_SECRET"); ref = os.getenv("DROPBOX_REFRESH_TOKEN")
    if not (key and sec and ref):
        return {"ok": False, "error": "Missing DROPBOX_* envs"}
    try:
        with httpx.Client(timeout=20) as c:
            r = c.post("https://api.dropboxapi.com/oauth2/token", data={"grant_type": "refresh_token","refresh_token": ref}, auth=(key, sec))
            r.raise_for_status()
            tok = r.json()["access_token"]
            r2 = c.post("https://api.dropboxapi.com/2/users/get_current_account", headers={"Authorization": f"Bearer {tok}"})
            r2.raise_for_status()
            return {"ok": True, "account_email": r2.json().get("email")}
    except Exception as e:
        return {"ok": False, "error": str(e)}

def _check_supabase():
    url = os.getenv("SUPABASE_URL"); key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
    if not (url and key):
        return {"ok": False, "error": "Missing SUPABASE_* envs"}
    headers = {"apikey": key, "Authorization": f"Bearer {key}"}
    try:
        with httpx.Client(timeout=20) as c:
            r = c.get(f"{url}/rest/v1/file_assets", headers=headers, params={"select":"id","limit":"1"})
            if r.status_code == 200:
                body = r.json()
                return {"ok": True, "table":"file_assets", "row_example": body[0] if body else None}
            return {"ok": False, "status": r.status_code, "body": r.text[:200]}
    except Exception as e:
        return {"ok": False, "error": str(e)}

def main(req: func.HttpRequest) -> func.HttpResponse:
    present = {n: bool(os.getenv(n)) for n in ["DROPBOX_APP_KEY","DROPBOX_APP_SECRET","DROPBOX_REFRESH_TOKEN","SUPABASE_URL","SUPABASE_SERVICE_ROLE_KEY"]}
    masked  = {n: _mask(os.getenv(n,"")) for n in ["DROPBOX_APP_KEY","DROPBOX_APP_SECRET","DROPBOX_REFRESH_TOKEN","SUPABASE_URL","SUPABASE_SERVICE_ROLE_KEY"]}
    dropbox = _check_dropbox()
    supabase = _check_supabase()
    greens = []; reds = []
    if all(present.values()): greens.append("All required env vars present")
    else: reds.append("Missing envs")
    greens.append(f"Dropbox OK ({dropbox.get('account_email')})" if dropbox.get("ok") else "Dropbox failed")
    greens.append("Supabase REST OK (file_assets reachable)" if supabase.get("ok") else "Supabase failed")
    ok = dropbox.get("ok") and supabase.get("ok")
    payload = {"ok": ok, "checks":{"env_present": present, "env_masked_preview": masked, "dropbox": dropbox, "supabase": supabase}, "summary":{"greens":greens,"reds":reds}}
    return func.HttpResponse(json.dumps(payload, indent=2), mimetype="application/json")
