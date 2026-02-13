import logging


def place_limit_order(client, symbol, side, quantity, price):
    """
    Place a LIMIT order on Binance Futures Testnet.

    A LIMIT order is executed only at the specified price or better.
    The order will remain open until it is filled or canceled.
    """

    try:
        logging.info(
            f"Placing LIMIT order | Symbol={symbol} | Side={side} | Quantity={quantity} | Price={price}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"  # Good Till Cancelled
        )

        logging.info(
            f"LIMIT order successful | OrderId={order.get('orderId')} | Status={order.get('status')} | Response={order}"
        )

        return order

    except Exception as error:
        logging.error(
            f"LIMIT order failed | Symbol={symbol} | Side={side} | Quantity={quantity} | Price={price} | Error={error}"
        )
        raise
