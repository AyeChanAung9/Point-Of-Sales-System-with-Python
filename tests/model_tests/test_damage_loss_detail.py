import unittest
from models.damage_loss_detail import DamageLossDetail

from typing import Dict, Any


class TestDamageLossDetail(unittest.TestCase):

    def test_valid_data(self) -> None:
        valid_data: Dict[str, Any] = {
            'damage_loss_details_id': 1,
            'damage_loss_id': 1001,
            'item_id': 101,
            'product_code': 'P001',
            'name': 'Product A',
            'price': 50.0,
            'reorder': 10,
            'category_id': 201,
            'category_name': 'Cosmetics',
            'qty': 5,
            'remark': 'Damaged during transit'
        }

        damage_loss_detail = DamageLossDetail(**valid_data)
        self.assertEqual(damage_loss_detail.damage_loss_details_id,
                         valid_data['damage_loss_details_id'])
        self.assertEqual(damage_loss_detail.damage_loss_id,
                         valid_data['damage_loss_id'])
        self.assertEqual(damage_loss_detail.item_id, valid_data['item_id'])
        self.assertEqual(damage_loss_detail.product_code,
                         valid_data['product_code'])
        self.assertEqual(damage_loss_detail.name, valid_data['name'])
        self.assertEqual(damage_loss_detail.price, valid_data['price'])
        self.assertEqual(damage_loss_detail.reorder, valid_data['reorder'])
        self.assertEqual(damage_loss_detail.category_id,
                         valid_data['category_id'])
        self.assertEqual(damage_loss_detail.qty, valid_data['qty'])
        self.assertEqual(damage_loss_detail.remark, valid_data['remark'])

    def test_invalid_data(self) -> None:
        invalid_data: Dict[str, Any] = {
            'damage_loss_details_id': 'invalid_id',  # Invalid ID
            'damage_loss_id': 'invalid_damage_loss_id',  # Invalid damage_loss_id
            'item_id': 101,
            'product_code': 'P001',
            'name': 'Product A',
            'price': 50.0,
            'reorder': 10,
            'category_id': 201,
            'category_name': 'Cosmetics',
            'qty': -5,  # Negative qty
            'remark': ''  # Empty remark
        }

        with self.assertRaises(ValueError):
            DamageLossDetail(**invalid_data)


if __name__ == '__main__':
    unittest.main()
