from typing import Any
from datetime import datetime, timezone

import requests

from webapp.constants import BASE_URL, COINMARKETCAP_SYMBOLS


# CoinGecko config
VS_CURRENCY = "usd"


ID_TO_SYMBOL = {
    "bitcoin": "BTC",
    "ethereum": "ETH",
    "solana": "SOL",
    
}


def get_response() -> requests.Response:
    """
    Call CoinGecko simple price API, e.g:
    https://api.coingecko.com/api/v3/simple/price
        ?ids=bitcoin,ethereum,solana
        &vs_currencies=usd
        &include_24hr_change=true
        &include_last_updated_at=true
    """
    try:
        response = requests.get(
            url=BASE_URL,
            params={
                "ids": COINMARKETCAP_SYMBOLS, 
                "vs_currencies": VS_CURRENCY,
                "include_24hr_change": "true",
                "include_last_updated_at": "true",
                "include_market_cap": "true",
                "include_24hr_vol": "true",
            },
            timeout=10,
        )

        response.raise_for_status()
        return response

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"API request failed: {e}") from e


def get_json_data() -> dict[str, Any]:
    response = get_response()
    try:
        return response.json()
    except requests.exceptions.JSONDecodeError as e:
        raise RuntimeError(f"Invalid JSON response: {e}") from e


def transform(data: dict[str, Any]) -> list[dict[str, Any]]:
    """
    CoinGecko 
    [
      { "symbol": "BTC", "price": ..., "percent_change_24h": ... },
      { "symbol": "ETH", ... },
      { "symbol": "SOL", ... },
    ]
    """
    try:
        results: list[dict[str, Any]] = []

        for coin_id, payload in data.items():
            symbol = ID_TO_SYMBOL.get(coin_id, coin_id.upper())
            price = payload.get(VS_CURRENCY)
            change_24h = payload.get(f"{VS_CURRENCY}_24h_change")

            last_updated_ts = payload.get("last_updated_at")
            if last_updated_ts is not None:
                last_updated = datetime.fromtimestamp(
                    last_updated_ts, tz=timezone.utc
                ).isoformat()
            else:
                last_updated = None

            result: dict[str, Any] = {
                "symbol": symbol,
                "last_updated": last_updated,
                "base_currency": VS_CURRENCY.upper(),
                "price": price,
                "percent_change_24h": change_24h,
                "market_cap": payload.get(f"{VS_CURRENCY}_market_cap"),
                "volume_24h": payload.get(f"{VS_CURRENCY}_24h_vol"),
            }

            results.append(result)

        return results

    except (KeyError, TypeError, ValueError) as e:
        raise RuntimeError(f"Invalid API response structure: {e}") from e


def get_crypto_data() -> list[dict[str, Any]]:
    json_data = get_json_data()
    return transform(json_data)
