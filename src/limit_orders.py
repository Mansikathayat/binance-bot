import logging

def place_limit_order(client, symbol, side, quantity, price):
    """
    Limit order: specified price pe trigger hota hai
    """
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logging.info(f"LIMIT order placed: {order}")
        return order

    except Exception as error:
        logging.error(f"LIMIT order failed: {error}")
        raise
