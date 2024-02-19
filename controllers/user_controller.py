from typing import Any

from database.user_db import UserDatabase
from models.user import User
from models.search_filter import SearchFilter


class UserController:
    def __init__(self):
        self.__database = UserDatabase()

# add, modify, delete

    def add_or_modify(self, user_dict: dict[str, Any]):
        user = User(**user_dict)
        if user.is_modify():
            response = self.__database.modify(user)
        else:
            response = self.__database.add(user)
        return response

    def delete(self, id: int):
        response = self.__database.delete(id)
        return response

# Views

    def view(self, params: dict[str, Any]):
        search_filter = SearchFilter(**params)
        response = self.__database.view(search_filter)
        return response
