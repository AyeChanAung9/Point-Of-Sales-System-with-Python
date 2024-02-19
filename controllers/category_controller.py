from typing import Any

from database.category_db import CategoryDatabase
from models.category import Category
from models.search_filter import SearchFilter


class CategoryController:
    def __init__(self):
        self.__database = CategoryDatabase()

# add, modify, delete

    def add_or_modify(self, category_dict: dict[str, Any]) -> str:
        category = Category(**category_dict)
        if category.is_modify():
            response = self.__database.modify(category)
        else:
            response = self.__database.add(category)
        return response

    def delete(self, id: int) -> str:
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
