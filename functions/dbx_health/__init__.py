import azure.functions as func
import json
from lib.dropbox_client import get_temp_link, ensure_folder

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # hit a cheap endpoint: ensure root exists and return ok
        ensure_folder("/Altus_Empire_Command_Center")
        return func.HttpResponse(json.dumps({"ok": True}), mimetype="application/json")
    except Exception as e:
        return func.HttpResponse(json.dumps({"ok": False, "error": str(e)}), status_code=500, mimetype="application/json")
