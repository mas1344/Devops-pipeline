from typing import Any

import requests

from webapp.constants import BASE_URL, COINMARKETCAP_API_KEY, COINMARKETCAP_SYMBOLS


def get_response() -> requests.Response:
    try:
        response = requests.get(
            url=BASE_URL,
            headers={
                "Accept": "application/json",
                "X-CMC_PRO_API_KEY": COINMARKETCAP_API_KEY,
            },
            params={"symbol": COINMARKETCAP_SYMBOLS},
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


def transform(data: dict[str, Any]) -> dict[str, Any]:
    try:
        coin_data = next(iter(data["data"].values()))
        crypto_data = next(iter(coin_data))
        quote_dict = crypto_data["quote"]
        base_currency = next(iter(quote_dict))
        quote_data = quote_dict[base_currency]

        return {
            "symbol": crypto_data.get("symbol"),
            "last_updated": quote_data.get("last_updated"),
            "base_currency": base_currency,
            "price": quote_data.get("price"),
            "circulating_supply": crypto_data.get("circulating_supply"),
            "total_supply": crypto_data.get("total_supply"),
            "market_cap": quote_data.get("market_cap"),
            "market_cap_dominance": quote_data.get("market_cap_dominance"),
            "fully_diluted_market_cap": quote_data.get("fully_diluted_market_cap"),
            "percent_change_1h": quote_data.get("percent_change_1h"),
            "percent_change_24h": quote_data.get("percent_change_24h"),
            "percent_change_7d": quote_data.get("percent_change_7d"),
            "percent_change_30d": quote_data.get("percent_change_30d"),
            "percent_change_60d": quote_data.get("percent_change_60d"),
            "percent_change_90d": quote_data.get("percent_change_90d"),
            "volume_24h": quote_data.get("volume_24h"),
            "volume_change_24h": quote_data.get("volume_change_24h"),
            "cmc_rank": crypto_data.get("cmc_rank"),
        }

    except (StopIteration, KeyError, TypeError, AttributeError) as e:
        raise RuntimeError(f"Invalid API response structure: {e}") from e


def get_crypto_data() -> dict[str, Any]:
    json_data = get_json_data()
    return transform(json_data)
