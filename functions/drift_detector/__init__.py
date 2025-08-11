
# functions/drift_detector/__init__.py
import os, json, logging
import httpx
from lib.pathmap import owner_root, property_root, unit_root, tenancy_root, OWNER_SUBS, PROPERTY_SUBS, UNIT_SUBS, TENANCY_SUBS
from lib.dropbox_client import DropboxClient

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

def _hdrs():
    return {"apikey": SUPABASE_KEY, "Authorization": f"Bearer {SUPABASE_KEY}"}

def _ensure(dbx, p):
    try:
        dbx.files_create_folder_v2(p, autorename=False)
        logging.info("create %s", p)
    except Exception as e:
        if "conflict" in str(e).lower(): return
        raise

def main(mytimer):
    logging.info("drift_detector starting")
    if not (SUPABASE_URL and SUPABASE_KEY):
        logging.warning("missing supabase config; skipping")
        return

    client = DropboxClient.from_env()
    dbx = client.dbx

    with httpx.Client(timeout=30) as c:
        # Owners
        try:
            ro = c.get(f"{SUPABASE_URL}/rest/v1/owners", headers=_hdrs(), params={"select":"id,name"})
            ro.raise_for_status()
            for o in ro.json():
                o_base = owner_root(o["name"], o["id"])
                _ensure(dbx, o_base)
                for s in OWNER_SUBS:
                    _ensure(dbx, f"{o_base}/{s}")
        except Exception:
            pass

        # Properties
        try:
            rp = c.get(f"{SUPABASE_URL}/rest/v1/properties", headers=_hdrs(), params={"select":"id,name,owner_id,owner_name"})
            rp.raise_for_status()
            for p in rp.json():
                p_base = property_root(p.get("owner_name"), p.get("owner_id"), p["name"], p["id"])
                _ensure(dbx, p_base)
                for s in PROPERTY_SUBS:
                    _ensure(dbx, f"{p_base}/{s}")
        except Exception:
            pass

        # Units
        try:
            ru = c.get(f"{SUPABASE_URL}/rest/v1/units", headers=_hdrs(), params={"select":"id,name,property_id,property_name,owner_id,owner_name"})
            ru.raise_for_status()
            for u in ru.json():
                u_base = unit_root(u.get("owner_name"), u.get("owner_id"), u.get("property_name"), u.get("property_id"), u["name"], u["id"])
                _ensure(dbx, u_base)
                for s in UNIT_SUBS:
                    _ensure(dbx, f"{u_base}/{s}")
        except Exception:
            pass

        # Tenancies (leases)
        try:
            rl = c.get(f"{SUPABASE_URL}/rest/v1/leases", headers=_hdrs(), params={"select":"id,tenant_id,tenant_name,unit_id,unit_name,property_id,property_name,owner_id,owner_name"})
            rl.raise_for_status()
            for l in rl.json():
                base = tenancy_root(l.get("owner_name"), l.get("owner_id"),
                                    l.get("property_name"), l.get("property_id"),
                                    l.get("unit_name"), l.get("unit_id"),
                                    {"lease_id": l["id"], "tenant_id": l.get("tenant_id"), "tenant_name": l.get("tenant_name")})
                _ensure(dbx, base)
                for s in TENANCY_SUBS:
                    _ensure(dbx, f"{base}/{s}")
        except Exception:
            pass

    logging.info("drift_detector done")
