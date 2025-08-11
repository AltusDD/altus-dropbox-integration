
import json
import azure.functions as func
from lib.dropbox_client import get_dbx

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        dbx = get_dbx()
        acct = dbx.users_get_current_account()
        return func.HttpResponse(json.dumps({"ok": True, "account_email": acct.email}), mimetype="application/json")
    except Exception as ex:
        return func.HttpResponse(json.dumps({"ok": False, "error": str(ex)}), mimetype="application/json", status_code=500)
