# dropbox_upload/__init__.py  (FULL REPLACEMENT)

import os, re, json, base64, hashlib
import azure.functions as func
import httpx
import dropbox

from lib.dropbox_client import DropboxClient
from lib.pathmap import owner_root, property_root, unit_root, lease_root  # roots we already have

# ---------- Supabase helper ----------
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

def _sb_insert(row: dict):
    if not (SUPABASE_URL and SUPABASE_KEY):
        return
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "content-type": "application/json",
        "prefer": "return=representation",
    }
    try:
        httpx.post(f"{SUPABASE_URL}/rest/v1/file_assets", headers=headers, json=row, timeout=15).raise_for_status()
    except Exception:
        # Don’t fail the upload if logging the row has a hiccup
        pass

# ---------- Dropbox helpers ----------
def _ensure_folder(client: DropboxClient, path: str):
    """
    Idempotently ensure a folder exists at `path` using the Dropbox SDK.
    """
    try:
        md = client.dbx.files_get_metadata(path)
        if isinstance(md, dropbox.files.FolderMetadata):
            return
        raise RuntimeError(f"path exists but is not a folder: {path}")
    except dropbox.exceptions.ApiError as e:
        # create if not_found
        try:
            if e.error.is_path() and e.error.get_path().is_not_found():
                client.dbx.files_create_folder_v2(path, autorename=False)
                return
        except Exception:
            pass
        if "conflict" in str(e).lower():
            return
        raise

def _slug(s: str) -> str:
    s = (s or "").strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "unnamed"

def _tenancy_slug(tenant_name: str, lease_id) -> str:
    return f"{_slug(tenant_name)}-lease-{lease_id}" if lease_id else _slug(tenant_name)

def _path_for(entity_type: str, meta: dict) -> str:
    """
    Returns the target Dropbox folder for this upload based on entity_type + metadata.
    Only a focused set is mapped here; extend as needed.
    """
    owner_name   = meta.get("owner_name")
    owner_id     = meta.get("owner_id")
    property_nm  = meta.get("property_name")
    property_id  = meta.get("property_id")
    unit_name    = meta.get("unit_name")
    unit_id      = meta.get("unit_id")
    lease_id     = meta.get("lease_id")
    tenant_name  = meta.get("tenant_name")

    # anchors
    prop_root = property_root(owner_name, owner_id, property_nm, property_id)
    unit_base = unit_root(owner_name, owner_id, property_nm, property_id, unit_name, unit_id)
    ten_slug  = _tenancy_slug(tenant_name, lease_id)

    # map of smart destinations
    PATH_BUILDERS = {
        # media
        "PropertyPhoto":        lambda m: f"{prop_root}/11_Media",
        "UnitPhoto":            lambda m: f"{unit_base}/06_Media",

        # inspections / work orders
        "Inspection":           lambda m: f"{(unit_base if unit_id else prop_root)}/02_Inspections",
        "WorkOrder":            lambda m: f"{(unit_base if unit_id else prop_root)}/03_Work_Orders",

        # tenancy-centric
        "LeaseSigned":          lambda m: f"{unit_base}/02_Tenancies/{ten_slug}/02_Lease/Signed",
        "LeaseAmendment":       lambda m: f"{unit_base}/02_Tenancies/{ten_slug}/02_Lease/Amendments",
        "LeaseAddendum":        lambda m: f"{unit_base}/02_Tenancies/{ten_slug}/02_Lease/Addenda",
        "TenantNotice":         lambda m: f"{unit_base}/02_Tenancies/{ten_slug}/04_Notices",
        "TenantCorrespondence": lambda m: f"{unit_base}/02_Tenancies/{ten_slug}/03_Correspondence",
        "RentReceipt":          lambda m: f"{unit_base}/02_Tenancies/{ten_slug}/05_Rent",
        "SubsidyDoc":           lambda m: f"{unit_base}/02_Tenancies/{ten_slug}/06_Subsidy",
        "MoveInDoc":            lambda m: f"{unit_base}/02_Tenancies/{ten_slug}/08_Move_In",
        "MoveOutDoc":           lambda m: f"{unit_base}/02_Tenancies/{ten_slug}/09_Move_Out",
        "TenantLegal":          lambda m: f"{unit_base}/02_Tenancies/{ten_slug}/10_Legal",
        "TenantCompliance":     lambda m: f"{unit_base}/02_Tenancies/{ten_slug}/11_Compliance",
        "TenantDocument":       lambda m: f"{unit_base}/02_Tenancies/{ten_slug}/12_Documents",
    }

    builder = PATH_BUILDERS.get(entity_type)
    if not builder:
        raise ValueError(f"Unknown entity_type '{entity_type}'")
    return builder(meta)

# ---------- Azure Function ----------
def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        payload = req.get_json()
    except Exception:
        return func.HttpResponse("Invalid JSON", status_code=400)

    entity_type      = (payload.get("entity_type") or "").strip()
    meta             = payload.get("meta") or {}
    original_name    = payload.get("original_filename")
    file_base64      = payload.get("file_base64")

    if not entity_type:
        return func.HttpResponse("Missing 'entity_type'", status_code=400)
    if not original_name:
        return func.HttpResponse("Missing 'original_filename'", status_code=400)
    if not file_base64:
        return func.HttpResponse("Missing 'file_base64'", status_code=400)

    # decode file
    try:
        data = base64.b64decode(file_base64)
    except Exception:
        return func.HttpResponse("'file_base64' is not valid base64", status_code=400)

    # figure out destination folder
    try:
        folder = _path_for(entity_type, meta)
    except Exception as e:
        return func.HttpResponse(str(e), status_code=400)

    # upload to Dropbox
    client = DropboxClient.from_env()
    _ensure_folder(client, folder)

    safe_name = re.sub(r'[\\/:*?"<>|]+', "-", original_name).strip() or "file"
    dbx_path  = f"{folder}/{safe_name}"

    client.dbx.files_upload(
        data,
        dbx_path,
        mode=dropbox.files.WriteMode("add"),
        autorename=True,
        mute=True,
    )

    # log in Supabase (best-effort)
    _sb_insert({
        "entity_type": entity_type,
        "owner_id": meta.get("owner_id"),
        "property_id": meta.get("property_id"),
        "unit_id": meta.get("unit_id"),
        "lease_id": meta.get("lease_id"),
        "tenant_id": meta.get("tenant_id"),
        "tenant_name": meta.get("tenant_name"),
        "dbx_path": dbx_path,
        "original_filename": original_name,
        "original_bytes": len(data),
        "content_hash": hashlib.sha1(data).hexdigest(),
        "stored_by": "api",
        "ingest_source": "azure",
    })

    return func.HttpResponse(json.dumps({"ok": True, "path": dbx_path}), mimetype="application/json")
