from models.category import Category
from models.search_filter import SearchFilter
from database.queries import *
from database.context_manager import DatabaseContextManager
from database.db_template import DatabaseTemplate
from database.sqlite_db import data_list_to_dict


class CategoryDatabase(DatabaseTemplate):

    # add, modify ,delete

    def add(self, category: Category):
        query = category_add
        params = (category.category_name,)
        return super().add_execute(category.category_name, query, params)

    def modify(self, category: Category):
        query = category_modify
        params = (category.category_name, category.category_id)
        return super().modify_execute(category.category_name, query, params)

    def delete(self, category_id: int):
        query = category_delete
        return super().delete_execute("Category", query, category_id)

    # Views
    def view(self, search_filter: SearchFilter):
        with DatabaseContextManager() as cursor:
            search = f"%{search_filter.search_keyword}%"
            cursor.execute(category_view_by_keyword,
                           (search, ))
            data = cursor.fetchall()
            categories = data_list_to_dict(data, cursor)
        return categories

    def get_all(self):
        query = category_view_for_item_filter
        return super().get_data_list(query)
