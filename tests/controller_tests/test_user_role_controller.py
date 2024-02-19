import unittest
from controllers.user_role_controller import UserRoleController


class TestUserRoleController(unittest.TestCase):

    def setUp(self):
        self.user_role_controller = UserRoleController()

    def test_add_user_role(self):
        user_role_dict = {'role_name': 'Manager'}
        response = self.user_role_controller.add_or_modify(user_role_dict)
        self.assertEqual(response, "Manager added successfully")

    def test_modify_user_role(self):
        user_role_dict = {'role_name': 'Inventory Manager', 'role_id': '2'}
        response = self.user_role_controller.add_or_modify(user_role_dict)
        self.assertEqual(response, "Inventory Manager updated successfully")

    def test_delete_user_role(self):
        # add user
        user_role_dict = {'role_name': 'Casher'}
        response = self.user_role_controller.add_or_modify(user_role_dict)
        # delete user by id
        user_role_id = 3
        response = self.user_role_controller.delete(user_role_id)
        self.assertEqual(response, "Categoryis deleted successfully")

    def test_view_user_roles(self):
        params = {'search_keyword': 'Admin', 'page_no': '1'}
        response = self.user_role_controller.view(params)
        self.assertEqual(response, [{'role_id': 1, 'role_name': 'Admin'}])

    def test_get_all_user_roles(self):
        response = self.user_role_controller.get_all()
        self.assertEqual(len(response), 2)


if __name__ == '__main__':
    unittest.main()
