from typing import Any
from models.item import Item

from other.validations import *


class SaleDetail:
    def __init__(self, **kwargs: Any) -> None:
        self.__sale_detail_id = kwargs.get("sale_detail_id")
        self.__sale_id = validate_number_greater_than_zero(
            kwargs.get("sale_id", "0"), "Sales ID")
        self.__item = Item(**kwargs)
        self.__qty = validate_number_greater_than_zero(
            kwargs.get("qty", "0"), "Quantity")
        self.__price = validate_price(kwargs.get("price", "0"))

    def to_tuple_db(self, sale_id: int):
        return (self.sale_detail_id, sale_id, self.item_id, self.qty, self.price)

    def to_tuple_db_without_id(self, sale_id: int):
        return (sale_id, self.item_id, self.qty, self.price)

    @property
    def sale_detail_id(self):
        return self.__sale_detail_id

    @property
    def sale_id(self):
        return self.__sale_id

    @property
    def item_id(self):
        return self.__item.item_id

    @property
    def product_code(self):
        return self.__item.product_code

    @property
    def name(self):
        return self.__item.name

    @property
    def item_price(self):
        return self.__item.price

    @property
    def reorder(self):
        return self.__item.reorder

    @property
    def category_id(self):
        return self.__item.category_id

    @property
    def item(self):
        return self.__item

    @property
    def qty(self):
        return self.__qty

    @property
    def price(self):
        return self.__price
