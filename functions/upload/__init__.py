import os, json, base64, logging, httpx, azure.functions as func
from lib.dropbox_client import DropboxClient
from lib.naming import unique_filename
from lib.pathmap import (
    property_root, unit_root, lease_root, owner_root, applicant_root, work_order_root
)

def _supabase_headers():
    url = os.getenv("SUPABASE_URL"); key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
    return url, {"apikey": key, "Authorization": f"Bearer {key}", "Content-Type": "application/json"}

def _save_asset(record):
    url, hdrs = _supabase_headers()
    try:
        with httpx.Client(timeout=20) as c:
            r = c.post(f"{url}/rest/v1/file_assets", headers=hdrs, json=record, params={"return":"minimal"})
            # ignore errors silently to keep upload path robust
    except Exception:
        pass

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        payload = req.get_json()
    except ValueError:
        return func.HttpResponse("Bad JSON", status_code=400)

    entity_type = payload.get("entity_type")
    meta = payload.get("meta", {})
    original = payload.get("original_filename") or "file.bin"
    b64 = payload.get("file_base64")
    if not b64:
        return func.HttpResponse("Missing file_base64", status_code=400)

    try:
        data = base64.b64decode(b64, validate=True)
    except Exception:
        return func.HttpResponse("Invalid base64", status_code=400)

    # route path
    try:
        if entity_type in ("PropertyPhoto","PropertyVideo","PropertyNotice"):
            base = property_root(meta.get("owner_name"), meta.get("owner_id"), meta.get("property_name"), meta.get("property_id"))
            sub = "03_Photos" if entity_type!="PropertyVideo" else "03_Photos"
            folder = f"{base}/{sub}"
        elif entity_type in ("UnitPhoto","Inspection","TurnoverPrePhoto","TurnoverPostPhoto","TurnoverBudget"):
            base = unit_root(meta.get("owner_name"), meta.get("owner_id"), meta.get("property_name"), meta.get("property_id"), meta.get("unit_name"), meta.get("unit_id"))
            sub = "01_Photos" if entity_type.endswith("Photo") else "02_Inspections" if entity_type=="Inspection" else "03_Turnover"
            folder = f"{base}/{sub}"
        elif entity_type in ("LeaseSigned","LeaseAmendment","LeaseCorrespondence","LeaseNotice","LeaseSubsidyVoucher","MoveInDoc","MoveOutDoc"):
            base = lease_root(meta.get("owner_name"), meta.get("owner_id"), meta.get("property_name"), meta.get("property_id"), meta.get("lease_id"))
            mapping = {
                "LeaseSigned": "Signed_Lease_Agreement",
                "LeaseAmendment": "Amendments",
                "LeaseCorrespondence": "Tenant_Correspondence",
                "LeaseNotice": "Notices",
                "LeaseSubsidyVoucher": "Subsidy",
                "MoveInDoc": "Legal",
                "MoveOutDoc": "Legal"
            }
            folder = f"{base}/{mapping.get(entity_type,'Legal')}"
        elif entity_type in ("OwnerManagementAgreement","OwnerW9","OwnerDirectDeposit","OwnerRemitPackage","OwnerCommunication"):
            base = owner_root(meta.get("owner_name"), meta.get("owner_id"))
            mapping = {
                "OwnerManagementAgreement":"01_Agreements",
                "OwnerW9":"02_Tax_W9",
                "OwnerDirectDeposit":"03_Banking_DD",
                "OwnerRemitPackage":"04_Remittance_Packages",
                "OwnerCommunication":"05_Communications"
            }
            folder = f"{base}/{mapping.get(entity_type,'07_Notes')}"
        elif entity_type in ("ApplicantDoc",):
            base = applicant_root(meta.get("owner_name"), meta.get("owner_id"), meta.get("property_name"), meta.get("property_id"), meta.get("applicant_name"), meta.get("applicant_id"))
            cat = meta.get("category") or "Application"
            folder = f"{base}/{cat}"
        elif entity_type in ("WorkOrderDoc",):
            base = work_order_root(meta.get("owner_name"), meta.get("owner_id"), meta.get("property_name"), meta.get("property_id"), meta.get("unit_name"), meta.get("unit_id"), meta.get("work_order_id"))
            cat = meta.get("category") or "Docs"
            folder = f"{base}/{cat}"
        else:
            return func.HttpResponse(f"Unknown entity_type: {entity_type}", status_code=400)
    except Exception as e:
        logging.exception("Path routing failed")
        return func.HttpResponse("Bad meta for routing", status_code=400)

    client = DropboxClient.from_env()
    client.ensure_folder(folder)

    stored = unique_filename(original)
    full_path = f"{folder}/{stored}"
    try:
        meta_dbx = client.upload(full_path, data)
    except Exception as e:
        logging.exception("Upload failed")
        return func.HttpResponse("Upload failed", status_code=500)

    # best-effort asset record
    _save_asset({
        "original_filename": original,
        "stored_filename": stored,
        "dropbox_path": full_path,
        "entity_type": entity_type,
        "entity_id": meta.get("lease_id") or meta.get("unit_id") or meta.get("property_id") or meta.get("owner_id") or meta.get("applicant_id") or meta.get("work_order_id"),
        "size_bytes": len(data)
    })

    return func.HttpResponse(json.dumps({"ok": True, "dropbox_path": full_path, "dbx_meta": meta_dbx}), mimetype="application/json")
