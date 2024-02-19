from typing import Any
from models.sale import Sale
from models.sale_detail import SaleDetail
from database.sale_db import SaleDatabase
from models.search_filter import SearchFilter
from other.helper import to_list_tuple


class SaleController:
    def __init__(self):
        self.__database = SaleDatabase()

    def __get_details(self, details_list: list[dict[str, Any]]) -> list[SaleDetail]:
        details: list[SaleDetail] = []
        for detail_dict in details_list:
            detail = SaleDetail(**detail_dict)
            details.append(detail)
        return details

    def add(self, sale_dict: dict[str, Any]):
        sale = Sale(**sale_dict)
        details = self.__get_details(sale_dict['details'])
        response = self.__database.add(sale, details)
        return response

    def modify(self, sale_dict: dict[str, Any]):
        sale = Sale(**sale_dict)
        details = self.__get_details(sale_dict['details'])
        response = self.__database.modify(
            sale, details, to_list_tuple(sale_dict['delete_ids']))
        return response

    def delete(self, id: int):
        response = self.__database.delete(id)
        return response

    def view(self, params: dict[str, Any]):
        search_filter = SearchFilter(**params)
        response = self.__database.view(search_filter)
        return response

    def view_details(self, id: int):
        response = self.__database.view_details(id)
        return response
