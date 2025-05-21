import csv
import datetime
import os
from .models import Sale, Expense # Assuming models.py is in the same directory

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
SALES_FILE = os.path.join(DATA_DIR, 'sales.csv')
EXPENSES_FILE = os.path.join(DATA_DIR, 'expenses.csv')

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

def _ensure_file_exists(filepath, headers):
    if not os.path.exists(filepath):
        with open(filepath, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headers)

def save_sale(sale: Sale):
    _ensure_file_exists(SALES_FILE, ['timestamp', 'item_name', 'quantity', 'price_per_unit', 'total_price'])
    with open(SALES_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            sale.timestamp.isoformat(),
            sale.item_name,
            sale.quantity,
            sale.price_per_unit,
            sale.total_price
        ])

def load_sales() -> list[Sale]:
    sales = []
    if not os.path.exists(SALES_FILE):
        return sales
    with open(SALES_FILE, 'r', newline='') as f:
        reader = csv.reader(f)
        header = next(reader, None) # Skip header
        if not header: # empty file
            return sales
        for row in reader:
            if not row: # skip empty rows if any
                continue
            try:
                sale = Sale(
                    timestamp=datetime.datetime.fromisoformat(row[0]),
                    item_name=row[1],
                    quantity=int(row[2]),
                    price_per_unit=float(row[3])
                    # total_price is calculated in Sale constructor
                )
                sales.append(sale)
            except (IndexError, ValueError) as e:
                print(f"Skipping malformed row in sales.csv: {row}. Error: {e}")
    return sales

def save_expense(expense: Expense):
    _ensure_file_exists(EXPENSES_FILE, ['timestamp', 'description', 'category', 'amount'])
    with open(EXPENSES_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            expense.timestamp.isoformat(),
            expense.description,
            expense.category,
            expense.amount
        ])

def load_expenses() -> list[Expense]:
    expenses = []
    if not os.path.exists(EXPENSES_FILE):
        return expenses
    with open(EXPENSES_FILE, 'r', newline='') as f:
        reader = csv.reader(f)
        header = next(reader, None) # Skip header
        if not header: # empty file
            return expenses
        for row in reader:
            if not row: # skip empty rows if any
                continue
            try:
                expense = Expense(
                    timestamp=datetime.datetime.fromisoformat(row[0]),
                    description=row[1],
                    category=row[2],
                    amount=float(row[3])
                )
                expenses.append(expense)
            except (IndexError, ValueError) as e:
                print(f"Skipping malformed row in expenses.csv: {row}. Error: {e}")
    return expenses

def get_sales_by_month(year: int, month: int) -> list[Sale]:
    sales = load_sales()
    return [
        sale for sale in sales
        if sale.timestamp.year == year and sale.timestamp.month == month
    ]

def get_expenses_by_month(year: int, month: int) -> list[Expense]:
    expenses = load_expenses()
    return [
        expense for expense in expenses
        if expense.timestamp.year == year and expense.timestamp.month == month
    ]

def get_sales_by_year(year: int) -> list[Sale]:
    sales = load_sales()
    return [
        sale for sale in sales
        if sale.timestamp.year == year
    ]

def get_expenses_by_year(year: int) -> list[Expense]:
    expenses = load_expenses()
    return [
        expense for expense in expenses
        if expense.timestamp.year == year
    ]
