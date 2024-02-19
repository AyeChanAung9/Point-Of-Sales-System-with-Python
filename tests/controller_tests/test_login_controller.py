import unittest
from controllers.login_controller import LoginController


class TestLoginController(unittest.TestCase):

    def setUp(self):
        self.login_controller = LoginController()

    def test_check_valid_user(self):
        user_dict = {'username': 'admin', 'password': '123456',
                     'remember_me': 'true', 'role_name_can_empty': 'true'}
        response = self.login_controller.check_valid(user_dict)
        self.assertTrue(response)

    def test_check_invalid_user(self):
        wrong_dict = {'username': 'invalid user', 'password': 'invalid',
                      'remember_me': 'true', 'role_name_can_empty': 'true'}
        with self.assertRaises(AssertionError):
            self.login_controller.check_valid(wrong_dict)


if __name__ == '__main__':
    unittest.main()
