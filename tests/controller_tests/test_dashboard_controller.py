import unittest
from controllers.dashboard_controller import DashboardController


class TestDashboardController(unittest.TestCase):

    def setUp(self):
        self.dashboard_controller = DashboardController()

    def test_inventory_info(self):
        response = self.dashboard_controller.inventory_info()
        self.assertEqual(
            response, {'in_hand': 0, 'out_of_stock': 7, 'low_in_stock': 0})

    def test_inventory_transactions(self):
        date = '2023-11-25'
        response = self.dashboard_controller.inventory_transactions(date)
        self.assertEqual(
            response, {'sale_qty': 0, 'item_receive_qty': 0, 'damage_loss_qty': 0})

    def test_sales(self):
        response = self.dashboard_controller.sales()
        self.assertEqual(response, {
                         'monthly_sales': 0, 'today_sales': 0, 'weekly_sales': 0, 'yearly_sales': 0})


if __name__ == '__main__':
    unittest.main()
