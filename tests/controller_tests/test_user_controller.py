import unittest
from controllers.user_controller import UserController


class TestUserController(unittest.TestCase):

    def setUp(self):
        self.user_controller = UserController()

    def test_add_user(self):
        user_dict = {'username': 'someone', 'password': '1127',
                     'role_id': '1', 'role_name_can_empty': 'true'}
        response = self.user_controller.add_or_modify(user_dict)
        self.assertEqual(response, "someone added successfully")

    def test_modify_user(self):
        user_dict = {'username': 'someone', 'password': '1027',
                     'role_id': '1', 'role_name_can_empty': 'true', 'user_id': '2'}
        response = self.user_controller.add_or_modify(user_dict)
        self.assertEqual(response, "someone updated successfully")

    def test_delete_user(self):
        # add data for deletion
        user_dict = {'username': 'delete', 'password': '1127',
                     'role_id': '1', 'role_name_can_empty': 'true'}
        response = self.user_controller.add_or_modify(user_dict)
        # delete user by id
        user_id = 3
        response = self.user_controller.delete(user_id)
        self.assertEqual(response, "User deleted successfully")

    def test_view_users(self):
        params = {'search_keyword': 'admin', 'filter_id': '1', 'page_no': '1'}
        response = self.user_controller.view(params)
        self.assertEqual(len(response), 1)


if __name__ == '__main__':
    unittest.main()
