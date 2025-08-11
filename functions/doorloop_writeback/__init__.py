import os, json, datetime
import azure.functions as func
import httpx

# Minimal DoorLoop client for Notes & Communications
DL_BASE = "https://app.doorloop.com/api"

def _hdrs():
    key = os.getenv("DOORLOOP_API_KEY")
    return {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}

def _post(client, path, payload):
    r = client.post(f"{DL_BASE}{path}", headers=_hdrs(), json=payload)
    return r.status_code, (r.json() if 'application/json' in r.headers.get('content-type','') else r.text)

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        body = req.get_json()
    except ValueError:
        return func.HttpResponse("Invalid JSON", status_code=400)

    prop_id = body.get("property_id")
    from_owner = body.get("from_owner_id")
    to_owner = body.get("to_owner_id")
    cutoff = body.get("cutoff_date")
    message = body.get("message") or f"Ownership transferred from {from_owner} to {to_owner} effective {cutoff}."

    if not (prop_id and from_owner and to_owner and cutoff):
        return func.HttpResponse("property_id, from_owner_id, to_owner_id, cutoff_date are required", status_code=400)

    if not os.getenv("DOORLOOP_API_KEY"):
        return func.HttpResponse("Server missing DOORLOOP_API_KEY app setting", status_code=500)

    # Build minimal payloads. DoorLoop's API may require additional fields; adjust as needed.
    note_payload = {
        "body": message,
        "propertyId": prop_id
    }
    comm_payload = {
        "channel": "system",
        "subject": "Ownership Transfer",
        "body": message,
        "propertyId": prop_id
    }

    out = {"note": None, "communication": None}
    with httpx.Client(timeout=30) as c:
        note_status, note_body = _post(c, "/notes", note_payload)
        out["note"] = {"status": note_status, "body": note_body}
        comm_status, comm_body = _post(c, "/communications", comm_payload)
        out["communication"] = {"status": comm_status, "body": comm_body}

    # We **cannot** reassign property owner via public API at this time.
    # This endpoint focuses on journaling the event into DoorLoop for audit parity.
    return func.HttpResponse(json.dumps({"ok": True, "writeback": out}), mimetype="application/json")