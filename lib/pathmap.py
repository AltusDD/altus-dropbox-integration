from __future__ import annotations
from .naming import slugify

ROOT = "/Altus_Empire_Command_Center"

def property_root(property_name: str, property_id: int) -> str:
    return f"{ROOT}/01_Properties/{slugify(property_name)}-{property_id}"

def unit_root(property_name: str, property_id: int, unit_name: str, unit_id: int) -> str:
    return f"{property_root(property_name, property_id)}/01_Units/{slugify(unit_name)}-{unit_id}"

def lease_root(lease_id: int) -> str:
    return f"{ROOT}/01_Properties/02_Leases/{lease_id}"  # simple path; most customers prefer under property in practice

def canonical_folder(entity_type: str, meta: dict) -> str:
    et = entity_type.lower()
    if et == "propertyphoto":
        return f"{property_root(meta['property_name'], int(meta['property_id']))}/03_Photos"
    if et == "unitphoto":
        return f"{unit_root(meta['property_name'], int(meta['property_id']), meta['unit_name'], int(meta['unit_id']))}/01_Photos"
    if et == "leasesigned":
        return f"{property_root(meta['property_name'], int(meta['property_id']))}/02_Leases/{int(meta['lease_id'])}/Signed_Lease_Agreement"
    if et == "leaseamendment":
        return f"{property_root(meta['property_name'], int(meta['property_id']))}/02_Leases/{int(meta['lease_id'])}/Amendments"
    if et == "leasecorrespondence":
        return f"{property_root(meta['property_name'], int(meta['property_id']))}/02_Leases/{int(meta['lease_id'])}/Tenant_Correspondence"
    # default fallback
    return ROOT
