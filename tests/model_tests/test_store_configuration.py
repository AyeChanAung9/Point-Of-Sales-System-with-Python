import unittest
from models.store_configuration import StoreConfiguration


class TestStoreConfiguration(unittest.TestCase):

    def setUp(self):
        # Create an instance of StoreConfiguration for testing
        self.store_config = StoreConfiguration(
            store_name="Test Store",
            contact_person="John Doe",
            phone_no="123-456-7890",
            address="Test Address",
            image_data=b"static/img/Dash.png"
        )

    def test_store_name(self):
        self.assertEqual(self.store_config.store_name, "Test Store")

    def test_contact_person(self):
        self.assertEqual(self.store_config.contact_person, "John Doe")

    def test_phone_no(self):
        self.assertEqual(self.store_config.phone_no, "123-456-7890")

    def test_address(self):
        self.assertEqual(self.store_config.address, "Test Address")

    def test_image_data(self):
        self.assertEqual(self.store_config.image_data, b"static/img/Dash.png")

    def test_to_tuple_db(self):
        expected_result = ("Test Store", "John Doe",
                           "123-456-7890", "Test Address", b"static/img/Dash.png")
        self.assertEqual(self.store_config.to_tuple_db(), expected_result)

    def test_to_tuple_db_without_id(self):
        expected_result = ("Test Store", "John Doe",
                           "123-456-7890", "Test Address", b"static/img/Dash.png")
        self.assertEqual(
            self.store_config.to_tuple_db_without_id(), expected_result)


if __name__ == '__main__':
    unittest.main()
