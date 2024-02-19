from typing import Any

from database.user_role_permission_db import UserRolePermissionDatabase
from other.helper import to_list_tuple_with_id


class UserRolePermissionController:
    def __init__(self) -> None:
        self.__database = UserRolePermissionDatabase()

    def modify(self,  permissions_dict: dict[str, Any]):
        response = self.__database.modify(permissions_dict["role_id"], to_list_tuple_with_id(
            permissions_dict["role_id"], permissions_dict["permissions"]))
        return response

    def get_by_role_id(self, role_id: int):
        response = self.__database.get_by_role_id(role_id)
        return response

    def has_permission(self, role_id: Any, permission: str):
        response = self.__database.has_permission(role_id, permission)
        return response
