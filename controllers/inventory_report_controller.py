from typing import Any
from database.inventory_report_db import InventoryReportDatabase


class InventoryReportController:
    def __init__(self):
        self.__database = InventoryReportDatabase()

    def get_stock_info_by_year(self, year: str):
        response = self.__database.get_stock_info_by_year(year)
        return response

    def __stock_transactions_by_year_convert_data_format(self, response: list[Any]):
        # Initialize dictionaries for each transaction type
        receive_db_values: dict[int, int] = {}
        sale_db_values: dict[int, int] = {}
        damage_loss_db_values: dict[int, int] = {}
        # Populate dictionaries from response data
        for data in response:
            month, receive, sale, damage_loss = map(int, data)
            receive_db_values[month] = receive
            sale_db_values[month] = sale
            damage_loss_db_values[month] = damage_loss
        # Initialize lists for each transaction type
        receive_values = [receive_db_values.get(i, 0) for i in range(1, 13)]
        sale_values = [sale_db_values.get(i, 0) for i in range(1, 13)]
        damage_loss_values = [
            damage_loss_db_values.get(i, 0) for i in range(1, 13)]
        return {"receive_values": receive_values, "sale_values": sale_values, "damage_loss_values": damage_loss_values}

    def get_stock_transactions_by_year(self, year: str):
        response = self.__database.get_stock_transactions_by_year(year)
        return self.__stock_transactions_by_year_convert_data_format(response)
