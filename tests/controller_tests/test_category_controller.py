import unittest
from controllers.category_controller import CategoryController


class TestCategoryController(unittest.TestCase):
    def setUp(self):
        self.controller = CategoryController()

    def test_add(self):
        category_data = {'category_name': 'Example Category'}
        response = self.controller.add_or_modify(category_data)
        self.assertEqual(
            response, f"{category_data['category_name']} added successfully")

    def test_modify(self):
        modified_data = {'category_id': 1,
                         'category_name': 'Modified Category'}
        response = self.controller.add_or_modify(modified_data)
        self.assertEqual(
            response, f"{modified_data['category_name']} updated successfully")

    def test_delete(self):
        # adding sample data to
        category_data = {'category_name': 'Golden Data'}
        self.controller.add_or_modify(category_data)
        # delete data
        category_id = 4
        response = self.controller.delete(category_id)
        self.assertEqual(response, "Categoryis deleted successfully")

    def test_view_without_keyword(self):
        params = {'search_keyword': '', 'page_no': '1'}
        response = self.controller.view(params)
        self.assertEqual(len(response), 4)

    def test_view_with_keyword(self):
        params = {'search_keyword': 'K', 'page_no': '1'}
        response = self.controller.view(params)
        self.assertEqual(
            response, [{'category_id': 3, 'category_name': 'Kitchen'}])

    def test_get_all(self):
        response = self.controller.get_all()
        self.assertEqual(len(response), 4)


if __name__ == '__main__':
    unittest.main()
