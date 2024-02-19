from database.queries import *
from database.context_manager import DatabaseContextManager
from database.sqlite_db import data_to_dict


class Dashboard:

    # inventory

    def inventory_info(self):
        with DatabaseContextManager() as cursor:
            cursor.execute(inventory_overview)
            data = cursor.fetchone()
            assert data, f"Cannot fetch inventory data!"
            inventory_view = data_to_dict(data, cursor)
        return inventory_view

    # stock transactions

    def inventory_transactions(self, date: str):
        with DatabaseContextManager() as cursor:
            cursor.execute(transaction_qty, (date, date))
            data = cursor.fetchone()
            assert data, f"Cannot fetch transactions!"
            transactions = data_to_dict(data, cursor)
        return transactions

    # sales

    def sales(self, date: str):
        with DatabaseContextManager() as cursor:
            cursor.execute(sales_overview, (date, date, date, date))
            data = cursor.fetchone()
            assert data, f"Cannot fetch sales!"
            sales = data_to_dict(data, cursor)
        return sales
