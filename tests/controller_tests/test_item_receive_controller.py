import unittest
from controllers.item_receive_controller import ItemReceiveController


class TestItemReceiveController(unittest.TestCase):

    def setUp(self):
        self.item_receive_controller = ItemReceiveController()

    def test_add_item_receive(self):
        item_receive_dict = {'voucher_no': 'IR202310251700931608429',
                             'tran_date': '2023-11-25',
                             'total_items': '1',
                             'user_id': '1',
                             'details': [{'product_code': 'E002', 'name': 'Power Bank', 'category_name': 'Electronics', 'qty': '3', 'item_id': '5', 'item_receive_details_id': None}]}

        response = self.item_receive_controller.add(item_receive_dict)
        self.assertEqual(response, "Item Receive voucher added successfully")

    def test_modify_item_receive(self):
        item_receive_dict = {'item_receive_id': '1',
                             'voucher_no': 'IR202310251700931608429',
                             'tran_date': '2023-11-25',
                             'total_items': '1',
                             'user_id': '1',
                             'details': [{'product_code': 'E003', 'name': 'Power Bank', 'category_name': 'Electronics', 'qty': '3', 'item_id': '5', 'item_receive_details_id': '1'}],
                             'delete_ids': []}

        response = self.item_receive_controller.modify(item_receive_dict)
        self.assertTrue(response)

    def test_delete_item_receive(self):
        item_receive_dict = {'voucher_no': 'IR202310251700931608439',
                             'tran_date': '2023-11-25',
                             'total_items': '1',
                             'user_id': '1',
                             'details': [{'product_code': 'E002', 'name': 'Power Bank', 'category_name': 'Electronics', 'qty': '3', 'item_id': '5', 'item_receive_details_id': None}]}

        response = self.item_receive_controller.add(item_receive_dict)

        item_receive_id = 2
        response = self.item_receive_controller.delete(item_receive_id)
        self.assertEqual(response, "Item Receive voucher deleted successfully")

    def test_view_item_receives(self):
        params = {'search_keyword': 'IR202310251700931608429',
                  'from_tran_date': '2023-11-01', 'to_tran_date': '2023-11-25', 'page_no': '1'}

        response = self.item_receive_controller.view(params)

        self.assertEqual(len(response), 1)

    def test_view_item_receive_details(self):
        item_receive_id = 1
        response = self.item_receive_controller.view_details(item_receive_id)

        self.assertEqual(len(response), 1)


if __name__ == '__main__':
    unittest.main()
