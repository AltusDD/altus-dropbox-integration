
import os, re, json, base64
import azure.functions as func
import httpx, dropbox
from lib.dropbox_client import DropboxClient
from lib.pathmap import property_root, unit_root

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

def _sb_headers():
    return {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "content-type": "application/json",
        "prefer": "return=representation",
    }

def _idempotent_lookup(key: str):
    if not key: return None
    if not (SUPABASE_URL and SUPABASE_KEY): return None
    with httpx.Client(timeout=10) as c:
        r = c.get(f"{SUPABASE_URL}/rest/v1/upload_requests",
                  headers=_sb_headers(),
                  params={"idempotency_key": f"eq.{key}", "select": "response"})
        if r.status_code == 200 and r.json():
            return r.json()[0].get("response")
    return None

def _idempotent_store(key: str, response: dict):
    if not key: return
    if not (SUPABASE_URL and SUPABASE_KEY): return
    with httpx.Client(timeout=10) as c:
        c.post(f"{SUPABASE_URL}/rest/v1/upload_requests",
               headers=_sb_headers(), json={"idempotency_key": key, "response": response})

def _ensure_folder(client: DropboxClient, path: str):
    try:
        md = client.dbx.files_get_metadata(path)
        if isinstance(md, dropbox.files.FolderMetadata):
            return
        raise RuntimeError(f"path exists but not folder: {path}")
    except dropbox.exceptions.ApiError as e:
        if "not_found" in str(e).lower():
            client.create_folder_if_not_exists(path); return
        if "conflict" in str(e).lower(): return
        raise

def _slug(s: str) -> str:
    s = (s or "").strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "unnamed"

def _tenancy_key(tenant_name, lease_id=None, application_id=None, tenant_id=None):
    tslug = _slug(tenant_name or "tenant")
    if lease_id:       return f"{int(lease_id)}-{tslug}"
    if application_id: return f"{int(application_id)}-{tslug}"
    if tenant_id:      return f"{int(tenant_id)}-{tslug}"
    return f"tenancy-{tslug}"

def _path_for(entity_type: str, meta: dict) -> str:
    owner_name   = meta.get("owner_name")
    owner_id     = meta.get("owner_id")
    property_nm  = meta.get("property_name")
    property_id  = meta.get("property_id")
    unit_name    = meta.get("unit_name")
    unit_id      = meta.get("unit_id")
    lease_id     = meta.get("lease_id")
    tenant_name  = meta.get("tenant_name")
    application_id = meta.get("application_id")
    tenant_id    = meta.get("tenant_id")

    prop_root = property_root(owner_name, owner_id, property_nm, property_id)
    unit_base = unit_root(owner_name, owner_id, property_nm, property_id, unit_name, unit_id)
    ten_key   = _tenancy_key(tenant_name, lease_id, application_id, tenant_id)

    PATHS = {
        "PropertyPhoto":        f"{prop_root}/11_Media",
        "UnitPhoto":            f"{unit_base}/06_Media",
        "Inspection":           f"{(unit_base if unit_id else prop_root)}/04_Inspections",
        "WorkOrder":            f"{(unit_base if unit_id else prop_root)}/05_Work_Orders",
        "LeaseSigned":          f"{unit_base}/02_Tenancies/{ten_key}/02_Lease/Signed",
        "LeaseAmendment":       f"{unit_base}/02_Tenancies/{ten_key}/02_Lease/Amendments",
        "LeaseAddendum":        f"{unit_base}/02_Tenancies/{ten_key}/02_Lease/Addenda",
        "TenantNotice":         f"{unit_base}/02_Tenancies/{ten_key}/04_Notices",
        "TenantCorrespondence": f"{unit_base}/02_Tenancies/{ten_key}/03_Correspondence",
        "RentReceipt":          f"{unit_base}/02_Tenancies/{ten_key}/05_Rent",
        "SubsidyDoc":           f"{unit_base}/02_Tenancies/{ten_key}/06_Subsidy",
        "MoveInDoc":            f"{unit_base}/02_Tenancies/{ten_key}/08_Move_In",
        "MoveOutDoc":           f"{unit_base}/02_Tenancies/{ten_key}/09_Move_Out",
        "TenantLegal":          f"{unit_base}/02_Tenancies/{ten_key}/10_Legal",
        "TenantCompliance":     f"{unit_base}/02_Tenancies/{ten_key}/11_Compliance",
        "TenantDocument":       f"{unit_base}/02_Tenancies/{ten_key}/12_Documents",
    }
    if entity_type not in PATHS:
        raise ValueError(f"Unknown entity_type '{entity_type}'")
    return PATHS[entity_type]

def _sb_insert(row: dict):
    if not (SUPABASE_URL and SUPABASE_KEY):
        return
    with httpx.Client(timeout=15) as c:
        c.post(f"{SUPABASE_URL}/rest/v1/file_assets", headers=_sb_headers(), json=row)

def main(req: func.HttpRequest) -> func.HttpResponse:
    idem_key = req.headers.get("Idempotency-Key") or (req.get_json(silent=True) or {}).get("idempotency_key")
    prior = _idempotent_lookup(idem_key)
    if prior:
        return func.HttpResponse(json.dumps(prior), mimetype="application/json")

    try:
        payload = req.get_json()
    except Exception:
        return func.HttpResponse("Invalid JSON", status_code=400)

    entity_type      = (payload.get("entity_type") or "").strip()
    meta             = payload.get("meta") or {}
    original_name    = payload.get("original_filename")
    file_base64      = payload.get("file_base64")

    if not entity_type:   return func.HttpResponse("Missing 'entity_type'", status_code=400)
    if not original_name: return func.HttpResponse("Missing 'original_filename'", status_code=400)
    if not file_base64:   return func.HttpResponse("Missing 'file_base64'", status_code=400)

    try:
        data = base64.b64decode(file_base64)
    except Exception:
        return func.HttpResponse("'file_base64' is not valid base64", status_code=400)

    folder = _path_for(entity_type, meta)
    client = DropboxClient.from_env()
    _ensure_folder(client, folder)

    safe_name = re.sub(r'[\\/:*?"<>|]+', "-", original_name).strip() or "file"
    dbx_path  = f"{folder}/{safe_name}"

    res = client.upload_bytes(dbx_path, data)

    response = {"ok": True, "path": getattr(res, 'path_display', None) or dbx_path, "rev": getattr(res, "rev", None)}
    try: _idempotent_store(idem_key, response)
    except Exception: pass

    try:
        _sb_insert({
            "entity_type": entity_type,
            "owner_id": meta.get("owner_id"),
            "owner_name": meta.get("owner_name"),
            "property_id": meta.get("property_id"),
            "property_name": meta.get("property_name"),
            "unit_id": meta.get("unit_id"),
            "unit_name": meta.get("unit_name"),
            "lease_id": meta.get("lease_id"),
            "tenant_id": meta.get("tenant_id"),
            "tenant_name": meta.get("tenant_name"),
            "dropbox_path": response["path"],
            "dropbox_rev": response.get("rev"),
            "size_bytes": len(data),
            "original_name": original_name,
            "source": "api",
            "meta": meta,
        })
    except Exception:
        pass

    return func.HttpResponse(json.dumps(response), mimetype="application/json")
