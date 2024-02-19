from database.dashboard_db import Dashboard
from datetime import datetime


class DashboardController:
    def __init__(self):
        self.__database = Dashboard()
        self.__today_date = str(datetime.now().date())

# Views

    def inventory_info(self):
        response = self.__database.inventory_info()
        return response

    def inventory_transactions(self, date: str):
        response = self.__database.inventory_transactions(date)
        return response

    def sales(self):
        response = self.__database.sales(self.__today_date)
        return response
