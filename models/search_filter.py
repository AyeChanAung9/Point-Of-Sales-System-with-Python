from typing import Any

from other.validations import *


class SearchFilter:

    def __init__(self, **kwargs: Any):
        self.__page_no = kwargs.get('page_no', 1)
        self.__search_keyword = kwargs.get('search_keyword', '')
        self.__filter_id = kwargs.get('filter_id', '')
        self.__from_tran_date = validate_trans_date_allow_empty(
            kwargs.get('from_tran_date', ''))
        self.__to_tran_date = validate_trans_date_allow_empty(
            kwargs.get('to_tran_date', ''))

    def start_row_no(self, batch_size: int):
        return (self.__page_no - 1) * batch_size

    @property
    def page_no(self):
        return self.__page_no

    @property
    def search_keyword(self):
        return self.__search_keyword

    @property
    def filter_id(self):
        return self.__filter_id

    @property
    def from_tran_date(self):
        return self.__from_tran_date

    @property
    def to_tran_date(self):
        return self.__to_tran_date
