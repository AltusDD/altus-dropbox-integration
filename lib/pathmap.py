import re
from typing import Optional

APP_ROOT = "Altus_Empire_Command_Center"

_slug_re = re.compile(r"[^a-z0-9]+")
def slugify(s: Optional[str]) -> str:
    if not s:
        return "unknown"
    s = s.lower().strip()
    s = _slug_re.sub("-", s)
    s = s.strip("-")
    return s or "unknown"

# ---- Empire Grade subfolders ----
OWNER_SUBS = [
    "01_Profile",
    "02_Agreements",
    "03_Tax",
    "04_Comms",
    "05_Reports",
    "06_Bill_Pay",
    "07_Legal",
]

PROPERTY_SUBS = [
    "01_Units",
    "02_Leases",
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

UNIT_SUBS = [
    "01_Photos",
    "02_Inspections",
    "03_Work_Orders",
    "04_Legal",
    "05_Turnover",
    "06_Media",
    "07_Construction",
]

LEASE_SUBS = [
    "Signed_Lease_Agreement",
    "Amendments",
    "Tenant_Correspondence",
    "Notices",
    "Subsidy_Vouchers",
    "Applications",
]

def owner_root(owner_name: Optional[str], owner_id: Optional[int]) -> str:
    return f"/{APP_ROOT}/00_Owners/{slugify(owner_name)}-{owner_id}"

# Keeping properties at the same level you already used
def property_root(owner_name: Optional[str], owner_id: Optional[int],
                  property_name: Optional[str], property_id: Optional[int]) -> str:
    return f"/{APP_ROOT}/01_Properties/{slugify(property_name)}-{property_id}"

def unit_root(owner_name: Optional[str], owner_id: Optional[int],
              property_name: Optional[str], property_id: Optional[int],
              unit_name: Optional[str], unit_id: Optional[int]) -> str:
    return (
        f"/{APP_ROOT}/01_Properties/{slugify(property_name)}-{property_id}"
        f"/01_Units/{slugify(unit_name)}-{unit_id}"
    )

def lease_root(owner_name: Optional[str], owner_id: Optional[int],
               property_name: Optional[str], property_id: Optional[int],
               lease_id: Optional[int]) -> str:
    return (
        f"/{APP_ROOT}/01_Properties/{slugify(property_name)}-{property_id}"
        f"/02_Leases/{lease_id}"
    )
