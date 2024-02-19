from typing import Any
from models.item import Item

from other.validations import *


class ItemReceiveDetail:
    def __init__(self, **kwargs: Any) -> None:
        self.__item_receive_details_id = kwargs.get("item_receive_details_id")
        self.__item_receive_id = validate_number(
            kwargs.get("item_receive_id", "0"), "Item Receive ID")
        self.__item = Item(**kwargs)
        self.__qty = validate_number_greater_than_zero(
            kwargs.get("qty", "0"), "Quantity")

    def to_tuple_db(self, item_receive_id: int):
        return (self.item_receive_details_id, item_receive_id, self.item_id, self.qty)

    def to_tuple_db_without_id(self, item_receive_id: int):
        return (item_receive_id, self.item_id, self.qty)

    @property
    def item_receive_details_id(self):
        return self.__item_receive_details_id

    @property
    def item_receive_id(self):
        return self.__item_receive_id

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
    def price(self):
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
