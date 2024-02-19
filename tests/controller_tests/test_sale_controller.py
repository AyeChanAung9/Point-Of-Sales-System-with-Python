import unittest
from controllers.sale_controller import SaleController


class TestSaleController(unittest.TestCase):

    def setUp(self):
        self.sale_controller = SaleController()

    def test_add_sale(self):
        sale_dict = {'voucher_no': 'S202310251700932699175', 'tran_date': '2023-11-25', 'total_items': '1', 'user_id': '1', 'discount': '3,200.00', 'details': [
            {'product_code': 'E002', 'name': 'Power Bank', 'category_name': 'Electronics', 'qty': '4', 'item_id': '5', 'sale_detail_id': None, 'price': '40,000.00'}], 'total_amount': '156,800.00', 'discount_percentage': '2', 'payment': 'cshp'}

        response = self.sale_controller.add(sale_dict)

        self.assertEqual(response, "Sale voucher added successfully")

    def test_modify_sale(self):
        sale_dict = {'voucher_no': 'S202310251700932699175', 'tran_date': '2023-11-25', 'total_items': '1', 'user_id': '1', 'discount': '1,200.00', 'details': [
            {'product_code': 'E002', 'name': 'Power Bank', 'category_name': 'Electronics', 'qty': '3', 'item_id': '5', 'sale_detail_id': '1', 'price': '40000.0'}], 'total_amount': '118,800.00', 'discount_percentage': '1', 'payment': 'cshp', 'sale_id': '1', 'delete_ids': []}
        response = self.sale_controller.modify(sale_dict)
        self.assertTrue(response)

    def test_delete_sale(self):
        # add data
        sale_dict = {'voucher_no': 'S202310251700932699185', 'tran_date': '2023-11-25', 'total_items': '1', 'user_id': '1', 'discount': '3,200.00', 'details': [
            {'product_code': 'E002', 'name': 'Power Bank', 'category_name': 'Electronics', 'qty': '4', 'item_id': '5', 'sale_detail_id': None, 'price': '40,000.00'}], 'total_amount': '156,800.00', 'discount_percentage': '2', 'payment': 'cshp'}
        response = self.sale_controller.add(sale_dict)
        # delete data by id
        sale_id = 2
        response = self.sale_controller.delete(sale_id)

        self.assertEqual(response, "Sale voucher deleted successfully")

    def test_view_sales(self):
        params = {'search_keyword': 'S202310251700932699175',
                  'from_tran_date': '', 'to_tran_date': '', 'page_no': '1'}
        response = self.sale_controller.view(params)
        self.assertEqual(len(response), 1)

    def test_view_sale_details(self):
        sale_id = 1
        response = self.sale_controller.view_details(sale_id)
        self.assertEqual(len(response), 1)


if __name__ == '__main__':
    unittest.main()
