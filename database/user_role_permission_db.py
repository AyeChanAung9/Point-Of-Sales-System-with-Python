from typing import Any
from database.context_manager import DatabaseContextManager
from database.queries import *
from database.sqlite_db import data_list_to_dict


class UserRolePermissionDatabase:
    def modify(self, role_id: int, permissions: list[Any]):
        # delete all previous permissions and insert new premissions
        with DatabaseContextManager() as cursor:
            cursor.execute(user_role_permissions_delete, (role_id,))

            cursor.executemany(user_role_permissions_insert,
                               permissions)
        return "User role permissions updated successfully"

    def get_by_role_id(self, role_id: int) -> Any:
        with DatabaseContextManager() as cursor:
            cursor.execute(
                user_role_permissions_view_by_role_id, (role_id,))
            data = cursor.fetchall()
            permissions = data_list_to_dict(data, cursor, no_column_name=True)
        return permissions

    def has_permission(self, role_id: int, permission: str):
        with DatabaseContextManager() as cursor:
            cursor.execute(
                user_role_permissions_has_permission, (role_id, permission))
            data = cursor.fetchall()
        return len(data) > 0
