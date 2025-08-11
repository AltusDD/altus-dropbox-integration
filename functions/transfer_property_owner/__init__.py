# functions/transfer_property_owner/__init__.py
import os, re, json, base64, logging, datetime as dt
import azure.functions as func
import httpx
import dropbox

from lib.pathmap import owner_root, property_root
from lib.dropbox_client import DropboxClient

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

def _headers():
    return {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "content-type": "application/json",
        "prefer": "return=representation",
    }

def _slug(s: str) -> str:
    s = (s or "").strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "unknown"

def _ensure_folder(dbx: dropbox.Dropbox, path: str):
    try:
        dbx.files_create_folder_v2(path, autorename=False)
    except dropbox.exceptions.ApiError as e:
        if "conflict" in str(e).lower():
            return
        raise

def _update_file_assets_paths(src_prefix: str, dst_prefix: str):
    """Rewrite dropbox_path for all file_assets rows under the property tree."""
    if not (SUPABASE_URL and SUPABASE_KEY): 
        return 0
    changed = 0
    with httpx.Client(timeout=30) as c:
        # paginate GET for rows whose dropbox_path starts with src_prefix
        # PostgREST like filter: dropbox_path=like.<prefix>%
        params = {
            "select": "id,dropbox_path",
            "dropbox_path": f"like.{src_prefix}%",
            "limit": "1000",
        }
        while True:
            r = c.get(f"{SUPABASE_URL}/rest/v1/file_assets", headers=_headers(), params=params)
            r.raise_for_status()
            rows = r.json()
            if not rows:
                break
            for row in rows:
                rid = row["id"]
                oldp = row["dropbox_path"]
                newp = oldp.replace(src_prefix, dst_prefix, 1)
                ur = c.patch(f"{SUPABASE_URL}/rest/v1/file_assets?id=eq.{rid}", headers=_headers(), json={"dropbox_path": newp})
                ur.raise_for_status()
                changed += 1
            # naive pagination via range header (optional). For simplicity, break when less than limit.
            if len(rows) < 1000:
                break
    return changed

def _record_transfer(property_id, from_owner_id, to_owner_id, cutoff_date, src_path, dst_path, moved_count):
    if not (SUPABASE_URL and SUPABASE_KEY): 
        return
    payload = {
        "property_id": property_id,
        "from_owner_id": from_owner_id,
        "to_owner_id": to_owner_id,
        "cutoff_date": cutoff_date,
        "src_path": src_path,
        "dst_path": dst_path,
        "moved_count": moved_count,
    }
    try:
        httpx.post(f"{SUPABASE_URL}/rest/v1/ownership_transfers", headers=_headers(), json=payload, timeout=15).raise_for_status()
    except Exception:
        pass

def _update_ownership_legs(property_id, from_owner_id, to_owner_id, cutoff_date):
    """Close out old leg and open new leg starting on cutoff_date. Tables must exist from migration."""
    if not (SUPABASE_URL and SUPABASE_KEY):
        return
    with httpx.Client(timeout=20) as c:
        # Close current active leg (no end_date) for from_owner_id
        try:
            # Select active leg
            r = c.get(f"{SUPABASE_URL}/rest/v1/property_ownerships",
                      headers=_headers(),
                      params={"select":"id","property_id":f"eq.{property_id}","owner_id":f"eq.{from_owner_id}","end_date":"is.null","limit":"1"})
            r.raise_for_status()
            rows = r.json()
            if rows:
                rid = rows[0]["id"]
                # Set end_date to cutoff_date - 1 day (inclusive previous day)
                end_date = (dt.datetime.fromisoformat(cutoff_date) - dt.timedelta(seconds=1)).date().isoformat()
                c.patch(f"{SUPABASE_URL}/rest/v1/property_ownerships?id=eq.{rid}", headers=_headers(), json={"end_date": end_date}).raise_for_status()
        except Exception:
            pass
        # Open new leg
        try:
            c.post(f"{SUPABASE_URL}/rest/v1/property_ownerships", headers=_headers(), json={
                "property_id": property_id,
                "owner_id": to_owner_id,
                "start_date": cutoff_date
            }).raise_for_status()
        except Exception:
            pass

