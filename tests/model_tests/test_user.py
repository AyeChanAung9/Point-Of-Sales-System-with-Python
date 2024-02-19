import unittest
from models.user import User


class TestUser(unittest.TestCase):

    def test_valid_user_creation(self):
        user_data = {
            'user_id': 1,
            'username': 'sample_user',
            'password': 'SecurePass123',
            'role_id': 2,
            'role_name': 'Admin',
        }

        user = User(**user_data)

        self.assertEqual(user.user_id, 1)
        self.assertEqual(user.username, 'sample_user')
        self.assertEqual(user.password, 'SecurePass123')
        self.assertEqual(user.role_id, 2)
        self.assertEqual(user.role_name, 'Admin')

    def test_invalid_user_creation(self):
        # Invalid user creation with empty username
        user_data = {
            'user_id': 1,
            'username': '',
            'password': 'InsecurePass',
            'role_id': 3,
            'role_name': 'User',
        }

        with self.assertRaises(ValueError):
            User(**user_data)


if __name__ == '__main__':
    unittest.main()
