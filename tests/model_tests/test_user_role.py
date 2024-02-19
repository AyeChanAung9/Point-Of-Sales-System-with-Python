import unittest
from models.user_role import UserRole


class TestUserRole(unittest.TestCase):

    def test_valid_user_role_creation(self):
        role_data = {
            'role_id': 1,
            'role_name_can_empty': '',
            'role_name': 'Admin',
        }

        user_role = UserRole(**role_data)

        self.assertEqual(user_role.role_id, 1)
        self.assertEqual(user_role.role_name, 'Admin')

    def test_invalid_user_role_creation(self):
        # Invalid user role creation with empty role name
        with self.assertRaises(ValueError):
            UserRole()


if __name__ == '__main__':
    unittest.main()
