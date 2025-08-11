import azure.functions as func, json
from lib.pathmap import property_root, unit_root
from lib.dropbox_client import ensure_folder

def main(req: func.HttpRequest):
    body = req.get_json()
    t = body.get("entity_type")
    data = body.get("new") or {}
    created = []
    if t == "property":
        base = property_root(data["name"], int(data["id"]))
        subs = ["01_Units","02_Leases","03_Photos","04_Inspections","05_Work_Orders","06_Legal","07_Financials","08_Acquisition_Docs"]
        for s in subs:
            p = f"{base}/{s}"; ensure_folder(p); created.append(p)
    elif t == "unit":
        base = unit_root(data["property_name"], int(data["property_id"]), data["name"], int(data["id"]))
        for s in ["01_Photos","02_Inspections"]:
            p = f"{base}/{s}"; ensure_folder(p); created.append(p)
    elif t == "lease":
        base = f"/Altus_Empire_Command_Center/02_Leases/{int(data['id'])}"
        for s in ["Signed_Lease_Agreement","Amendments","Tenant_Correspondence"]:
            p = f"{base}/{s}"; ensure_folder(p); created.append(p)
    else:
        return func.HttpResponse("unknown entity_type", status_code=400)
    return func.HttpResponse(json.dumps({"ok": True, "created": created}), mimetype="application/json")
