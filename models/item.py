from typing import Any
from models.category import Category
from other.validations import *


class Item:
    def __init__(self,  **kwargs: Any) -> None:
        self.__item_id = kwargs.get('item_id', "0")
        self.__product_code = validate_code(
            kwargs.get('product_code', ''), "Product Code")
        self.__name = validate_non_empty_string(
            kwargs.get('name', ''), "Item Name")
        self.__price = validate_price(kwargs.get('price', '0'))
        self.__reorder = validate_number(
            kwargs.get('reorder', '0'), "Re-order Limit")
        self.__category = Category(**kwargs)
        self.__cost_price = kwargs.get('cost_price', '')

    def is_modify(self):
        return (isinstance(self.item_id, int) and self.item_id > 0) or int(self.item_id) > 0

    @property
    def item_id(self):
        return self.__item_id

    @property
    def product_code(self):
        return self.__product_code

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def reorder(self):
        return self.__reorder

    @property
    def category(self):
        return self.__category

    @property
    def category_id(self):
        return self.__category.category_id

    @property
    def category_name(self):
        return self.__category.category_name

    @property
    def cost_price(self):
        return self.__cost_price
