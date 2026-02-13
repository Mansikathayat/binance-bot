def validate_symbol(symbol: str):
    """
    Validate trading symbol (e.g., BTCUSDT)
    """
    if not symbol:
        raise ValueError("Symbol is required")

    if not isinstance(symbol, str):
        raise ValueError("Symbol must be a string")

    # Basic format check (letters + numbers only)
    if not symbol.isalnum():
        raise ValueError("Invalid symbol format (only letters and numbers allowed)")


def validate_side(side: str):
    """
    Validate order side (BUY or SELL)
    """
    if not side:
        raise ValueError("Side is required")

    side = side.upper()

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be either BUY or SELL")


def validate_order_type(order_type: str):
    """
    Validate order type (MARKET or LIMIT)
    """
    if not order_type:
        raise ValueError("Order type is required")

    order_type = order_type.upper()

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be either MARKET or LIMIT")


def validate_quantity(quantity: float):
    """
    Validate order quantity
    """
    if quantity is None:
        raise ValueError("Quantity is required")

    if not isinstance(quantity, (int, float)):
        raise ValueError("Quantity must be a number")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")


def validate_price(price: float):
    """
    Validate limit price
    """
    if price is None:
        raise ValueError("Price is required for LIMIT orders")

    if not isinstance(price, (int, float)):
        raise ValueError("Price must be a number")

    if price <= 0:
        raise ValueError("Price must be greater than 0")
