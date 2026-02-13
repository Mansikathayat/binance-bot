import os
import logging
from binance.client import Client


def get_client():
    """
    Initialize and return a Binance Futures Testnet client.

    - Reads API credentials from environment variables
    - Connects to Binance Futures Testnet endpoint
    """

    # Load API credentials from environment variables
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        raise ValueError(
            "API credentials not found. Please set BINANCE_API_KEY and BINANCE_API_SECRET."
        )

    try:
        logging.info("Initializing Binance client...")

        client = Client(api_key, api_secret)

        # Set Binance Futures Testnet URL
        client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        logging.info("Binance Futures Testnet client initialized successfully.")

        return client

    except Exception as error:
        logging.error(f"Failed to initialize Binance client: {error}")
        raise
