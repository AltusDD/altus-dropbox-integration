
from .naming import slugify

ROOT = "/Altus_Empire_Command_Center"

def property_root(meta: dict) -> str:
    pname = meta.get("property_name") or meta.get("name") or "property"
    pid = meta.get("property_id") or meta.get("id") or 0
    return f"{ROOT}/01_Properties/{slugify(pname)}-{pid}"

def unit_root(meta: dict) -> str:
    base = property_root(meta)
    uname = meta.get("unit_name") or meta.get("name") or "unit"
    uid = meta.get("unit_id") or meta.get("id") or 0
    return f"{base}/01_Units/{slugify(uname)}-{uid}"

def lease_root(meta: dict) -> str:
    base = property_root(meta)
    lid = meta.get("lease_id") or meta.get("id") or 0
    return f"{base}/02_Leases/{lid}"

def canonical_folders_for(entity_type: str, meta_or_new: dict) -> list[str]:
    t = (entity_type or "").lower()
    if t == "property":
        pr = property_root(meta_or_new)
        return [
            pr + "/01_Units",
            pr + "/02_Leases",
            pr + "/03_Photos",
            pr + "/04_Inspections",
            pr + "/05_Work_Orders",
            pr + "/06_Legal",
            pr + "/07_Financials",
            pr + "/08_Acquisition_Docs",
        ]
    if t == "unit":
        ur = unit_root(meta_or_new)
        return [ur + "/01_Photos", ur + "/02_Inspections"]
    if t == "lease":
        lr = lease_root(meta_or_new)
        return [lr + "/Signed_Lease_Agreement", lr + "/Amendments", lr + "/Tenant_Correspondence"]
    return []

def upload_folder_for(entity_type: str, meta: dict) -> str:
    t = (entity_type or "").lower()
    if t == "propertyphoto":
        return property_root(meta) + "/03_Photos"
    if t == "unitphoto":
        return unit_root(meta) + "/01_Photos"
    if t == "inspection":
        return property_root(meta) + "/04_Inspections"
    if t == "leasesigned":
        return lease_root(meta) + "/Signed_Lease_Agreement"
    if t == "leaseamendment":
        return lease_root(meta) + "/Amendments"
    if t == "leasecorrespondence":
        return lease_root(meta) + "/Tenant_Correspondence"
    if t == "deal_room":
        return ROOT + "/04_Deal_Room"
    return property_root(meta)
