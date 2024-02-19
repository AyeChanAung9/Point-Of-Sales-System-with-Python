import unittest
from unittest.mock import patch
from models.item import Item

item_data = {
    'item_id': 1,
    'product_code': 'ABC123',
    'name': 'Sample Item',
            'price': '10.99',
            'reorder': '5',
            'category_id': 1,
            'category_name': 'Sample Category',
            'cost_price': '8.99',
}


class TestItem(unittest.TestCase):

    def test_valid_item_creation(self):

        with patch('other.validations.validate_code', return_value='ABC123'), \
                patch('other.validations.validate_non_empty_string', return_value='Sample Item'), \
                patch('other.validations.validate_price', return_value='10.99'), \
                patch('other.validations.validate_number', return_value='5'):
            item = Item(**item_data)

        self.assertEqual(item.item_id, 1)
        self.assertEqual(item.product_code, 'ABC123')
        self.assertEqual(item.name, 'Sample Item')
        self.assertEqual(item.price, '10.99')
        self.assertEqual(item.reorder, '5')
        self.assertEqual(item.category_id, 1)
        self.assertEqual(item.category_name, 'Sample Category')
        self.assertEqual(item.cost_price, '8.99')

    def test_invalid_item_creation(self):
        # Invalid item creation with invalid product code
        item_data = {'product_code': 'InvalidProductCode'}
        with self.assertRaises(ValueError):
            Item(**item_data)

        # Invalid item creation with empty name
        item_data = {'name': ''}
        with self.assertRaises(ValueError):
            Item(**item_data)

        # Invalid item creation with negative price
        item_data = {'price': '-5.99'}
        with self.assertRaises(ValueError):
            Item(**item_data)

        # Invalid item creation with non-numeric reorder
        item_data = {'reorder': 'NotANumber'}
        with self.assertRaises(ValueError):
            Item(**item_data)

    def test_is_modify_method_new_item(self):
        # Test is_modify method for a new item

        item = Item(**item_data)
        self.assertTrue(item.is_modify())


if __name__ == '__main__':
    unittest.main()
