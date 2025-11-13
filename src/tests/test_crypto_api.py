from webapp.crypto_api import transform, get_response
import types

def test_transform():
    sample = {
        "data": {"BTC": [{"quote": {"USD": {"price": 12345.67}}}]}  
    }
    assert transform(sample) == 12345.67

def test_response(monkeypatch):
    class DummyResp:
        status_code = 200
        url = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest?symbol=BTC"
        def raise_for_status(self): pass
        def json(self):
            return {"data": {"BTC": [{"quote": {"USD": {"price": 12345.67}}}]}}
    def fake_get(url, headers, params, timeout):
        return DummyResp()

    monkeypatch.setattr("webapp.crypto_api.requests.get", fake_get)

    resp = get_response()
    assert resp.status_code == 200
    assert transform(resp.json()) == 12345.67
