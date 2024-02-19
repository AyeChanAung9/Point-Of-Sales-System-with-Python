from typing import Any

from other.validations import *


class DamageLoss:
    def __init__(self, **kwargs: Any) -> None:
        self.__damage_loss_id = kwargs.get("damage_loss_id", "0")
        self.__voucher_no = validate_voucher_no(kwargs.get("voucher_no", ''))
        self.__tran_date = validate_trans_date(kwargs.get("tran_date", ''))
        self.__total_items = validate_number(
            kwargs.get("total_items", "0"), "Total items")
        self.__user_id = validate_number_greater_than_zero(
            kwargs.get("user_id", "0"), "User ID")

    def to_tuple_db(self):
        return (self.voucher_no, self.tran_date, self.total_items, self.user_id, self.damage_loss_id)

    def to_tuple_db_without_id(self):
        return (self.voucher_no, self.tran_date, self.total_items, self.user_id)

    @property
    def damage_loss_id(self):
        return self.__damage_loss_id

    @property
    def voucher_no(self):
        return self.__voucher_no

    @property
    def tran_date(self):
        return self.__tran_date

    @property
    def total_items(self):
        return self.__total_items

    @property
    def user_id(self):
        return self.__user_id
