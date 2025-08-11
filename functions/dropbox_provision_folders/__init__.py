import json
import azure.functions as func
from lib.pathmap import (
    owner_root, property_root, unit_root, lease_root, applicant_root,
    PROPERTY_CONTAINERS, UNIT_SUBS, LEASE_SUBS, APPLICANT_SUBS,
    property_work_order_root, unit_turnover_work_order_root, WORK_ORDER_SUBS
)
from lib.dropbox_client import ensure_folder  # already in your repo

def _i(v):  # safe int cast
    try:
        return int(v)
    except Exception:
        return v

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        body = req.get_json()
    except Exception:
        return func.HttpResponse("Send JSON body", status_code=400)

    et = (body.get("entity_type") or "").lower()
    data = body.get("new") or {}
    created = []

    def add(path):
        ensure_folder(path); created.append(path)

    if et == "owner":
        base = owner_root(data.get("name"), _i(data.get("id")))
        add(base)

    elif et == "property":
        base = property_root(data.get("owner_name"), _i(data.get("owner_id")),
                             data.get("name"), _i(data.get("id")))
        add(base)
        for c in PROPERTY_CONTAINERS:
            add(f"{base}/{c}")

    elif et == "unit":
        base = unit_root(data.get("owner_name"), _i(data.get("owner_id")),
                         data.get("property_name"), _i(data.get("property_id")),
                         data.get("name"), _i(data.get("id")))
        add(base)
        for s in UNIT_SUBS:
            add(f"{base}/{s}")

    elif et == "lease":
        base = lease_root(data.get("owner_name"), _i(data.get("owner_id")),
                          data.get("property_name"), _i(data.get("property_id")),
                          _i(data.get("id")))
        add(base)
        for s in LEASE_SUBS:
            add(f"{base}/{s}")

    elif et == "applicant":
        base = applicant_root(data.get("owner_name"), _i(data.get("owner_id")),
                              data.get("property_name"), _i(data.get("property_id")),
                              _i(data.get("id")), data.get("name"))
        add(base)
        for s in APPLICANT_SUBS:
            add(f"{base}/{s}")

    elif et == "work_order":
        # If unit info present, nest under Unit → Turnover; else under Property
        if data.get("unit_id"):
            base = unit_turnover_work_order_root(
                data.get("owner_name"), _i(data.get("owner_id")),
                data.get("property_name"), _i(data.get("property_id")),
                data.get("unit_name"), _i(data.get("unit_id")),
                _i(data.get("id"))
            )
        else:
            base = property_work_order_root(
                data.get("owner_name"), _i(data.get("owner_id")),
                data.get("property_name"), _i(data.get("property_id")),
                _i(data.get("id"))
            )
        add(base)
        for s in WORK_ORDER_SUBS:
            add(f"{base}/{s}")

    else:
        return func.HttpResponse("unknown entity_type", status_code=400)

    return func.HttpResponse(json.dumps({"ok": True, "created": created}), mimetype="application/json")
