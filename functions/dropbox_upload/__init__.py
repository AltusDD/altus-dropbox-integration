
import base64, json
import azure.functions as func
from lib.dropbox_client import DropboxClient
from lib.pathmap import (
    property_root, unit_root, lease_root, applicant_root,
    property_work_order_root, unit_turnover_work_order_root
)

def _i(v):
    try: return int(v)
    except Exception: return v

def _prop(meta):
    return property_root(meta.get("owner_name"), _i(meta.get("owner_id")),
                         meta.get("property_name"), _i(meta.get("property_id")))

def _unit(meta):
    return unit_root(meta.get("owner_name"), _i(meta.get("owner_id")),
                     meta.get("property_name"), _i(meta.get("property_id")),
                     meta.get("unit_name"), _i(meta.get("unit_id")))

def _lease(meta):
    return lease_root(meta.get("owner_name"), _i(meta.get("owner_id")),
                      meta.get("property_name"), _i(meta.get("property_id")),
                      _i(meta.get("lease_id")))

def _applicant(meta):
    return applicant_root(meta.get("owner_name"), _i(meta.get("owner_id")),
                          meta.get("property_name"), _i(meta.get("property_id")),
                          _i(meta.get("applicant_id")), meta.get("applicant_name"))

def _pwo(meta, wo_id):
    return property_work_order_root(meta.get("owner_name"), _i(meta.get("owner_id")),
                                    meta.get("property_name"), _i(meta.get("property_id")),
                                    _i(wo_id))

def _uwo(meta, wo_id):
    return unit_turnover_work_order_root(meta.get("owner_name"), _i(meta.get("owner_id")),
                                         meta.get("property_name"), _i(meta.get("property_id")),
                                         meta.get("unit_name"), _i(meta.get("unit_id")),
                                         _i(wo_id))

def build_folder(entity_type: str, m: dict) -> str:
    et = (entity_type or "").lower()

    # Property / Unit media & inspections
    if et == "propertyphoto":      return f"{_prop(m)}/03_Photos"
    if et == "propertyinspection": return f"{_prop(m)}/04_Inspections"
    if et == "unitphoto":          return f"{_unit(m)}/01_Media/01_Photos"
    if et == "unitvideo":          return f"{_unit(m)}/01_Media/02_Videos"
    if et == "unitinspection":     return f"{_unit(m)}/02_Inspections"

    # Turnover lifecycle
    if et == "turnoverprephoto":   return f"{_unit(m)}/03_Turnover/01_Pre_Media"
    if et == "turnoverprevideo":   return f"{_unit(m)}/03_Turnover/01_Pre_Media"
    if et == "turnoverbudget":     return f"{_unit(m)}/03_Turnover/02_Scope_Budget"
    if et == "turnoverpostphoto":  return f"{_unit(m)}/03_Turnover/04_Post_Media"
    if et == "turnoverpostvideo":  return f"{_unit(m)}/03_Turnover/04_Post_Media"

    # Work orders (property-level or unit-turnover, based on presence of unit_id)
    if et in ("workorderdoc", "workorderphoto", "workorderinvoice"):
        wo_id = m.get("work_order_id")
        if m.get("unit_id"):
            base = _uwo(m, wo_id)
        else:
            base = _pwo(m, wo_id)
        if et == "workorderphoto":   return f"{base}/Photos"
        if et == "workorderinvoice": return f"{base}/Invoices"
        return f"{base}/Docs"

    # Lease docs
    if et == "leasesigned":         return f"{_lease(m)}/01_Signed_Lease"
    if et == "leaseamendment":      return f"{_lease(m)}/02_Amendments"
    if et == "leasecorrespondence": return f"{_lease(m)}/03_Tenant_Correspondence"
    if et == "leasemovein":         return f"{_lease(m)}/04_Move_In"
    if et == "leasemoveout":        return f"{_lease(m)}/05_Move_Out"
    if et == "leasenotice":         return f"{_lease(m)}/06_Notices"

    # Applicants
    if et == "applicantapplication":    return f"{_applicant(m)}/Application"
    if et == "applicantscreening":      return f"{_applicant(m)}/Screening"
    if et == "applicantcorrespondence": return f"{_applicant(m)}/Correspondence"

    raise ValueError(f"Unknown entity_type: {entity_type}")

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        payload = req.get_json()
    except Exception:
        return func.HttpResponse("Send JSON body", status_code=400)

    entity_type = payload.get("entity_type")
    meta = payload.get("meta", {})

    try:
        content = base64.b64decode(payload.get("file_base64", ""))
    except Exception:
        return func.HttpResponse("Invalid base64", status_code=400)
    original = payload.get("original_filename", "file.bin")

    try:
        folder = build_folder(entity_type, meta)
    except Exception as e:
        return func.HttpResponse(str(e), status_code=400)

    client = DropboxClient.from_env()
    md = client.upload_file(folder, original, content)

    out = {"ok": True, "dropbox_path": getattr(md, "path_display", None), "name": getattr(md, "name", original), "size": getattr(md, "size", None)}
    return func.HttpResponse(json.dumps(out), mimetype="application/json")
