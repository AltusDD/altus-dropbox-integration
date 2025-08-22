import json
import azure.functions as func
from lib.dropbox_client import ensure_folder

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Example: make sure base folder for the app exists in Dropbox
        result = ensure_folder("/Altus_Empire_Command_Center")
        return func.HttpResponse(
            json.dumps({"ok": True, "result": result}),
            mimetype="application/json",
            status_code=200,
        )
    except Exception as e:
        return func.HttpResponse(
            json.dumps({"ok": False, "error": str(e)}),
            mimetype="application/json",
            status_code=500,
        )
