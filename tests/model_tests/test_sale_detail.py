import unittest
from models.sale_detail import SaleDetail


class TestSaleDetail(unittest.TestCase):

    def test_valid_sale_detail_creation(self):
        sale_detail_data = {
            'sale_detail_id': 1,
            'sale_id': 2,
            'item_id': 3,
            'product_code': 'P123',
            'name': 'Item1',
            'reorder': 5,
            'category_id': 4,
            'qty': 5,
            'price': 50.0,
            'category_name': 'Cosmetics',
        }

        sale_detail = SaleDetail(**sale_detail_data)

        self.assertEqual(sale_detail.sale_detail_id, 1)
        self.assertEqual(sale_detail.sale_id, 2)
        self.assertEqual(sale_detail.item_id, 3)
        self.assertEqual(sale_detail.product_code, 'P123')
        self.assertEqual(sale_detail.name, 'Item1')
        self.assertEqual(sale_detail.reorder, 5)
        self.assertEqual(sale_detail.category_id, 4)
        self.assertEqual(sale_detail.qty, 5)
        self.assertEqual(sale_detail.price, 50.0)

    def test_to_tuple_db_method(self):
        sale_detail_data = {
            'sale_detail_id': 1,
            'sale_id': 2,
            'item_id': 3,
            'product_code': 'P123',
            'name': 'Item1',
            'category_name': 'Cosmetics',
            'reorder': 5,
            'category_id': 4,
            'qty': 5,
            'price': 50.0
        }

        sale_detail = SaleDetail(**sale_detail_data)
        result = sale_detail.to_tuple_db(2)

        expected_result = (1, 2, 3, 5, 50.0)
        self.assertEqual(result, expected_result)

    def test_invalid_sale_detail_creation(self):
        invalid_sale_detail_data = {
            'sale_detail_id': -1,  # Invalid sale_detail_id
            'sale_id': 0,  # Invalid sale_id
            'item_id': -3,
            'product_code': 'P123',
            'name': 'Item1',
            'reorder': 5,
            'category_id': 4,
            'qty': -5,  # Invalid qty
            'price': -50.0  # Invalid price
        }

        with self.assertRaises(ValueError):
            SaleDetail(**invalid_sale_detail_data)


if __name__ == '__main__':
    unittest.main()
