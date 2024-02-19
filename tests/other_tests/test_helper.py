import unittest
import os
from other.helper import to_list_tuple, delete_file


class TestHelper(unittest.TestCase):

    def test_to_list_tuple(self):
        # Test case 1: Testing to_list_tuple with an empty list
        data = []
        result = to_list_tuple(data)
        self.assertEqual(result, [])

        # Test case 2: Testing to_list_tuple with a list of integers
        data = [1, 2, 3]
        result = to_list_tuple(data)
        self.assertEqual(result, [(1,), (2,), (3,)])

        # Test case 3: Testing to_list_tuple with a list of strings
        data = ['a', 'b', 'c']
        result = to_list_tuple(data)
        self.assertEqual(result, [('a',), ('b',), ('c',)])

        # Test case 4: Testing to_list_tuple with a list of mixed types
        data = [1, 'a', True]
        result = to_list_tuple(data)
        self.assertEqual(result, [(1,), ('a',), (True,)])

    def test_delete_file(self):
        # Test case 1: Testing delete_file with an existing file

        file_content = """This fiel is created for testing purpose."""

        file_name = 'dummy_file_for_test.txt'
        with open(file_name, 'w') as file:
            file.write(file_content)
        delete_file(file_name)
        self.assertFalse(os.path.exists(file_name))

        # Test case 2: Testing delete_file with a nonexistent file
        file_name = "nonexistent_file.txt"
        delete_file(file_name)
        self.assertFalse(os.path.exists(file_name))


if __name__ == '__main__':
    unittest.main()
