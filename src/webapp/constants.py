import os

import dotenv

dotenv.load_dotenv()

BASE_URL = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"

COINMARKETCAP_API_KEY = os.getenv("COINMARKETCAP_API_KEY", "")
print("🔑 API KEY length:", len(COINMARKETCAP_API_KEY) if COINMARKETCAP_API_KEY else None)
COINMARKETCAP_SYMBOLS = os.getenv("COINMARKETCAP_SYMBOLS", "BTC")

UPDATE_FREQ_SEC = int(os.getenv("UPDATE_FREQ_SEC", 60))
