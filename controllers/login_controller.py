from typing import Any
from models.user import User
from database.user_db import UserDatabase


class LoginController:
    def __init__(self):
        self.__database = UserDatabase()

    def check_valid(self, user_dict: dict[str, Any]):
        user = User(**user_dict)
        response = self.__database.user_check_valid(user)
        return response
