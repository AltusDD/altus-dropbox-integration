from .naming import slugify
ROOT = "/Altus_Empire_Command_Center"

def property_root(name: str, pid: int) -> str:
    return f"{ROOT}/01_Properties/{slugify(name)}-{pid}"

def unit_root(pname: str, pid: int, uname: str, uid: int) -> str:
    return f"{property_root(pname,pid)}/01_Units/{slugify(uname)}-{uid}"

def folder_for(entity_type: str, meta: dict) -> str:
    t = (entity_type or "").lower()
    if t == "propertyphoto":
        return f"{property_root(meta['property_name'], int(meta['property_id']))}/03_Photos"
    if t == "unitphoto":
        return f"{unit_root(meta['property_name'], int(meta['property_id']), meta['unit_name'], int(meta['unit_id']))}/01_Photos"
    if t == "leasesigned":
        return f"{property_root(meta['property_name'], int(meta['property_id']))}/02_Leases/{int(meta['lease_id'])}/Signed_Lease_Agreement"
    if t == "leaseamendment":
        return f"{property_root(meta['property_name'], int(meta['property_id']))}/02_Leases/{int(meta['lease_id'])}/Amendments"
    if t == "leasecorrespondence":
        return f"{property_root(meta['property_name'], int(meta['property_id']))}/02_Leases/{int(meta['lease_id'])}/Tenant_Correspondence"
    return property_root(meta.get('property_name','property'), int(meta.get('property_id',0) or 0))
