import json
import types
from projects.flask_api.app import create_app

def test_health():
    app = create_app()
    client = app.test_client()
    resp = client.get('/health')
    assert resp.status_code == 200
    assert resp.get_json()['status'] == 'ok'

def test_sum():
    app = create_app()
    client = app.test_client()
    resp = client.post('/sum', json={'nums':[1,2,3.5]})
    assert resp.status_code == 200
    assert resp.get_json()['total'] == 6.5
