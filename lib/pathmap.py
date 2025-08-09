from __future__ import annotations
from .naming import slugify

ROOT = "/Altus_Empire_Command_Center"

def property_root(property_name: str, property_id: int) -> str:
    return f"{ROOT}/01_Properties/{slugify(property_name)}-{property_id}"

def unit_root(property_name: str, property_id: int, unit_name: str, unit_id: int) -> str:
    return f"{property_root(property_name, property_id)}/01_Units/{slugify(unit_name)}-{unit_id}"

def lease_root(property_name: str, property_id: int, lease_id: int) -> str:
    return f"{property_root(property_name, property_id)}/02_Leases/{lease_id}"

def deal_room_root() -> str:
    return f"{ROOT}/04_Deal_Room"

def upload_target(entity_type: str, meta: dict) -> str:
    et = (entity_type or "").strip()
    if et == "Inspection":
        if meta.get("unit_name") and meta.get("unit_id"):
            return f"{unit_root(meta['property_name'], meta['property_id'], meta['unit_name'], meta['unit_id'])}/02_Inspections"
        return f"{property_root(meta['property_name'], meta['property_id'])}/04_Inspections"
    if et == "UnitPhoto":
        return f"{unit_root(meta['property_name'], meta['property_id'], meta['unit_name'], meta['unit_id'])}/01_Photos"
    if et == "PropertyPhoto":
        return f"{property_root(meta['property_name'], meta['property_id'])}/03_Photos"
    if et == "LeaseSigned":
        return f"{lease_root(meta['property_name'], meta['property_id'], meta['lease_id'])}/Signed_Lease_Agreement"
    if et == "LeaseAmendment":
        return f"{lease_root(meta['property_name'], meta['property_id'], meta['lease_id'])}/Amendments"
    if et == "LeaseCorrespondence":
        return f"{lease_root(meta['property_name'], meta['property_id'], meta['lease_id'])}/Tenant_Correspondence"
    if et == "Deal_Room":
        return deal_room_root()
    raise ValueError(f"Unsupported entity_type: {entity_type}")
