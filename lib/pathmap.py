# lib/pathmap.py
import re
from typing import Optional, Dict, Any

ROOT = "/Altus_Empire_Command_Center"
OWNERS_DIR = "00_Owners"
AUM_DIR = "10_AUM"  # Assets Under Management under each owner

# ---------- helpers ----------
_slug_rx = re.compile(r"[^a-z0-9]+")
def slugify(name: Optional[str]) -> str:
    if not name:
        return "unknown"
    s = name.strip().lower()
    s = _slug_rx.sub("-", s).strip("-")
    return s or "unknown"

def _tag(name: str, _id: Optional[int | str]) -> str:
    sid = f"-{_id}" if _id not in (None, "", "null") else ""
    return f"{slugify(name)}{sid}"

# ---------- owner ----------
def owner_root(owner_name: str, owner_id: Optional[int | str]) -> str:
    return f"{ROOT}/{OWNERS_DIR}/{_tag(owner_name, owner_id)}"

OWNER_SUBS = [
    "01_Profile",
    "02_Agreements",
    "03_Tax",
    "04_Comms",
    "05_Reports",
    "06_Bill_Pay",
    "07_Legal",
    AUM_DIR,  # where all properties live
]

# ---------- property (under owner/AUM) ----------
def property_root(owner_name: str, owner_id: Optional[int | str],
                  property_name: str, property_id: Optional[int | str]) -> str:
    return f"{owner_root(owner_name, owner_id)}/{AUM_DIR}/{_tag(property_name, property_id)}"

PROPERTY_SUBS = [
    "01_Units",
    "02_Leases",           # optional index/archive; primary lease docs live in Tenancies
    "03_Photos",
    "04_Inspections",
    "05_Work_Orders",
    "06_Legal",
    "07_Financials",
    "08_Acquisition_Docs",
    "09_Notices",
    "10_Construction",
    "11_Media",
]

# ---------- unit (under property/01_Units) ----------
def unit_root(owner_name: str, owner_id: Optional[int | str],
              property_name: str, property_id: Optional[int | str],
              unit_name: str, unit_id: Optional[int | str]) -> str:
    return f"{property_root(owner_name, owner_id, property_name, property_id)}/01_Units/{_tag(unit_name, unit_id)}"

UNIT_SUBS = [
    "01_Photos",        # unit-level
    "02_Tenancies",     # tenancy folders live here
    "03_Inspections",
    "04_Work_Orders",
    "05_Legal",
    "06_Media",
    "07_Construction",
]

# ---------- tenancy (application -> lease -> move-out) ----------
TENANCY_SUBS = [
    "00_Application",
    "01_Screening",
    "02_Lease/Signed",
    "02_Lease/Amendments",
    "02_Lease/Addenda",
    "03_Correspondence",
    "04_Notices",
    "05_Rent",
    "06_Subsidy",
    "07_Maintenance",
    "08_Move_In",
    "09_Move_Out",
    "10_Legal",
    "11_Compliance",
    "12_Documents",
]

def tenancy_key(meta: Dict[str, Any]) -> str:
    """
    Choose a stable, human-readable key for the tenancy folder.
    Priority: lease_id -> application_id -> tenant_id.
    """
    name = meta.get("tenant_name") or "tenant"
    if meta.get("lease_id"):      return _tag(name, f"lease-{meta['lease_id']}")
    if meta.get("application_id"):return _tag(name, f"app-{meta['application_id']}")
    if meta.get("tenant_id"):     return _tag(name, f"tenant-{meta['tenant_id']}")
    return _tag(name, "tenancy")

def tenancy_root(owner_name: str, owner_id: Optional[int | str],
                 property_name: str, property_id: Optional[int | str],
                 unit_name: str, unit_id: Optional[int | str],
                 meta: Dict[str, Any]) -> str:
    base_unit = unit_root(owner_name, owner_id, property_name, property_id, unit_name, unit_id)
    return f"{base_unit}/02_Tenancies/{tenancy_key(meta)}"

# ---------- (optional) legacy lease root (kept for compatibility) ----------
def lease_root(owner_name: str, owner_id: Optional[int | str],
               property_name: str, property_id: Optional[int | str],
               lease_id: Optional[int | str]) -> str:
    return f"{property_root(owner_name, owner_id, property_name, property_id)}/02_Leases/{_tag('lease', lease_id)}"

LEASE_SUBS = [
    "Signed_Lease_Agreement",
    "Amendments",
    "Tenant_Correspondence",
]
