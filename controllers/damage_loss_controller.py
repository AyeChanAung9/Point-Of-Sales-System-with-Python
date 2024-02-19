from typing import Any
from other.helper import to_list_tuple

from database.damage_loss_db import DamageLossDatabase
from models.damage_loss_detail import DamageLossDetail
from models.damage_loss import DamageLoss
from models.search_filter import SearchFilter


class DamageLossController:
    def __init__(self):
        self.__database = DamageLossDatabase()

    def __get_details(self, details_list: list[dict[str, Any]]) -> list[DamageLossDetail]:
        details: list[DamageLossDetail] = []
        for detail_dict in details_list:
            detail = DamageLossDetail(**detail_dict)
            details.append(detail)
        return details

# add, modify, delete

    def add(self, damage_loss_dict: dict[str, Any]):
        damage_loss = DamageLoss(**damage_loss_dict)
        details = self.__get_details(damage_loss_dict['details'])
        response = self.__database.add(damage_loss, details)
        return response

    def modify(self, damage_loss_dict: dict[str, Any]):
        damage_loss = DamageLoss(**damage_loss_dict)
        details = self.__get_details(damage_loss_dict['details'])
        response = self.__database.modify(
            damage_loss, details, to_list_tuple(damage_loss_dict['delete_ids']))
        return response

    def delete(self, damage_loss_id: int):
        response = self.__database.delete(damage_loss_id)
        return response
# Views

    def view(self, params: dict[str, Any]):
        search_filter = SearchFilter(**params)
        response = self.__database.view(search_filter)
        return response

    def view_details(self, damage_loss_id: int):
        response = self.__database.view_details(damage_loss_id)
        return response
