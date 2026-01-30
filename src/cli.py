import argparse
import logging

from logging_config import setup_logger
from client import get_client
from validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from market_orders import place_market_order
from limit_orders import place_limit_order

def main():
    # 1️⃣ Logging start
    setup_logger()

    # 2️⃣ CLI arguments
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("symbol", help="Trading symbol (e.g. BTCUSDT)")
    parser.add_argument("side", help="BUY or SELL")
    parser.add_argument("order_type", help="MARKET or LIMIT")
    parser.add_argument("quantity", type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price (LIMIT only)")

    args = parser.parse_args()

    try:
        # 3️⃣ Validation
        validate_symbol(args.symbol)
        validate_side(args.side)
        validate_order_type(args.order_type)
        validate_quantity(args.quantity)

        # 4️⃣ Binance client
        client = get_client()

        # 5️⃣ Order routing
        if args.order_type == "MARKET":
            order = place_market_order(
                client, args.symbol, args.side, args.quantity
            )

        elif args.order_type == "LIMIT":
            if args.price is None:
                raise ValueError("LIMIT order ke liye price zaroori hai")

            validate_price(args.price)

            order = place_limit_order(
                client, args.symbol, args.side, args.quantity, args.price
            )

        # 6️⃣ Output
        print("✅ Order Successful")
        print("Order ID:", order["orderId"])
        print("Status:", order["status"])

    except Exception as error:
        logging.error(error)
        print("❌ Error:", error)

if __name__ == "__main__":
    main()
