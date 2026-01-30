from binance.client import Client

# ⚠️ Yahan Binance Futures TESTNET ki keys daalo
API_KEY = "lRL6szV3bvYPMp0nkRwBd0Mho4c0wDdPSW0NSsHeLRD0o4hK6ySrBeDSgDDBaDk8"
API_SECRET = "PBgg457RyuPnkngeFRgRk1c335gRCWpS3TmyAiLsVmWq1zGZwu5o5fdbo58K6zAa"

def get_client():
    """
    Binance Futures Testnet client return karta hai
    """
    client = Client(API_KEY, API_SECRET)

    # TESTNET endpoint (real money safe)
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    return client
