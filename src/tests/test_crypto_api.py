from webapp.crypto_api import transform, get_response


def test_transform():
    """
    Unit test for transform function.
    
    Tests that the transform function correctly extracts and maps
    cryptocurrency data from the CoinMarketCap API response format
    into our application's expected data structure.
    """
    # Arrange: Create mock data that mirrors CoinMarketCap API response structure
    test_fake_data = {
        "data": {
            "BTC": [
                {
                    "id": 1,
                    "name": "Bitcoin",
                    "symbol": "BTC",
                    "circulating_supply": 19500000,
                    "total_supply": 21000000,
                    "cmc_rank": 1,
                    "quote": {
                        "USD": {
                            "price": 103929.32609335119,
                            "market_cap": 2000000000000,
                            "percent_change_24h": 2.5,
                            "last_updated": "2024-01-01T12:00:00.000Z"
                        }
                    }
                },
            ]
        }
    }
    
    # Act: Call the transform function with our test data
    result = transform(test_fake_data)
    
    # Assert: Verify that all expected fields are correctly extracted and mapped
    # Core cryptocurrency identification
    assert result["symbol"] == "BTC", "Symbol should be extracted correctly"
    assert result["price"] == 103929.32609335119, "Price should match USD quote price"
    
    # Supply and ranking information
    assert result["circulating_supply"] == 19500000, "Circulating supply should be mapped"
    assert result["total_supply"] == 21000000, "Total supply should be mapped"
    assert result["cmc_rank"] == 1, "CoinMarketCap rank should be preserved"
    
    # Market data
    assert result["market_cap"] == 2000000000000, "Market cap should come from USD quote"
    assert result["percent_change_24h"] == 2.5, "24h price change should be extracted"
    
    # Metadata
    assert result["last_updated"] == "2024-01-01T12:00:00.000Z", "Last updated timestamp should be preserved"

def test_response():
    response = get_response()

    assert response.status_code == 200







