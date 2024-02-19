import unittest
from models.category import Category


class TestCategory(unittest.TestCase):

    def test_valid_category_creation(self):
        category_data = {
            'category_id': 1,
            'category_name_can_empty': '',
            'category_name': 'Sample Category',
        }

        category = Category(**category_data)

        self.assertEqual(category.category_id, 1)
        self.assertEqual(category.category_name, 'Sample Category')

    def test_invalid_category_creation(self):
        # Invalid category creation with empty category name
        category_data = {
            'category_id': 1,
            'category_name_can_empty': '',
            'category_name': '',
        }

        with self.assertRaises(ValueError):
            Category(**category_data)


if __name__ == '__main__':
    unittest.main()
