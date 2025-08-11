import json, logging, azure.functions as func
from lib.pathmap import (
    owner_root, OWNER_SUBS,
    property_root, PROPERTY_SUBS,
    unit_root, UNIT_SUBS,
    lease_root, LEASE_SUBS,
    applicant_root, APPLICANT_SUBS,
    work_order_root
)
from lib.dropbox_client import DropboxClient

def _intval(v):
    try: return int(v)
    except: return v

def _p(body, k, d=None): 
    v = body.get(k, d)
    return v

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        payload = req.get_json()
    except ValueError:
        return func.HttpResponse("Invalid JSON", status_code=400)

    entity_type = payload.get("entity_type")
    data = payload.get("new", {})

    try:
        client = DropboxClient.from_env()
    except Exception as e:
        logging.exception("Dropbox client init failed")
        return func.HttpResponse("Server configuration error", status_code=500)

    created = []

    def mk(path, subs=None):
        client.ensure_folder(path)
        created.append(path)
        if subs:
            for s in subs:
                client.ensure_folder(f"{path}/{s}")
                created.append(f"{path}/{s}")

    if entity_type == "owner":
        base = owner_root(data.get("name"), _intval(data.get("id")))
        mk(base, OWNER_SUBS)

    elif entity_type == "property":
        base = property_root(data.get("owner_name"), _intval(data.get("owner_id")), data.get("name"), _intval(data.get("id")))
        mk(base, PROPERTY_SUBS)

    elif entity_type == "unit":
        base = unit_root(data.get("owner_name"), _intval(data.get("owner_id")), data.get("property_name"), _intval(data.get("property_id")), data.get("name"), _intval(data.get("id")))
        mk(base, UNIT_SUBS)

    elif entity_type == "lease":
        base = lease_root(data.get("owner_name"), _intval(data.get("owner_id")), data.get("property_name"), _intval(data.get("property_id")), _intval(data.get("id")))
        mk(base, LEASE_SUBS)

    elif entity_type == "applicant":
        base = applicant_root(data.get("owner_name"), _intval(data.get("owner_id")), data.get("property_name"), _intval(data.get("property_id")), data.get("name"), _intval(data.get("id")))
        mk(base, APPLICANT_SUBS)

    elif entity_type == "work_order":
        base = work_order_root(
            data.get("owner_name"), _intval(data.get("owner_id")),
            data.get("property_name"), _intval(data.get("property_id")),
            data.get("unit_name"), _intval(data.get("unit_id")), _intval(data.get("id"))
        )
        mk(base, ["Photos","Invoices","Docs"])

    else:
        return func.HttpResponse("unknown entity_type", status_code=400)

    return func.HttpResponse(json.dumps({"ok": True, "created": created}), mimetype="application/json")
