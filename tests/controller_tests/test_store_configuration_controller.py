import unittest
from controllers.store_configuration_controller import StoreConfigController


class TestStoreConfigController(unittest.TestCase):

    def setUp(self):
        self.store_config_controller = StoreConfigController()

    def test_modify_store_configuration(self):

        store_config_dict = {
            "store_name": "Test Store",
            "contact_person": "John Doe",
            "phone_no": "123-456-7890",
            "address": "Test Address",
            "image_data": b"static/img/Dash.png"
        }

        response = self.store_config_controller.modify(store_config_dict)
        self.assertEqual(response, "Store configuration updated successfully")

    def test_view_store_configuration(self):
        response = self.store_config_controller.view()
        self.assertTrue(response)


if __name__ == '__main__':
    unittest.main()
