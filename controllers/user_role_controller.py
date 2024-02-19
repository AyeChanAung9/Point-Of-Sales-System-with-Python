from typing import Any

from database.user_role_db import UserRoleDatabase
from models.user_role import UserRole
from models.search_filter import SearchFilter


class UserRoleController:
    def __init__(self):
        self.__database = UserRoleDatabase()

# add, modify, delete

    def add_or_modify(self, user_role_dict: dict[str, Any]):
        user_role = UserRole(**user_role_dict)
        if user_role.is_modify():
            response = self.__database.modify(user_role)
        else:
            response = self.__database.add(user_role)
        return response

    def delete(self, id: int):
        response = self.__database.delete(id)
        return response

# Views

    def view(self, params: dict[str, Any]):
        search_filter = SearchFilter(**params)
        response = self.__database.view(search_filter)
        return response

    def get_all(self):
        response = self.__database.get_all()
        return response
