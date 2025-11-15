from webapp.crypto_api import transform, get_response
import types


def test_transform_single_coin():
 
    fake_data = {
        "bitcoin": {
            "usd": 103929.32609335119,
            "usd_24h_change": -1.23,
            "last_updated_at": 1731580800, 
            "usd_market_cap": 123456789.0,
            "usd_24h_vol": 9876543.0,
        }
    }

    result = transform(fake_data)


    assert isinstance(result, list)
    assert len(result) == 1

    coin = result[0]
    assert coin["symbol"] == "BTC"
    assert coin["base_currency"] == "USD"
    assert coin["price"] == fake_data["bitcoin"]["usd"]
    assert coin["percent_change_24h"] == fake_data["bitcoin"]["usd_24h_change"]
    assert coin["market_cap"] == fake_data["bitcoin"]["usd_market_cap"]
    assert coin["volume_24h"] == fake_data["bitcoin"]["usd_24h_vol"]
    assert coin["last_updated"] is not None  


def test_response_and_transform(monkeypatch):
    class DummyResp:
        status_code = 200
        url = "https://example.com"

        def raise_for_status(self):
            pass

        def json(self):
           
            return {
                "bitcoin": {
                    "usd": 12345.67,
                    "usd_24h_change": 2.5,
                    "last_updated_at": 1731580800,
                    "usd_market_cap": 111.0,
                    "usd_24h_vol": 222.0,
                }
            }

    def fake_get(url, params=None, timeout=10):
        return DummyResp()

    monkeypatch.setattr("webapp.crypto_api.requests.get", fake_get)

    resp = get_response()
    assert resp.status_code == 200

    result = transform(resp.json())
    assert isinstance(result, list)
    assert len(result) == 1

    coin = result[0]
    assert coin["symbol"] == "BTC"
    assert coin["price"] == 12345.67
