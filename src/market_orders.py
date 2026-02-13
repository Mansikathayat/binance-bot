import logging


def place_market_order(client, symbol, side, quantity):
    """
    Place a MARKET order on Binance Futures Testnet.
    Executes immediately at the best available market price.
    """

    try:
        logging.info(
            f"Placing MARKET order | Symbol={symbol} | Side={side} | Quantity={quantity}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logging.info(
            f"MARKET order successful | OrderId={order.get('orderId')} | Status={order.get('status')} | Response={order}"
        )

        return order

    except Exception as error:
        logging.error(
            f"MARKET order failed | Symbol={symbol} | Side={side} | Quantity={quantity} | Error={error}"
        )
        raise
