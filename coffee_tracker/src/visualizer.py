import matplotlib
matplotlib.use('Agg') # Use a non-interactive backend that doesn't require a GUI
import matplotlib.pyplot as plt
import os
import datetime
from .data_manager import get_sales_by_year, get_expenses_by_year # Assuming data_manager.py is in the same package

# Ensure plots directory exists
PLOTS_DIR = os.path.join(os.path.dirname(__file__), '..', 'plots')
os.makedirs(PLOTS_DIR, exist_ok=True)

def generate_monthly_sales_chart(year: int, sales_data: list = None):
    # If no specific sales data is provided, fetch it for the given year
    if sales_data is None:
        sales_data = get_sales_by_year(year)

    if not sales_data:
        print(f"No sales data available for the year {year} to generate a chart.")
        return None

    months = [i for i in range(1, 13)]
    monthly_totals = [0.0] * 12 # Initialize with 0.0 for float values

    for sale in sales_data:
        if sale.timestamp.year == year:
            month_index = sale.timestamp.month - 1
            monthly_totals[month_index] += sale.total_price

    active_months = [m for m, total in zip(months, monthly_totals) if total > 0]
    active_totals = [total for total in monthly_totals if total > 0]
    
    if not active_totals:
        print(f"No sales recorded with positive totals for the year {year} to generate a chart.")
        return None

    month_names = [datetime.date(year, m, 1).strftime('%b') for m in active_months]

    plt.figure(figsize=(10, 6))
    plt.bar(month_names, active_totals, color='skyblue')
    plt.xlabel("Month")
    plt.ylabel("Total Sales ($)")
    plt.title(f"Monthly Sales for {year}")
    plt.xticks(rotation=45)
    plt.tight_layout() # Adjust layout to prevent labels from being cut off

    filename = os.path.join(PLOTS_DIR, f"sales_{year}.png")
    plt.savefig(filename)
    plt.close() # Close the figure to free up memory
    print(f"Sales chart saved to {filename}")
    return filename

def generate_monthly_expenses_chart(year: int, expenses_data: list = None):
    # If no specific expenses data is provided, fetch it for the given year
    if expenses_data is None:
        expenses_data = get_expenses_by_year(year)

    if not expenses_data:
        print(f"No expenses data available for the year {year} to generate a chart.")
        return None

    months = [i for i in range(1, 13)]
    monthly_totals = [0.0] * 12 # Initialize with 0.0 for float values

    for expense in expenses_data:
        if expense.timestamp.year == year:
            month_index = expense.timestamp.month - 1
            monthly_totals[month_index] += expense.amount
            
    active_months = [m for m, total in zip(months, monthly_totals) if total > 0]
    active_totals = [total for total in monthly_totals if total > 0]

    if not active_totals:
        print(f"No expenses recorded with positive totals for the year {year} to generate a chart.")
        return None

    month_names = [datetime.date(year, m, 1).strftime('%b') for m in active_months]

    plt.figure(figsize=(10, 6))
    plt.bar(month_names, active_totals, color='salmon')
    plt.xlabel("Month")
    plt.ylabel("Total Expenses ($)")
    plt.title(f"Monthly Expenses for {year}")
    plt.xticks(rotation=45)
    plt.tight_layout()

    filename = os.path.join(PLOTS_DIR, f"expenses_{year}.png")
    plt.savefig(filename)
    plt.close()
    print(f"Expenses chart saved to {filename}")
    return filename
