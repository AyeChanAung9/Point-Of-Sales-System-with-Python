from typing import Any

from database.item_db import ItemDatabase
from database.user_role_permission_db import UserRolePermissionDatabase
from models.item import Item
from models.search_filter import SearchFilter


class ItemController:
    def __init__(self) -> None:
        self.__database = ItemDatabase()
        self.__user_role_permission_db = UserRolePermissionDatabase()

    # add, modify, delete
    def add_or_modify(self, item_dict: dict[str, Any]):
        item = Item(**item_dict)
        if item.is_modify():
            response = self.__database.modify(item)
        else:
            response = self.__database.add(item)
        return response

    def delete(self, item_id: int) -> str:
        response = self.__database.delete(item_id)
        return response

    # Views
    def view(self, params: dict[str, Any]):
        search_filter = SearchFilter(**params)
        response = self.__database.view(search_filter)
        return response

    def get_by_product_code(self, product_code: str):
        response = self.__database.get_by_product_code(product_code)
        return response
