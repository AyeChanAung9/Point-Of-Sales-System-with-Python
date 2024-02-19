from typing import Any

from other.validations import validate_non_empty_string, validate_string

role_name_validate_fun = {
    "true": validate_string, "": validate_non_empty_string}


class UserRole:
    def __init__(self, **kwargs: Any) -> None:
        self.__role_id = kwargs.get('role_id', "0")
        self.__role_name = role_name_validate_fun[kwargs.get('role_name_can_empty', "")](
            kwargs.get('role_name', ''), "Role name")

    def is_modify(self):
        return (isinstance(self.role_id, int) and self.role_id > 0) or int(self.role_id) > 0

    @property
    def role_id(self):
        return self.__role_id

    @property
    def role_name(self):
        return self.__role_name
