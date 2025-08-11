from .naming import slugify

APP_ROOT = "Altus_Empire_Command_Center"

# ---- Owner ----
def owner_root(owner_name, owner_id):
    return f"/{APP_ROOT}/00_Owners/{slugify(owner_name)}-{owner_id}"

OWNER_SUBS = [
    "00_Onboarding",
    "01_Agreements",
    "02_Tax_W9",
    "03_Banking_DD",
    "04_Remittance_Packages",
    "05_Communications",
    "06_Legal",
    "07_Notes"
]

# ---- Property (kept at top-level 01_Properties to preserve your current tree) ----
def property_folder_name(property_name, property_id):
    return f"{slugify(property_name)}-{property_id}"

def property_root(owner_name, owner_id, property_name, property_id):
    return f"/{APP_ROOT}/01_Properties/{property_folder_name(property_name, property_id)}"

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
    "11_Applicants",
    "12_Turnover"
]

# ---- Unit ----
def unit_root(owner_name, owner_id, property_name, property_id, unit_name, unit_id):
    prop = property_folder_name(property_name, property_id)
    return f"/{APP_ROOT}/01_Properties/{prop}/01_Units/{slugify(unit_name)}-{unit_id}"

UNIT_SUBS = [
    "01_Photos",
    "02_Inspections",
    "03_Turnover",
    "04_Work_Orders",
    "05_Construction",
    "06_Notices"
]

# ---- Lease ----
def lease_root(owner_name, owner_id, property_name, property_id, lease_id):
    prop = property_folder_name(property_name, property_id)
    return f"/{APP_ROOT}/01_Properties/{prop}/02_Leases/{lease_id}"

LEASE_SUBS = [
    "Signed_Lease_Agreement",
    "Amendments",
    "Tenant_Correspondence",
    "Notices",
    "Subsidy",
    "Legal"
]

# ---- Applicant ----
def applicant_root(owner_name, owner_id, property_name, property_id, applicant_name, applicant_id):
    prop = property_folder_name(property_name, property_id)
    return f"/{APP_ROOT}/01_Properties/{prop}/11_Applicants/{slugify(applicant_name)}-{applicant_id}"

APPLICANT_SUBS = [
    "Application",
    "Screening",
    "Correspondence"
]

# ---- Work Order ----
def work_order_root(owner_name, owner_id, property_name, property_id, unit_name=None, unit_id=None, work_order_id=None):
    prop = property_folder_name(property_name, property_id)
    if unit_id:
        unit = f"{slugify(unit_name)}-{unit_id}"
        return f"/{APP_ROOT}/01_Properties/{prop}/01_Units/{unit}/04_Work_Orders/WO-{work_order_id}"
    return f"/{APP_ROOT}/01_Properties/{prop}/05_Work_Orders/WO-{work_order_id}"
