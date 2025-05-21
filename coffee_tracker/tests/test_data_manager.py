import unittest
import os
import csv
import datetime
from coffee_tracker.src.models import Sale, Expense
from coffee_tracker.src.data_manager import (
    save_sale, load_sales, save_expense, load_expenses,
    get_sales_by_month, get_expenses_by_month,
    get_sales_by_year, get_expenses_by_year,
    DATA_DIR, SALES_FILE, EXPENSES_FILE
)

class TestDataManager(unittest.TestCase):

    def setUp(self):
        # Ensure a clean state before each test
        self.test_sales_file = os.path.join(DATA_DIR, 'test_sales.csv')
        self.test_expenses_file = os.path.join(DATA_DIR, 'test_expenses.csv')

        # Override original file paths for testing
        global SALES_FILE, EXPENSES_FILE
        self._original_sales_file = SALES_FILE
        self._original_expenses_file = EXPENSES_FILE
        SALES_FILE = self.test_sales_file
        EXPENSES_FILE = self.test_expenses_file
        
        os.makedirs(DATA_DIR, exist_ok=True)
        self.clear_test_files()

    def tearDown(self):
        self.clear_test_files()
        # Restore original file paths
        global SALES_FILE, EXPENSES_FILE
        SALES_FILE = self._original_sales_file
        EXPENSES_FILE = self._original_expenses_file
        # Attempt to remove test files if they exist
        if os.path.exists(self.test_sales_file):
            os.remove(self.test_sales_file)
        if os.path.exists(self.test_expenses_file):
            os.remove(self.test_expenses_file)

    def clear_test_files(self):
        if os.path.exists(self.test_sales_file):
            os.remove(self.test_sales_file)
        if os.path.exists(self.test_expenses_file):
            os.remove(self.test_expenses_file)

    def test_save_and_load_sales(self):
        self.assertEqual(len(load_sales()), 0) # Should be empty initially
        sale1_time = datetime.datetime(2023, 1, 15, 10, 0, 0)
        sale1 = Sale(sale1_time, "Latte", 1, 3.5)
        save_sale(sale1)
        
        sale2_time = datetime.datetime(2023, 1, 16, 11, 0, 0)
        sale2 = Sale(sale2_time, "Muffin", 2, 2.0)
        save_sale(sale2)

        sales = load_sales()
        self.assertEqual(len(sales), 2)
        self.assertEqual(sales[0].item_name, "Latte")
        self.assertEqual(sales[0].total_price, 3.5)
        self.assertEqual(sales[0].timestamp, sale1_time)
        self.assertEqual(sales[1].item_name, "Muffin")
        self.assertEqual(sales[1].quantity, 2)
        self.assertEqual(sales[1].timestamp, sale2_time)

    def test_save_and_load_expenses(self):
        self.assertEqual(len(load_expenses()), 0) # Should be empty initially
        exp1_time = datetime.datetime(2023, 2, 10, 14, 0, 0)
        expense1 = Expense(exp1_time, "Coffee Beans", "Supplies", 50.0)
        save_expense(expense1)

        exp2_time = datetime.datetime(2023, 2, 12, 10, 0, 0)
        expense2 = Expense(exp2_time, "Electricity Bill", "Utilities", 75.0)
        save_expense(expense2)

        expenses = load_expenses()
        self.assertEqual(len(expenses), 2)
        self.assertEqual(expenses[0].description, "Coffee Beans")
        self.assertEqual(expenses[0].amount, 50.0)
        self.assertEqual(expenses[0].timestamp, exp1_time)
        self.assertEqual(expenses[1].category, "Utilities")
        self.assertEqual(expenses[1].timestamp, exp2_time)

    def test_empty_files_load(self):
        # Ensure files exist but are empty (only headers)
        with open(self.test_sales_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['timestamp', 'item_name', 'quantity', 'price_per_unit', 'total_price'])
        self.assertEqual(len(load_sales()), 0)

        with open(self.test_expenses_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['timestamp', 'description', 'category', 'amount'])
        self.assertEqual(len(load_expenses()), 0)

    def test_get_sales_by_month_and_year(self):
        s1 = Sale(datetime.datetime(2023, 1, 5), "S1", 1, 1)
        s2 = Sale(datetime.datetime(2023, 1, 15), "S2", 1, 1)
        s3 = Sale(datetime.datetime(2023, 2, 5), "S3", 1, 1)
        s4 = Sale(datetime.datetime(2024, 1, 5), "S4", 1, 1)
        save_sale(s1); save_sale(s2); save_sale(s3); save_sale(s4)

        jan_2023_sales = get_sales_by_month(2023, 1)
        self.assertEqual(len(jan_2023_sales), 2)
        self.assertTrue(all(s.timestamp.year == 2023 and s.timestamp.month == 1 for s in jan_2023_sales))

        feb_2023_sales = get_sales_by_month(2023, 2)
        self.assertEqual(len(feb_2023_sales), 1)
        self.assertEqual(feb_2023_sales[0].item_name, "S3")
        
        jan_2024_sales = get_sales_by_year(2024) # Also tests get_sales_by_year
        self.assertEqual(len(jan_2024_sales), 1)
        self.assertEqual(jan_2024_sales[0].item_name, "S4")

        self.assertEqual(len(get_sales_by_month(2023, 3)), 0) # No sales in March 2023
        self.assertEqual(len(get_sales_by_year(2025)), 0) # No sales in 2025

    def test_get_expenses_by_month_and_year(self):
        e1 = Expense(datetime.datetime(2023, 1, 5), "E1", "C1", 10)
        e2 = Expense(datetime.datetime(2023, 1, 15), "E2", "C1", 10)
        e3 = Expense(datetime.datetime(2023, 2, 5), "E3", "C2", 10)
        e4 = Expense(datetime.datetime(2024, 1, 5), "E4", "C1", 10)
        save_expense(e1); save_expense(e2); save_expense(e3); save_expense(e4)

        jan_2023_expenses = get_expenses_by_month(2023, 1)
        self.assertEqual(len(jan_2023_expenses), 2)
        self.assertTrue(all(e.timestamp.year == 2023 and e.timestamp.month == 1 for e in jan_2023_expenses))

        feb_2023_expenses = get_expenses_by_month(2023, 2)
        self.assertEqual(len(feb_2023_expenses), 1)
        self.assertEqual(feb_2023_expenses[0].description, "E3")

        jan_2024_expenses = get_expenses_by_year(2024) # Also tests get_expenses_by_year
        self.assertEqual(len(jan_2024_expenses), 1)
        self.assertEqual(jan_2024_expenses[0].description, "E4")
        
        self.assertEqual(len(get_expenses_by_month(2023, 3)), 0)
        self.assertEqual(len(get_expenses_by_year(2025)), 0)

if __name__ == '__main__':
    unittest.main()
