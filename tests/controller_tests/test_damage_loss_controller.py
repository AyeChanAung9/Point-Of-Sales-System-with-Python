import unittest
from controllers.damage_loss_controller import DamageLossController


class TestDamageLossController(unittest.TestCase):

    def setUp(self):
        self.damage_loss_controller = DamageLossController()

    def test_add_damage_loss(self):
        damage_loss_dict = {'voucher_no': 'DL202310251700926958518',
                            'tran_date': '2023-11-25',
                            'total_items': '1',
                            'user_id': '1',
                            'details': [
                                {'product_code': 'K001',
                                 'name': 'Knife',
                                 'category_name': 'Kitchen',
                                 'qty': '2',
                                 'remark': 'Broken',
                                 'item_id': '6',
                                 'damage_loss_details_id': None}
                            ]}

        response = self.damage_loss_controller.add(damage_loss_dict)
        self.assertEqual(response, "Damage Loss voucher added successfully")

    def test_modify_damage_loss(self):
        modify_data = {'damage_loss_id': '1',
                       'voucher_no': 'DL202310251700926958518',
                       'tran_date': '2023-11-25',
                       'total_items': '1',
                       'user_id': '1',
                       'details': [
                           {'damage_loss_details_id': '1',
                            'damage_loss_id': '1',
                            'item_id': '6',
                            'product_code': 'K001',
                            'name': 'Knife',
                            'category_name': 'Kitchen',
                            'qty': '4',
                            'remark': 'Broken'}],
                       'delete_ids': []}

        response = self.damage_loss_controller.modify(modify_data)
        self.assertEqual(response, "Damage Loss voucher modified successfully")

    def test_delete_damage_loss(self):
        # add data
        damage_loss_dict = {'voucher_no': 'DL202310251700926958518',
                            'tran_date': '2023-11-25',
                            'total_items': '1',
                            'user_id': '1',
                            'details': [
                                {'product_code': 'K001',
                                 'name': 'Knife',
                                 'category_name': 'Kitchen',
                                 'qty': '2',
                                 'remark': 'Broken',
                                 'item_id': '6',
                                 'damage_loss_details_id': None}
                            ]}
        response = self.damage_loss_controller.add(damage_loss_dict)
        # delete data by id
        damage_loss_id = 2

        response = self.damage_loss_controller.delete(damage_loss_id)
        self.assertTrue(response, "Damage_loss voucher deleted successfully")

    def test_view_damage_losses(self):
        params = {'search_keyword': 'DL202310211700577219059',
                  'from_tran_date': '2023-11-01', 'to_tran_date': '2023-11-24', 'page_no': '1'}
        response = self.damage_loss_controller.view(params)
        self.assertEqual(response, [])

    def test_view_damage_loss_details(self):
        damage_loss_id = 1
        response = self.damage_loss_controller.view_details(damage_loss_id)

        self.assertEqual(len(response), 1)
