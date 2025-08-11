from .naming import slugify

ROOT = "Altus_Empire_Command_Center"

# ---- Roots ----
def owner_root(owner_name: str, owner_id: int) -> str:
    return f"{ROOT}/01_Owners/{slugify(owner_name)}-{owner_id}"

def property_root(owner_name: str, owner_id: int, property_name: str, property_id: int) -> str:
    return f"{owner_root(owner_name, owner_id)}/Properties/{slugify(property_name)}-{property_id}"

def unit_root(owner_name: str, owner_id: int, property_name: str, property_id: int, unit_name: str, unit_id: int) -> str:
    return f"{property_root(owner_name, owner_id, property_name, property_id)}/01_Units/{slugify(unit_name)}-{unit_id}"

def lease_root(owner_name: str, owner_id: int, property_name: str, property_id: int, lease_id: int) -> str:
    return f"{property_root(owner_name, owner_id, property_name, property_id)}/02_Leases/{lease_id}"

def applicant_root(owner_name: str, owner_id: int, property_name: str, property_id: int, applicant_id: int, applicant_name: str) -> str:
    return f"{property_root(owner_name, owner_id, property_name, property_id)}/10_Applicants/{slugify(applicant_name)}-{applicant_id}"

# ---- Property containers (always created at property provision) ----
PROPERTY_CONTAINERS = [
    "02_Leases",
    "03_Photos",
    "04_Inspections",
    "05_Work_Orders",
    "06_Legal",
    "07_Financials",
    "08_Acquisition_Docs",
    "10_Applicants",
]

# ---- Lease docs ----
LEASE_SUBS = [
    "01_Signed_Lease",
    "02_Amendments",
    "03_Tenant_Correspondence",
    "04_Move_In",
    "05_Move_Out",
    "06_Notices",
]

# ---- Unit structure ----
UNIT_SUBS = [
    "01_Media/01_Photos",
    "01_Media/02_Videos",
    "02_Inspections",
    "03_Turnover/01_Pre_Media",
    "03_Turnover/02_Scope_Budget",
    "03_Turnover/03_Work_Orders",
    "03_Turnover/04_Post_Media",
]

# ---- Applicants ----
APPLICANT_SUBS = ["Application", "Screening", "Correspondence"]

# ---- Work Orders ----
def property_work_order_root(owner_name: str, owner_id: int, property_name: str, property_id: int, work_order_id: int) -> str:
    return f"{property_root(owner_name, owner_id, property_name, property_id)}/05_Work_Orders/{work_order_id}"

def unit_turnover_work_order_root(owner_name: str, owner_id: int, property_name: str, property_id: int,
                                  unit_name: str, unit_id: int, work_order_id: int) -> str:
    return f"{unit_root(owner_name, owner_id, property_name, property_id, unit_name, unit_id)}/03_Turnover/03_Work_Orders/{work_order_id}"

WORK_ORDER_SUBS = ["Bids", "POs", "Photos", "Invoices", "Docs"]
