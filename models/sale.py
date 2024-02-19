from typing import Any

from other.validations import *


class Sale:

    def __init__(self, **kwargs: Any) -> None:
        self.__sale_id = kwargs.get("sale_id", "0")
        self.__voucher_no = validate_voucher_no(kwargs.get("voucher_no", ""))
        self.__tran_date = validate_trans_date(kwargs.get("tran_date", ""))
        self.__total_items = validate_number(
            kwargs.get("total_items", "0"), "Total items")
        self.__user_id = validate_number_greater_than_zero(
            kwargs.get("user_id", "0"), "User ID")
        self.__discount = validate_number(
            kwargs.get("discount", "0.0"), "Discount")
        self.__total_amount = validate_number(
            kwargs.get("total_amount", "0.0"), "Total amount")
        self.__discount_percentage = validate_number(
            kwargs.get("discount_percentage", "0"), "Discount Percentage")
        self.__payment = kwargs.get("payment", "")

    def to_tuple_db(self):
        return (self.voucher_no, self.tran_date, self.total_items,
                self.user_id, self.discount, self.total_amount, self.discount_percentage, self.payment, self.sale_id)

    def to_tuple_db_without_id(self):
        return (self.voucher_no, self.tran_date, self.total_items,
                self.user_id, self.discount, self.total_amount, self.discount_percentage, self.payment)

    @property
    def sale_id(self):
        return self.__sale_id

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

    @property
    def discount(self):
        return self.__discount

    @property
    def total_amount(self):
        return self.__total_amount

    @property
    def discount_percentage(self):
        return self.__discount_percentage

    @property
    def payment(self):
        return self.__payment
