def validate_symbol(symbol: str):
    if not symbol:
        raise ValueError("Symbol empty nahi ho sakta")

def validate_side(side: str):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side BUY ya SELL hona chahiye")

def validate_order_type(order_type: str):
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type MARKET ya LIMIT hona chahiye")

def validate_quantity(quantity: float):
    if quantity <= 0:
        raise ValueError("Quantity zero se zyada honi chahiye")

def validate_price(price: float):
    if price <= 0:
        raise ValueError("Price zero se zyada honi chahiye")
