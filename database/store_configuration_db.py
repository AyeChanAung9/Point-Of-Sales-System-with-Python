from models.store_configuration import StoreConfiguration
from database.queries import *
from database.context_manager import DatabaseContextManager
from database.sqlite_db import data_to_dict


class StoreConfigDatabase:

    def modify(self, store_config: StoreConfiguration):
        with DatabaseContextManager() as cursor:
            cursor.execute(store_config_modify, (store_config.store_name,
                                                 store_config.contact_person, store_config.phone_no, store_config.address,
                                                 store_config.image_data))
            modified_row = cursor.rowcount
            assert modified_row > 0, "Failed to modify store configuration!"
        return "Store configuration updated successfully"

    def view(self):
        with DatabaseContextManager() as cursor:
            cursor.execute(store_config_view)
            data = cursor.fetchone()
            assert data, "Store configuration not found!"
            store_configuration = data_to_dict(data, cursor)
        return store_configuration

    def get_image(self):
        with DatabaseContextManager() as cursor:
            cursor.execute(store_config_image)
            data = cursor.fetchone()
            assert data, "Store Image not found!"
            image_data = data[0]
        return image_data
