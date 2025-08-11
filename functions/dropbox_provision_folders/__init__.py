import azure.functions as func
import json
from lib.pathmap import property_root, unit_root, lease_root
from lib.dropbox_client import ensure_folder

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        body = req.get_json()
        entity_type = body.get("entity_type")
        data = body.get("new") or {}
        created = []

        if entity_type == "property":
            base = property_root(data["name"], int(data["id"]))
            for sub in ["01_Units", "02_Leases", "03_Photos", "04_Inspections", "05_Work_Orders", "06_Legal", "07_Financials", "08_Acquisition_Docs"]:
                ensure_folder(f"{base}/{sub}")
                created.append(f"{base}/{sub}")
        elif entity_type == "unit":
            base = unit_root(data["property_name"], int(data["property_id"]), data["name"], int(data["id"]))
            for sub in ["01_Photos", "02_Inspections"]:
                ensure_folder(f"{base}/{sub}")
                created.append(f"{base}/{sub}")
        elif entity_type == "lease":
            base = f"/Altus_Empire_Command_Center/02_Leases/{int(data['id'])}"
            for sub in ["Signed_Lease_Agreement", "Amendments", "Tenant_Correspondence"]:
                ensure_folder(f"{base}/{sub}")
                created.append(f"{base}/{sub}")
        else:
            return func.HttpResponse("unknown entity_type", status_code=400)

        return func.HttpResponse(json.dumps({"ok": True, "created": created}), mimetype="application/json")
    except Exception as e:
        return func.HttpResponse(str(e), status_code=400)
