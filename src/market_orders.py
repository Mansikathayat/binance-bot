import logging

def place_market_order(client, symbol, side, quantity):
    """
    Market order: turant execute hota hai
    """
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logging.info(f"MARKET order placed: {order}")
        return order

    except Exception as error:
        logging.error(f"MARKET order failed: {error}")
        raise
