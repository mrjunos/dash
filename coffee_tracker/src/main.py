import datetime
from .data_manager import save_sale, save_expense, load_sales, load_expenses, get_sales_by_year, get_expenses_by_year
from .models import Sale, Expense
from .visualizer import generate_monthly_sales_chart, generate_monthly_expenses_chart
import sys # For sys.exit()

def add_sale_interaction():
    print("\n--- Add New Sale ---")
    try:
        item_name = input("Enter item name (or type 'cancel' to return): ").strip()
        if item_name.lower() == 'cancel':
            print("Sale addition cancelled.")
            return

        while True:
            try:
                quantity_str = input("Enter quantity sold (or type 'cancel'): ").strip()
                if quantity_str.lower() == 'cancel':
                    print("Sale addition cancelled.")
                    return
                quantity = int(quantity_str)
                if quantity > 0:
                    break
                print("Quantity must be a positive integer.")
            except ValueError:
                print("Invalid input. Please enter a whole number for quantity.")

        while True:
            try:
                price_str = input("Enter price per unit (or type 'cancel'): ").strip()
                if price_str.lower() == 'cancel':
                    print("Sale addition cancelled.")
                    return
                price_per_unit = float(price_str)
                if price_per_unit >= 0:
                    break
                print("Price per unit cannot be negative.")
            except ValueError:
                print("Invalid input. Please enter a valid number for price.")

        timestamp = datetime.datetime.now()
        sale = Sale(timestamp=timestamp, item_name=item_name, quantity=quantity, price_per_unit=price_per_unit)
        save_sale(sale)
        print("Sale recorded successfully!")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def add_expense_interaction():
    print("\n--- Add New Expense ---")
    try:
        description = input("Enter expense description (or type 'cancel' to return): ").strip()
        if description.lower() == 'cancel':
            print("Expense addition cancelled.")
            return

        category = input("Enter expense category (e.g., rent, supplies, or type 'cancel'): ").strip()
        if category.lower() == 'cancel':
            print("Expense addition cancelled.")
            return
            
        while True:
            try:
                amount_str = input("Enter expense amount (or type 'cancel'): ").strip()
                if amount_str.lower() == 'cancel':
                    print("Expense addition cancelled.")
                    return
                amount = float(amount_str)
                if amount > 0:
                    break
                print("Amount must be a positive number.")
            except ValueError:
                print("Invalid input. Please enter a valid number for amount.")

        timestamp = datetime.datetime.now()
        expense = Expense(timestamp=timestamp, description=description, category=category, amount=amount)
        save_expense(expense)
        print("Expense recorded successfully!")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def view_sales_chart_interaction():
    print("\n--- View Monthly Sales Chart ---")
    while True:
        try:
            year_str = input("Enter year to generate sales chart for (e.g., 2023) (or type 'cancel'): ").strip()
            if year_str.lower() == 'cancel':
                print("Chart generation cancelled.")
                return
            year = int(year_str)
            if 1900 < year < 2200: # Basic year validation
                break
            print("Please enter a valid year (e.g., 2023).")
        except ValueError:
            print("Invalid input. Please enter a whole number for year.")
    
    # Fetch data for the chart; visualizer can also fetch but doing it here allows for checking if data exists first
    sales_for_year = get_sales_by_year(year)
    if not sales_for_year:
        print(f"No sales data found for {year}.")
        return
        
    chart_filename = generate_monthly_sales_chart(year, sales_data=sales_for_year)
    if chart_filename:
        print(f"Sales chart for {year} generated: {chart_filename}")
    else:
        print(f"Could not generate sales chart for {year}. There might be no sales with positive amounts.")


def view_expenses_chart_interaction():
    print("\n--- View Monthly Expenses Chart ---")
    while True:
        try:
            year_str = input("Enter year to generate expenses chart for (e.g., 2023) (or type 'cancel'): ").strip()
            if year_str.lower() == 'cancel':
                print("Chart generation cancelled.")
                return
            year = int(year_str)
            if 1900 < year < 2200: # Basic year validation
                break
            print("Please enter a valid year (e.g., 2023).")
        except ValueError:
            print("Invalid input. Please enter a whole number for year.")

    expenses_for_year = get_expenses_by_year(year)
    if not expenses_for_year:
        print(f"No expenses data found for {year}.")
        return

    chart_filename = generate_monthly_expenses_chart(year, expenses_data=expenses_for_year)
    if chart_filename:
        print(f"Expenses chart for {year} generated: {chart_filename}")
    else:
        print(f"Could not generate expenses chart for {year}. There might be no expenses with positive amounts.")

def main_menu():
    print("\nWelcome to the Coffee Shop Tracker!")
    while True:
        print("\nMain Menu:")
        print("1. Add New Sale")
        print("2. Add New Expense")
        print("3. View Monthly Sales Chart")
        print("4. View Monthly Expenses Chart")
        print("5. List All Sales (Debug)")
        print("6. List All Expenses (Debug)")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_sale_interaction()
        elif choice == '2':
            add_expense_interaction()
        elif choice == '3':
            view_sales_chart_interaction()
        elif choice == '4':
            view_expenses_chart_interaction()
        elif choice == '5': # Debug option
            print("\n--- All Sales ---")
            sales = load_sales()
            if not sales:
                print("No sales recorded yet.")
            for sale_entry in sales:
                print(sale_entry)
        elif choice == '6': # Debug option
            print("\n--- All Expenses ---")
            expenses = load_expenses()
            if not expenses:
                print("No expenses recorded yet.")
            for expense_entry in expenses:
                print(expense_entry)
        elif choice == '0':
            print("Exiting Coffee Shop Tracker. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    # Import necessary functions from data_manager and visualizer
    # This structure assumes main.py is in src and can import from .data_manager etc.
    # If running directly as a script from coffee_tracker/src, Python might complain about relative imports
    # To run: python -m coffee_tracker.src.main (from the directory containing coffee_tracker)
    # Or adjust imports if running coffee_tracker/src/main.py directly and handle PYTHONPATH

    # For simplicity of worker execution, we assume it's run in a context where imports work.
    main_menu()
