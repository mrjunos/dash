import unittest
import datetime
from coffee_tracker.src.models import Sale, Expense # Adjust import based on how tests will be run (e.g. from project root)

class TestModels(unittest.TestCase):

    def test_sale_creation(self):
        timestamp = datetime.datetime.now()
        sale = Sale(timestamp, "Coffee", 2, 2.5)
        self.assertEqual(sale.item_name, "Coffee")
        self.assertEqual(sale.quantity, 2)
        self.assertEqual(sale.price_per_unit, 2.5)
        self.assertEqual(sale.total_price, 5.0)
        self.assertEqual(sale.timestamp, timestamp)

    def test_sale_invalid_quantity(self):
        with self.assertRaises(ValueError):
            Sale(datetime.datetime.now(), "Coffee", 0, 2.5)
        with self.assertRaises(ValueError):
            Sale(datetime.datetime.now(), "Coffee", -1, 2.5)

    def test_sale_invalid_price(self):
        with self.assertRaises(ValueError):
            Sale(datetime.datetime.now(), "Coffee", 1, -0.5)

    def test_expense_creation(self):
        timestamp = datetime.datetime.now()
        expense = Expense(timestamp, "Rent", "Overhead", 500.0)
        self.assertEqual(expense.description, "Rent")
        self.assertEqual(expense.category, "Overhead")
        self.assertEqual(expense.amount, 500.0)
        self.assertEqual(expense.timestamp, timestamp)

    def test_expense_invalid_amount(self):
        with self.assertRaises(ValueError):
            Expense(datetime.datetime.now(), "Rent", "Overhead", 0)
        with self.assertRaises(ValueError):
            Expense(datetime.datetime.now(), "Rent", "Overhead", -100)

if __name__ == '__main__':
    unittest.main()
