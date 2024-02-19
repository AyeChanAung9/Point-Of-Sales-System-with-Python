from typing import Any
from database.store_configuration_db import StoreConfigDatabase
from models.store_configuration import StoreConfiguration


class StoreConfigController:
    def __init__(self) -> None:
        self.__database = StoreConfigDatabase()

    def modify(self, store_config_dict: dict[str, Any]):
        store_config = StoreConfiguration(**store_config_dict)
        response = self.__database.modify(store_config)
        return response

    def view(self):
        response = self.__database.view()
        return response

    def get_image(self):
        response = self.__database.get_image()
        return response
