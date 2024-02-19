from database.queries import *
from database.context_manager import DatabaseContextManager
from database.sqlite_db import data_to_dict


class InventoryReportDatabase:

    def get_stock_info_by_year(self, year: str):
        with DatabaseContextManager() as cursor:
            cursor.execute(get_stock_info_by_year, (year,))
            data = cursor.fetchone()
            assert data, f"Inventory stock info for {year} not found!"
            report_details = data_to_dict(data, cursor)
        return report_details

    def get_stock_transactions_by_year(self, year: str):
        with DatabaseContextManager() as cursor:
            cursor.execute(get_stock_transactions_by_year, (year, ))
            data = cursor.fetchall()
        return data
