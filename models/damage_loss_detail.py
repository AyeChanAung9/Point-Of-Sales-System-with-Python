from typing import Any
from models.item import Item

from other.validations import *


class DamageLossDetail:
    def __init__(self, **kwargs: Any) -> None:
        self.__damage_loss_details_id = kwargs.get("damage_loss_details_id")
        self.__damage_loss_id = validate_number(
            kwargs.get("damage_loss_id", "0"), "Damage Loss ID")
        self.__item = Item(**kwargs)
        self.__qty = validate_number_greater_than_zero(
            kwargs.get("qty", "0"), "Quantity")
        self.__remark = validate_remark(kwargs.get("remark", ''))

    def to_tuple_db(self, damage_loss_id: int):
        return (self.damage_loss_details_id, damage_loss_id, self.item_id, self.qty, self.remark)

    def to_tuple_db_without_id(self, damage_loss_id: int):
        return (damage_loss_id, self.item_id, self.qty, self.remark)

    @property
    def damage_loss_details_id(self):
        return self.__damage_loss_details_id

    @property
    def damage_loss_id(self):
        return self.__damage_loss_id

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

    @property
    def remark(self):
        return self.__remark