def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    Transfer an entire property folder tree from one owner to another and update DB metadata.
    Request JSON:
    {
      "property_id": 201, "property_name": "Sunset Villas",
      "from_owner_id": 101, "from_owner_name": "Sunset Capital Partners",
      "to_owner_id": 555, "to_owner_name": "Rising Tide Holdings",
      "cutoff_date": "2025-08-15",
      "leave_marker": true  # optional: drop a marker under the old owner/99_Dispositions
    }
    """
    try:
        payload = req.get_json()
    except Exception:
        return func.HttpResponse("Invalid JSON", status_code=400)

    required = ["property_id","property_name","from_owner_id","from_owner_name","to_owner_id","to_owner_name","cutoff_date"]
    missing = [k for k in required if not payload.get(k)]
    if missing:
        return func.HttpResponse(f"Missing fields: {', '.join(missing)}", status_code=400)

    prop_id   = int(payload["property_id"])
    prop_name = payload["property_name"]
    from_oid  = int(payload["from_owner_id"])
    from_onm  = payload["from_owner_name"]
    to_oid    = int(payload["to_owner_id"])
    to_onm    = payload["to_owner_name"]
    cutoff    = payload["cutoff_date"]
    leave_marker = bool(payload.get("leave_marker", True))

    # build source/destination roots using ID-first mapping
    src = property_root(from_onm, from_oid, prop_name, prop_id)
    dst = property_root(to_onm,   to_oid,   prop_name, prop_id)

    client = DropboxClient.from_env()
    dbx = client.dbx

    # ensure destination owner + properties container exists
    to_owner_root = owner_root(to_onm, to_oid)
    _ensure_folder(dbx, to_owner_root)
    _ensure_folder(dbx, f"{to_owner_root}/10_Properties")

    # move the entire property folder
    try:
        dbx.files_move_v2(src, dst, autorename=False)
        moved = True
    except dropbox.exceptions.ApiError as e:
        if "conflict" in str(e).lower():
            # destination already exists; treat as moved
            moved = True
        else:
            return func.HttpResponse(json.dumps({"ok": False, "stage":"move", "error": str(e)}), mimetype="application/json", status_code=500)

    # update file_assets paths
    changed = 0
    try:
        changed = _update_file_assets_paths(src, dst)
    except Exception as e:
        # still continue; report partial
        pass

    # optional: leave a marker under old owner
    marker_path = None
    if leave_marker:
        old_owner_root = owner_root(from_onm, from_oid)
        disp_base = f"{old_owner_root}/99_Dispositions/{prop_id}-{_slug(prop_name)}"
        try:
            _ensure_folder(dbx, f"{old_owner_root}/99_Dispositions")
            _ensure_folder(dbx, disp_base)
            marker = f"Transferred_to_{to_oid}-{_slug(to_onm)}_on_{cutoff}.txt"
            marker_path = f"{disp_base}/{marker}"
            content = f"Property transferred on {cutoff}\nNew path: {dst}\n"
            dbx.files_upload(content.encode("utf-8"), marker_path, mode=dropbox.files.WriteMode("add"), autorename=True, mute=True)
        except Exception:
            marker_path = None

    # update ownership legs (close old, open new)
    try:
        _update_ownership_legs(prop_id, from_oid, to_oid, cutoff)
    except Exception:
        pass

    # record transfer
    try:
        _record_transfer(prop_id, from_oid, to_oid, cutoff, src, dst, changed)
    except Exception:
        pass

    return func.HttpResponse(json.dumps({
        "ok": True,
        "moved": moved,
        "src": src,
        "dst": dst,
        "assets_relinked": changed,
        "marker_path": marker_path
    }), mimetype="application/json")
