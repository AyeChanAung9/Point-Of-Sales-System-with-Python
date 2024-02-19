import unittest
from controllers.item_controller import ItemController


class TestItemController(unittest.TestCase):

    def setUp(self):
        self.item_controller = ItemController()

    def test_add_item(self):
        item_dict = {'name': 'Battery',
                     'product_code': 'E003',
                     'cost_price': '5000',
                     'price': '7000',
                     'reorder': '20',
                     'category_id': '2',
                     'category_name_can_empty': 'true'}
        response = self.item_controller.add_or_modify(item_dict)

        self.assertTrue(response, "Battery(E003) added successfully")

    def test_modify_item(self):
        item_dict = {'name': 'Battery',
                     'product_code': 'E111',
                     'cost_price': '5000',
                     'price': '9000',
                     'reorder': '30',
                     'category_id': '2',
                     'category_name_can_empty': 'true',
                     'item_id': '7'}

        response = self.item_controller.add_or_modify(item_dict)

        self.assertEqual(response, "Battery updated successfully")

    def test_delete_item(self):
        # add item
        item_dict = {'name': 'Laptop',
                     'product_code': 'E004',
                     'cost_price': '8000',
                     'price': '10000',
                     'reorder': '20',
                     'category_id': '2',
                     'category_name_can_empty': 'true'}

        response = self.item_controller.add_or_modify(item_dict)
        # delete item by id
        item_id = 8
        response = self.item_controller.delete(item_id)
        self.assertEqual(response, 'Itemis deleted successfully')

    def test_view_items(self):
        params = {'search_keyword': 'Battery',
                  'filter_id': '2', 'page_no': '1'}
        response = self.item_controller.view(params)
        self.assertEqual(response, [{'item_id': 7, 'product_code': 'E111', 'name': 'Battery', 'price': 9000.0,
                         'reorder': 30, 'category_id': 2, 'cost_price': 5000.0, 'category_name': 'Electronics', 'current_stock': 0}])

    def test_get_by_product_code(self):
        product_code = 'E003'
        response = self.item_controller.get_by_product_code(product_code)
        self.assertEqual(response, {'item_id': 7, 'product_code': 'E003', 'name': 'Battery', 'price': 7000.0,
                         'reorder': 20, 'category_id': 2, 'cost_price': 5000.0, 'category_name': 'Electronics', 'current_stock': 0})


if __name__ == '__main__':
    unittest.main()
