from __future__ import annotations
import json, logging
import azure.functions as func
from lib.dropbox_client import ensure_folder_tree
from lib.pathmap import ROOT, property_root, unit_root, lease_root

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        payload = req.get_json()
    except Exception:
        return func.HttpResponse("Invalid JSON", status_code=400)

    entity_type = (payload or {}).get("entity_type")
    row = (payload or {}).get("new") or {}

    try:
        paths = [ROOT]
        if entity_type == "property":
            base = property_root(row["name"], row["id"])  # requires: id, name
            paths += [
                base,
                f"{base}/01_Units",
                f"{base}/02_Leases",
                f"{base}/03_Photos",
                f"{base}/04_Inspections",
                f"{base}/05_Work_Orders",
                f"{base}/06_Legal",
                f"{base}/07_Financials",
                f"{base}/08_Acquisition_Docs",
            ]
        elif entity_type == "unit":
            base = unit_root(row["property_name"], row["property_id"], row["name"], row["id"])
            paths += [base, f"{base}/01_Photos", f"{base}/02_Inspections"]
        elif entity_type == "lease":
            base = lease_root(row["property_name"], row["property_id"], row["id"])
            paths += [
                base,
                f"{base}/Signed_Lease_Agreement",
                f"{base}/Amendments",
                f"{base}/Tenant_Correspondence",
            ]
        else:
            return func.HttpResponse("Unknown entity_type", status_code=400)

        ensure_folder_tree(*paths)
        return func.HttpResponse("ok", status_code=200)
    except Exception as e:
        logging.exception("provision error")
        return func.HttpResponse(str(e), status_code=500)
