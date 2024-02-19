
from typing import Any
from models.search_filter import SearchFilter
from models.user import User
from database.queries import *
from database.context_manager import DatabaseContextManager
from database.sqlite_db import data_list_to_dict, data_to_dict
from flask_bcrypt import generate_password_hash, check_password_hash  # type: ignore


class UserDatabase:
    # add, modify, delete

    def add(self, user: User):
        with DatabaseContextManager() as cursor:
            cursor.execute(
                user_add, (user.username, generate_password_hash(user.password), user.role_id))
            user_id = cursor.lastrowid
            assert user_id is not None, f"Failed to add {user.username}!"
        return f"{user.username} added successfully"

    def modify(self, user: User):
        with DatabaseContextManager() as cursor:
            cursor.execute(user_modify, (user.username,
                                         generate_password_hash(user.password), user.role_id, user.user_id))
            modified_row = cursor.rowcount
            assert modified_row > 0, f"Failed to modify {user.username}!"
        return f"{user.username} updated successfully"

    def delete(self, user_id: int):
        with DatabaseContextManager() as cursor:
            cursor.execute(user_delete, (user_id,))
            deleted_row = cursor.rowcount
            assert deleted_row > 0, "Failed to delete User!"
        return "User deleted successfully"

    # Views
    def view(self, search_filter: SearchFilter):
        with DatabaseContextManager() as cursor:
            search = f"%{search_filter.search_keyword}%"

            if search_filter.filter_id:
                cursor.execute(user_view_by_role, (search,
                                                   search_filter.filter_id))
            else:
                cursor.execute(user_view_by_keyword, (search,))
            data = cursor.fetchall()
            users = data_list_to_dict(data, cursor)
        return users

    def get_by_id(self, user_id: int):
        with DatabaseContextManager() as cursor:
            cursor.execute(user_view_by_id, (user_id,))
            data = cursor.fetchone()
            assert data, f"No user with user id - {user_id}"
            user = data_to_dict(data, cursor)
        return user

    def __hashed_pw(self, password: Any):
        return password.decode('utf-8')

    def user_check_valid(self, user: User):
        with DatabaseContextManager() as cursor:
            cursor.execute(
                user_view_by_username, (user.username, ))
            data = cursor.fetchone()
            assert data, "Username or password incorrect."
            is_valid = check_password_hash(data[2], user.password)
            hashed_pw = self.__hashed_pw(data[2])
            assert is_valid, "Username or password incorrect."
        return (data[0], data[1], hashed_pw, data[3])
