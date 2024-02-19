import unittest

from models.damage_loss import DamageLoss


class TestDamageLoss(unittest.TestCase):

    def test_valid_damage_loss_creation(self):
        damage_loss_data = {
            'damage_loss_id': 1,
            'voucher_no': 'DL123',
            'tran_date': '2023-01-01',
            'total_items': 5,
            'user_id': 2,
        }

        damage_loss = DamageLoss(**damage_loss_data)

        self.assertEqual(damage_loss.damage_loss_id, 1)
        self.assertEqual(damage_loss.voucher_no, 'DL123')
        self.assertEqual(damage_loss.tran_date, '2023-01-01')
        self.assertEqual(damage_loss.total_items, 5)
        self.assertEqual(damage_loss.user_id, 2)

    def test_to_tuple_db_method(self):
        damage_loss_data = {
            'damage_loss_id': 1,
            'voucher_no': 'DL123',
            'tran_date': '2023-01-01',
            'total_items': 5,
            'user_id': 2,
        }

        damage_loss = DamageLoss(**damage_loss_data)
        result = damage_loss.to_tuple_db()

        expected_result = ('DL123', '2023-01-01', 5, 2, 1)
        self.assertEqual(result, expected_result)

    def test_invalid_damage_loss_creation(self):
        invalid_damage_loss_data = {
            'damage_loss_id': -1,  # Invalid damage_loss_id
            'voucher_no': 'invalid',  # Invalid voucher_no
            'tran_date': 'invalid',  # Invalid tran_date
            'total_items': -5,  # Invalid total_items
            'user_id': 0,  # Invalid user_id
        }

        with self.assertRaises(ValueError):
            DamageLoss(**invalid_damage_loss_data)


if __name__ == '__main__':
    unittest.main()
