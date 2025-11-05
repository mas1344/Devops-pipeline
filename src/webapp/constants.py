import os

import dotenv

dotenv.load_dotenv()

BASE_URL = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"

COINMARKETCAP_API_KEY = os.getenv("COINMARKETCAP_API_KEY", "")
COINMARKETCAP_SYMBOLS = os.getenv("COINMARKETCAP_SYMBOLS", "BTC")

UPDATE_FREQ_SEC = int(os.getenv("UPDATE_FREQ_SEC", 60))
