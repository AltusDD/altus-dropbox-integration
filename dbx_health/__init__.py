import azure.functions as func, json
from lib.dropbox_client import ensure_folder

def main(req: func.HttpRequest):
    try:
        ensure_folder("/Altus_Empire_Command_Center")
        return func.HttpResponse(json.dumps({"ok": True}), mimetype="application/json")
    except Exception as e:
        return func.HttpResponse(json.dumps({"ok": False, "error": str(e)}), status_code=500, mimetype="application/json")
