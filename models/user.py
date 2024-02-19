from typing import Any

from models.user_role import UserRole
from other.validations import validate_password, validate_non_empty_string


class User:
    def __init__(self, **kwargs: Any) -> None:
        self.__user_id = kwargs.get('user_id', "0")
        self.__username = validate_non_empty_string(
            kwargs.get('username', ''), "Username")
        self.__password = validate_password(kwargs.get('password', ''))
        self.__role = UserRole(**kwargs)  # type: ignore

    def is_modify(self):
        return (isinstance(self.user_id, int) and self.user_id > 0) or int(self.user_id) > 0

    @property
    def user_id(self):
        return self.__user_id

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @property
    def role(self):
        return self.__role

    @property
    def role_id(self):
        return self.__role.role_id

    @property
    def role_name(self):
        return self.__role.role_name
