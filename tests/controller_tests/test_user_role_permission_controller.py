import unittest
from controllers.user_role_permission_controller import UserRolePermissionController


class TestUserRolePermissionController(unittest.TestCase):

    def setUp(self):
        self.controller = UserRolePermissionController()

    def test_modify(self):
        modified_data = {'role_id': '1', 'permissions': ['item_read', 'item_delete', 'category_read',
                                                         'category_write', 'item_receive_write', 'damage_loss_write',
                                                         'sales_read', 'reports', 'users', 'user_roles', 'user_permissions',
                                                         'store_configuration']}
        response = self.controller.modify(modified_data)
        self.assertEqual(
            response, "User role permissions updated successfully")

    def test_get_by_role_id(self):
        role_id = 1
        response = self.controller.get_by_role_id(role_id)
        self.assertEqual(response, ['category_delete', 'category_read', 'category_write',
                                    'damage_loss_delete', 'damage_loss_read', 'damage_loss_write',
                                    'item_delete', 'item_read', 'item_receive_delete', 'item_receive_read', 'item_receive_write',
                                    'item_write', 'reports', 'sales_delete', 'sales_read', 'sales_write', 'store_configuration',
                                    'user_permissions', 'user_roles', 'users'])

    def test_has_permission(self):
        role_id = 1
        permission = "user_permissions"
        response = self.controller.has_permission(role_id, permission)
        self.assertEqual(response, True)


if __name__ == "__main__":
    unittest.main()
