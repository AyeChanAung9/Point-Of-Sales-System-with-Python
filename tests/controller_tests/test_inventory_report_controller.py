import unittest
from controllers.inventory_report_controller import InventoryReportController


class TestInventoryReportController(unittest.TestCase):

    def setUp(self):
        self.controller = InventoryReportController()

    def test_get_stock_info_by_year(self):
        year = '2023'
        response = self.controller.get_stock_info_by_year(year)
        self.assertEqual(response, {'total_products': 7, 'total_categories': 4,
                                    'low_in_stock': 0, 'out_of_stock': 7, 'instock': 0,
                                    'item_receive_total': 0, 'damage_loss_total': 0,
                                    'sale_total': 0})

    def test_get_stock_transactions_by_year(self):
        year = '2023'
        response = self.controller.get_stock_transactions_by_year(year)
        expected_result = {
            'receive_values': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'sale_values': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'damage_loss_values': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        }
        self.assertEqual(response, expected_result)


if __name__ == '__main__':
    unittest.main()
