import unittest
from models.item_receive_detail import ItemReceiveDetail
from typing import Dict, Any


class TestItemReceiveDetail(unittest.TestCase):
    def setUp(self):

        self.valid_data: Dict[str, Any] = {
            'item_receive_details_id': 1,
            'item_receive_id': 1001,
            'item_id': 1,
            'product_code': 'ABC123',
            'name': 'Sample Item',
            'price': '10.99',
            'reorder': '5',
            'category_id': 1,
            'category_name': 'Sample Category',
            'cost_price': '8.99',
            'qty': 5
        }

        self.invalid_data: Dict[str, Any] = {
            'item_receive_details_id': 'invalid_id',  # Invalid ID
            'item_receive_id': 'invalid_item_receive_id',  # Invalid item_receive_id
            'item_id': 1,
            'product_code': 'ABC123',
            'name': 'Sample Item',
            'price': '10.99',
            'reorder': '5',
            'category_id': 1,
            'category_name': 'Sample Category',
            'cost_price': '8.99',
            'qty': -5  # Negative qty
        }

    def test_valid_data(self):
        item_receive_detail = ItemReceiveDetail(**self.valid_data)
        self.assertEqual(item_receive_detail.item_receive_details_id,
                         self.valid_data['item_receive_details_id'])
        self.assertEqual(item_receive_detail.item_receive_id,
                         self.valid_data['item_receive_id'])
        self.assertEqual(item_receive_detail.item_id,
                         self.valid_data['item_id'])
        self.assertEqual(item_receive_detail.product_code,
                         self.valid_data['product_code'])
        self.assertEqual(item_receive_detail.name,
                         self.valid_data['name'])
        self.assertEqual(item_receive_detail.price,
                         self.valid_data['price'])
        self.assertEqual(item_receive_detail.reorder,
                         self.valid_data['reorder'])
        self.assertEqual(item_receive_detail.category_id,
                         self.valid_data['category_id'])
        self.assertEqual(item_receive_detail.qty, self.valid_data['qty'])

    def test_invalid_data(self):
        with self.assertRaises(ValueError):
            ItemReceiveDetail(**self.invalid_data)


if __name__ == '__main__':
    unittest.main()
