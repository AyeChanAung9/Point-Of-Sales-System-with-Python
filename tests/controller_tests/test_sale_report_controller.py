import unittest
from controllers.sale_report_controller import SaleReportController


class TestSaleReportController(unittest.TestCase):

    def setUp(self):
        self.controller = SaleReportController()

    def test_get_year(self):
        response = self.controller.get_year()
        self.assertEqual(response, [])

    def test_get_top_selling(self):
        sample_data = {'from_date': '2023-01-01', 'to_date': '2023-12-31'}
        response = self.controller.get_top_selling(sample_data)
        self.assertEqual(response, [])

    def test_get_items_by_total_sales(self):
        sample_data = {'from_date': '-05-01', 'to_date': '-05-31'}
        response = self.controller.get_items_by_total_sales(sample_data)
        self.assertEqual(response, [])

    def test_get_categories_sales_by_total_sales(self):
        sample_data = {'from_date': '-05-01', 'to_date': '-05-31'}
        response = self.controller.get_categories_sales_by_total_sales(
            sample_data)
        self.assertEqual(response, [])

    def test_get_total_sales(self):
        sample_data = {'option': 'monthly',
                       'from_date': '2023-01-01', 'to_date': '2023-12-31'}
        response = self.controller.get_total_sales(sample_data)
        self.assertEqual(response, [])

    def test_get_sale_report_by_daily(self):
        sample_data = "2023-01-01"
        response = self.controller.get_sale_report_by_daily(sample_data)
        self.assertEqual(response, [])

    def test_get_qty_sold_by_category(self):
        sample_data = {'option': 'monthly',
                       'from_date': '2023-01-01', 'to_date': '2023-12-31'}
        response = self.controller.get_qty_sold_by_category(sample_data)
        self.assertEqual(response, [{'category_name': 'Modified Category', 'tran_date': 'No Sales', 'year': None, 'qty': 0},
                                    {'category_name': 'Electronics',
                                        'tran_date': 'No Sales', 'year': None, 'qty': 0},
                                    {'category_name': 'Kitchen',
                                        'tran_date': 'No Sales', 'year': None, 'qty': 0},
                                    {'category_name': 'Golden Data', 'tran_date': 'No Sales', 'year': None, 'qty': 0}])

    def test_get_revenue_category(self):
        sample_data = {'option': 'monthly',
                       'from_date': '2023-01-01', 'to_date': '2023-12-31'}
        response = self.controller.get_revenue_category(sample_data)
        self.assertEqual(response, [{'category_name': 'Modified Category', 'tran_date': 'No Sales', 'year': None, 'total_price': 0},
                                    {'category_name': 'Electronics', 'tran_date': 'No Sales',
                                        'year': None, 'total_price': 0},
                                    {'category_name': 'Kitchen', 'tran_date': 'No Sales',
                                        'year': None, 'total_price': 0},
                                    {'category_name': 'Golden Data', 'tran_date': 'No Sales', 'year': None, 'total_price': 0}])

    def test_get_qty_sold_by_item(self):
        sample_data = {'option': 'monthly',
                       'from_date': '2023-01-01', 'to_date': '2023-12-31'}
        response = self.controller.get_qty_sold_by_item(sample_data)
        self.assertEqual(response, [{'item_id': 1, 'item_name': 'Face Cleanser', 'tran_date': 'No Sales', 'year': None, 'qty': 0},
                                    {'item_id': 2, 'item_name': 'Serum',
                                        'tran_date': 'No Sales', 'year': None, 'qty': 0},
                                    {'item_id': 3, 'item_name': 'Toner',
                                        'tran_date': 'No Sales', 'year': None, 'qty': 0},
                                    {'item_id': 4, 'item_name': 'Hair Dryer',
                                        'tran_date': 'No Sales', 'year': None, 'qty': 0},
                                    {'item_id': 5, 'item_name': 'Power Bank',
                                        'tran_date': 'No Sales', 'year': None, 'qty': 0},
                                    {'item_id': 6, 'item_name': 'Knife',
                                        'tran_date': 'No Sales', 'year': None, 'qty': 0},
                                    {'item_id': 7, 'item_name': 'Battery', 'tran_date': 'No Sales', 'year': None, 'qty': 0}])

    def test_get_revenue_item(self):
        sample_data = {'option': 'monthly',
                       'from_date': '2023-01-01', 'to_date': '2023-12-31'}
        response = self.controller.get_revenue_item(sample_data)
        self.assertEqual(response, [{'item_id': 1, 'item_name': 'Face Cleanser', 'tran_date': 'No Sales', 'year': None, 'total_price': 0},
                                    {'item_id': 2, 'item_name': 'Serum',
                                        'tran_date': 'No Sales', 'year': None, 'total_price': 0},
                                    {'item_id': 3, 'item_name': 'Toner',
                                        'tran_date': 'No Sales', 'year': None, 'total_price': 0},
                                    {'item_id': 4, 'item_name': 'Hair Dryer',
                                        'tran_date': 'No Sales', 'year': None, 'total_price': 0},
                                    {'item_id': 5, 'item_name': 'Power Bank',
                                        'tran_date': 'No Sales', 'year': None, 'total_price': 0},
                                    {'item_id': 6, 'item_name': 'Knife',
                                        'tran_date': 'No Sales', 'year': None, 'total_price': 0},
                                    {'item_id': 7, 'item_name': 'Battery', 'tran_date': 'No Sales', 'year': None, 'total_price': 0}])

    def test_get_sale_growth(self):
        sample_data = "2023"
        response = self.controller.get_sale_growth(sample_data)
        self.assertEqual(response, [{'item_id': 1, 'item_name': 'Face Cleanser', 'tran_date': 'No Sales', 'total_price': 0, 'sale_percentage': 0},
                                    {'item_id': 2, 'item_name': 'Serum', 'tran_date': 'No Sales',
                                        'total_price': 0, 'sale_percentage': 0},
                                    {'item_id': 3, 'item_name': 'Toner', 'tran_date': 'No Sales',
                                        'total_price': 0, 'sale_percentage': 0},
                                    {'item_id': 4, 'item_name': 'Hair Dryer', 'tran_date': 'No Sales',
                                        'total_price': 0, 'sale_percentage': 0},
                                    {'item_id': 5, 'item_name': 'Power Bank', 'tran_date': 'No Sales',
                                        'total_price': 0, 'sale_percentage': 0},
                                    {'item_id': 6, 'item_name': 'Knife', 'tran_date': 'No Sales',
                                        'total_price': 0, 'sale_percentage': 0},
                                    {'item_id': 7, 'item_name': 'Battery', 'tran_date': 'No Sales', 'total_price': 0, 'sale_percentage': 0}])

    def test_get_quarterly_sale(self):
        sample_data = "2023"
        response = self.controller.get_quarterly_sale(sample_data)
        self.assertEqual(response, [{'product_code': 'C001', 'item_name': 'Face Cleanser', 'category_id': 1, 'category_name': 'Modified Category', 'quarter': 'No Sales', 'year': 'No Sales', 'total_quarterly_sales': 0, 'total_quarterly_profit': 0},
                                    {'product_code': 'C002', 'item_name': 'Serum', 'category_id': 1, 'category_name': 'Modified Category',
                                        'quarter': 'No Sales', 'year': 'No Sales', 'total_quarterly_sales': 0, 'total_quarterly_profit': 0},
                                    {'product_code': 'C003', 'item_name': 'Toner', 'category_id': 1, 'category_name': 'Modified Category',
                                        'quarter': 'No Sales', 'year': 'No Sales', 'total_quarterly_sales': 0, 'total_quarterly_profit': 0},
                                    {'product_code': 'E001', 'item_name': 'Hair Dryer', 'category_id': 2, 'category_name': 'Electronics',
                                        'quarter': 'No Sales', 'year': 'No Sales', 'total_quarterly_sales': 0, 'total_quarterly_profit': 0},
                                    {'product_code': 'E002', 'item_name': 'Power Bank', 'category_id': 2, 'category_name': 'Electronics',
                                        'quarter': 'No Sales', 'year': 'No Sales', 'total_quarterly_sales': 0, 'total_quarterly_profit': 0},
                                    {'product_code': 'E111', 'item_name': 'Battery', 'category_id': 2, 'category_name': 'Electronics',
                                        'quarter': 'No Sales', 'year': 'No Sales', 'total_quarterly_sales': 0, 'total_quarterly_profit': 0},
                                    {'product_code': 'K001', 'item_name': 'Knife', 'category_id': 3, 'category_name': 'Kitchen', 'quarter': 'No Sales', 'year': 'No Sales', 'total_quarterly_sales': 0, 'total_quarterly_profit': 0}])


if __name__ == "__main__":
    unittest.main()
