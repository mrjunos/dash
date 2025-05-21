import datetime

class Sale:
    def __init__(self, timestamp: datetime.datetime, item_name: str, quantity: int, price_per_unit: float):
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if price_per_unit < 0:
            raise ValueError("Price per unit cannot be negative.")

        self.timestamp = timestamp
        self.item_name = item_name
        self.quantity = quantity
        self.price_per_unit = price_per_unit
        self.total_price = quantity * price_per_unit

    def __repr__(self):
        return f"Sale(timestamp={self.timestamp!r}, item_name={self.item_name!r}, quantity={self.quantity!r}, price_per_unit={self.price_per_unit!r}, total_price={self.total_price!r})"

class Expense:
    def __init__(self, timestamp: datetime.datetime, description: str, category: str, amount: float):
        if amount <= 0:
            raise ValueError("Expense amount must be positive.")

        self.timestamp = timestamp
        self.description = description
        self.category = category
        self.amount = amount

    def __repr__(self):
        return f"Expense(timestamp={self.timestamp!r}, description={self.description!r}, category={self.category!r}, amount={self.amount!r})"
