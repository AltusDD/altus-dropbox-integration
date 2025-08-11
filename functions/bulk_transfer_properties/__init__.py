
import json
import azure.functions as func
from .transfer_logic import do_transfer

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        body = req.get_json()
    except Exception:
        return func.HttpResponse('Invalid JSON', status_code=400)

    from_owner = body.get('from_owner') or {}
    to_owner   = body.get('to_owner') or {}
    properties = body.get('properties') or []
    dry        = bool(body.get('dry_run') or False)

    if not properties:
        return func.HttpResponse('Provide properties[]', status_code=400)

    results = []
    for p in properties:
        res = do_transfer(from_owner, to_owner, p, dry)
        results.append(res)

    return func.HttpResponse(json.dumps({'ok': True, 'results': results}), mimetype='application/json')
