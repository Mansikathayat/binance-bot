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
    # 1️⃣ Initialize logging
    setup_logger()

    # 2️⃣ CLI arguments
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("symbol", help="Trading symbol (e.g. BTCUSDT)")
    parser.add_argument("side", help="Order side: BUY or SELL")
    parser.add_argument("order_type", help="Order type: MARKET or LIMIT")
    parser.add_argument("quantity", type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price (required for LIMIT orders)")

    args = parser.parse_args()

    try:
        # 3️⃣ Normalize input (IMPORTANT)
        args.side = args.side.upper()
        args.order_type = args.order_type.upper()

        # 4️⃣ Validation
        validate_symbol(args.symbol)
        validate_side(args.side)
        validate_order_type(args.order_type)
        validate_quantity(args.quantity)

        # 5️⃣ Print Order Request Summary
        print("\n===== ORDER REQUEST =====")
        print(f"Symbol   : {args.symbol}")
        print(f"Side     : {args.side}")
        print(f"Type     : {args.order_type}")
        print(f"Quantity : {args.quantity}")

        if args.order_type == "LIMIT":
            if args.price is None:
                raise ValueError("Price is required for LIMIT orders")

            validate_price(args.price)
            print(f"Price    : {args.price}")

        # 6️⃣ Initialize Binance client
        client = get_client()

        # 7️⃣ Route order
        if args.order_type == "MARKET":
            order = place_market_order(
                client, args.symbol, args.side, args.quantity
            )

        elif args.order_type == "LIMIT":
            order = place_limit_order(
                client, args.symbol, args.side, args.quantity, args.price
            )

        else:
            raise ValueError("Invalid order type. Use MARKET or LIMIT")

        # 8️⃣ Print Response
        print("\n===== ORDER RESPONSE =====")
        print(f"Order ID      : {order.get('orderId')}")
        print(f"Status        : {order.get('status')}")
        print(f"Executed Qty  : {order.get('executedQty', 'N/A')}")
        print(f"Avg Price     : {order.get('avgPrice', 'N/A')}")

        print("\n✅ Order placed successfully!")

        # 9️⃣ Log success
        logging.info(
            f"Order placed | Symbol={args.symbol} | Side={args.side} | "
            f"Type={args.order_type} | Quantity={args.quantity} | "
            f"Price={args.price} | Response={order}"
        )

    except Exception as error:
        # 🔟 Log error
        logging.error(f"Order failed: {error}")

        # User-friendly output
        print("\n❌ Order failed!")
        print(f"Reason: {error}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("\n❌ Unexpected error occurred!")
        print(f"Details: {e}")
