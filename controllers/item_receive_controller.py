
from models.search_filter import SearchFilter
from models.item_receive_detail import ItemReceiveDetail
from models.item_receive import ItemReceive
from database.item_receive_db import ItemReceiveDatabase
from typing import Any
from other.helper import to_list_tuple


class ItemReceiveController:
    def __init__(self):
        self.__database = ItemReceiveDatabase()

    def __get_details(self, details_list: list[dict[str, Any]]) -> list[ItemReceiveDetail]:
        details: list[ItemReceiveDetail] = []
        for detail_dict in details_list:
            detail = ItemReceiveDetail(**detail_dict)
            details.append(detail)
        return details

    def add(self, item_receive_dict: dict[str, Any]):
        item_receive = ItemReceive(**item_receive_dict)
        details = self.__get_details(item_receive_dict['details'])
        response = self.__database.add(item_receive, details)
        return response

    def modify(self, item_receive_dict: dict[str, Any]):
        item_receive = ItemReceive(**item_receive_dict)
        details = self.__get_details(item_receive_dict['details'])
        response = self.__database.modify(
            item_receive, details, to_list_tuple(item_receive_dict['delete_ids']))
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
