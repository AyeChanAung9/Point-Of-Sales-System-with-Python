from models.user_role import UserRole
from models.search_filter import SearchFilter
from database.queries import *
from database.context_manager import DatabaseContextManager
from database.db_template import DatabaseTemplate
from database.sqlite_db import data_list_to_dict


class UserRoleDatabase(DatabaseTemplate):

    # add, modfiy ,delete

    def add(self, user_role: UserRole):
        query = user_role_add
        params = (user_role.role_name,)
        return super().add_execute(user_role.role_name, query, params)

    def modify(self, user_role: UserRole):
        query = user_role_modify
        params = (user_role.role_name, user_role.role_id)
        return super().modify_execute(user_role.role_name, query, params)

    def delete(self, role_id: int):
        query = user_role_delete
        return super().delete_execute("Category", query, role_id)

    # Views

    def view(self, search_filter: SearchFilter):
        with DatabaseContextManager() as cursor:
            search = f"%{search_filter.search_keyword}%"

            cursor.execute(user_role_view,
                           (search,))
            data = cursor.fetchall()
            roles = data_list_to_dict(data, cursor)
        return roles

    def get_all(self):
        query = user_role_view_for_role_filter
        return super().get_data_list(query)
