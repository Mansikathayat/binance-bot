import os
from binance.client import Client

# ⚠️ Yahan Binance Futures TESTNET ki keys daalo
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET =  os.getenv("BINANCE_API_SECRET")
def get_client():
    """
    Binance Futures Testnet client return karta hai
    """
    client = Client(API_KEY, API_SECRET)

    # TESTNET endpoint (real money safe)
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    return client
