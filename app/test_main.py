import unittest
from datetime import date
from unittest.mock import patch
from app.main import outdated_products


class TestOutdatedProducts(unittest.TestCase):

    @patch('datetime.date')
    def test_outdated_products(self, mock_date):
        # Mock today's date to be February 2, 2022
        mock_date.today.return_value = date(2022, 2, 2)

        # Test case with various products
        products = [
            {
                "name": "salmon",
                "expiration_date": date(2022, 2, 10),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": date(2022, 2, 5),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": date(2022, 2, 1),
                "price": 160
            },
            {
                "name": "milk",
                "expiration_date": date(2022, 2, 2),  # Expires today
                "price": 50
            }
        ]

        result = outdated_products(products)
        self.assertEqual(result, ["duck"])

        # Additional test case with no outdated products
        products_no_outdated = [
            {
                "name": "beef",
                "expiration_date": date(2022, 2, 15),
                "price": 250
            },
            {
                "name": "pork",
                "expiration_date": date(2022, 2, 8),
                "price": 180
            }
        ]

        result_no_outdated = outdated_products(products_no_outdated)
        self.assertEqual(result_no_outdated, [])