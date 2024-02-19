import unittest
from models.search_filter import SearchFilter
from typing import Dict, Any


class TestSearchFilter(unittest.TestCase):

    def test_valid_data(self) -> None:
        valid_data: Dict[str, Any] = {
            'page_no': 2,
            'search_keyword': 'keyword',
            'filter_id': '123',
            'from_tran_date': '2023-01-01',
            'to_tran_date': '2023-01-31'
        }

        search_filter = SearchFilter(**valid_data)
        self.assertEqual(search_filter.page_no, valid_data['page_no'])
        self.assertEqual(search_filter.search_keyword,
                         valid_data['search_keyword'])
        self.assertEqual(search_filter.filter_id, valid_data['filter_id'])
        self.assertEqual(search_filter.from_tran_date,
                         valid_data['from_tran_date'])
        self.assertEqual(search_filter.to_tran_date,
                         valid_data['to_tran_date'])

    def test_invalid_data(self) -> None:
        invalid_data: Dict[str, Any] = {
            'page_no': 'invalid_page_no',  # Invalid page_no
            'search_keyword': 123,  # Invalid search_keyword
            'filter_id': 456,  # Invalid filter_id
            'from_tran_date': 'invalid_date',  # Invalid from_tran_date
            'to_tran_date': 789  # Invalid to_tran_date
        }

        with self.assertRaises(ValueError):
            SearchFilter(**invalid_data)

    def test_default_values(self) -> None:
        default_values: Dict[str, Any] = {}

        search_filter = SearchFilter(**default_values)
        self.assertEqual(search_filter.page_no, 1)  # Default page_no is 1
        # Default search_keyword is an empty string
        self.assertEqual(search_filter.search_keyword, '')
        # Default filter_id is an empty string
        self.assertEqual(search_filter.filter_id, '')
        # Default from_tran_date is an empty string
        self.assertEqual(search_filter.from_tran_date, '')
        # Default to_tran_date is an empty string
        self.assertEqual(search_filter.to_tran_date, '')


if __name__ == '__main__':
    unittest.main()
