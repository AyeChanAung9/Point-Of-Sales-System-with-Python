import unittest
from models.sale import Sale


class TestSale(unittest.TestCase):

    def test_valid_sale_creation(self):
        sale_data = {
            'sale_id': 1,
            'voucher_no': '123ABC',
            'tran_date': '2023-01-01',
            'total_items': 5,
            'user_id': 2,
            'discount': 10.0,
            'total_amount': 90.0,
            'discount_percentage': 5,
            'payment': 'Credit Card',
        }

        sale = Sale(**sale_data)

        self.assertEqual(sale.sale_id, 1)
        self.assertEqual(sale.voucher_no, '123ABC')
        self.assertEqual(sale.tran_date, '2023-01-01')
        self.assertEqual(sale.total_items, 5)
        self.assertEqual(sale.user_id, 2)
        self.assertEqual(sale.discount, 10.0)
        self.assertEqual(sale.total_amount, 90.0)
        self.assertEqual(sale.discount_percentage, 5)
        self.assertEqual(sale.payment, 'Credit Card')

    def test_to_tuple_db_method(self):
        sale_data = {
            'sale_id': 1,
            'voucher_no': '123ABC',
            'tran_date': '2023-01-01',
            'total_items': 5,
            'user_id': 2,
            'discount': 10.0,
            'total_amount': 90.0,
            'discount_percentage': 5,
            'payment': 'Credit Card',
        }

        sale = Sale(**sale_data)
        result = sale.to_tuple_db()

        expected_result = ('123ABC', '2023-01-01', 5, 2,
                           10.0, 90.0, 5, 'Credit Card', 1)
        self.assertEqual(result, expected_result)

    def test_to_tuple_db_without_id_method(self):
        sale_data = {
            'voucher_no': '123ABC',
            'tran_date': '2023-01-01',
            'total_items': 5,
            'user_id': 2,
            'discount': 10.0,
            'total_amount': 90.0,
            'discount_percentage': 5,
            'payment': 'Credit Card',
        }

        sale = Sale(**sale_data)
        result = sale.to_tuple_db_without_id()

        expected_result = ('123ABC', '2023-01-01', 5, 2,
                           10.0, 90.0, 5, 'Credit Card')
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
