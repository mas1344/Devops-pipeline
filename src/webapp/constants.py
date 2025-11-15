import os

import dotenv

dotenv.load_dotenv()

BASE_URL = "https://api.coingecko.com/api/v3/simple/price"

COINMARKETCAP_SYMBOLS = "bitcoin,ethereum,solana"  


COINMARKETCAP_API_KEY = os.getenv("COINMARKETCAP_API_KEY", "")


UPDATE_FREQ_SEC = int(os.getenv("UPDATE_FREQ_SEC", 60))
