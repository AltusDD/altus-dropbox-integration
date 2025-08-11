
import os, json
import azure.functions as func
import httpx

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_SERVICE_ROLE_KEY')

def _hdrs():
    return {'apikey': SUPABASE_KEY, 'Authorization': f'Bearer {SUPABASE_KEY}'}

def main(req: func.HttpRequest) -> func.HttpResponse:
    entity_type = req.params.get('entity_type')
    entity_id   = req.params.get('entity_id')

    params = {'select': '*', 'order': 'entity_type.asc,entity_id.asc'}
    if entity_type:
        params['entity_type'] = f'eq.{entity_type}'
    if entity_id:
        params['entity_id'] = f'eq.{entity_id}'

    r = httpx.get(f"{SUPABASE_URL}/rest/v1/vw_missing_documents_audit", headers=_hdrs(), params=params, timeout=30.0)
    if r.status_code != 200:
        return func.HttpResponse(f"Supabase error: {r.status_code} {r.text}", status_code=500)

    return func.HttpResponse(json.dumps({'ok': True, 'missing': r.json()}), mimetype='application/json')
