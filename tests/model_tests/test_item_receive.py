import unittest
from models.item_receive import ItemReceive


class TestItemReceive(unittest.TestCase):
    def setUp(self):

        self.valid_data = {
            'item_receive_id': 1,
            'voucher_no': 'VR123',
            'tran_date': '2023-01-01',
            'total_items': 10,
            'user_id': 1001
        }

        self.invalid_data = {
            'item_receive_id': 'invalid_id',  # Invalid ID
            'voucher_no': '',  # Empty voucher_no
            'tran_date': 'invalid_date',  # Invalid date format
            'total_items': -5,  # Negative total_items
            'user_id': 'invalid_user_id'  # Invalid user_id
        }

    def test_valid_data(self):
        item_receive = ItemReceive(**self.valid_data)
        self.assertEqual(item_receive.item_receive_id,
                         self.valid_data['item_receive_id'])
        self.assertEqual(item_receive.voucher_no,
                         self.valid_data['voucher_no'])
        self.assertEqual(item_receive.tran_date, self.valid_data['tran_date'])
        self.assertEqual(item_receive.total_items,
                         self.valid_data['total_items'])
        self.assertEqual(item_receive.user_id, self.valid_data['user_id'])

    def test_invalid_data(self):
        with self.assertRaises(ValueError):
            ItemReceive(**self.invalid_data)


if __name__ == '__main__':
    unittest.main()
