from typing import Any
from database.sale_report_db import SaleReportDatabase


class SaleReportController:
    def __init__(self) -> None:
        self.__database = SaleReportDatabase()

    def get_year(self):
        response = self.__database.get_sale_year_by_year()
        return response

    def get_top_selling(self, reports_dict: dict[str, Any]):
        response = self.__database.get_top_selling_items(
            reports_dict['from_date'], reports_dict['to_date'])
        return response

    def get_items_by_total_sales(self, reports_dict: dict[str, Any]):
        response = self.__database.get_items_by_total_sales(
            reports_dict['from_date'], reports_dict['to_date'])
        return response

    def get_categories_sales_by_total_sales(self, reports_dict: dict[str, Any]):
        response = self.__database.get_categories_sales_by_total_sales(
            reports_dict['from_date'], reports_dict['to_date'])
        return response

    def get_total_sales(self, reports_dict: dict[str, Any]):
        if reports_dict['option'] == 'daily':
            response = self.__database.get_total_sales_daily(
                reports_dict['from_date'], reports_dict['to_date'])
        elif reports_dict['option'] == 'weekly':
            response = self.__database.get_total_sales_weekly(
                reports_dict['from_date'], reports_dict['to_date'])
        else:
            response = self.__database.get_total_sales_monthly(
                reports_dict['from_date'], reports_dict['to_date'])
        return response

    def get_sale_report_by_daily(self, date: str):
        response = self.__database.get_sale_report_by_daily(date)
        return response

    def get_qty_sold_by_category(self, reports_dict: dict[str, Any]):
        if reports_dict['option'] == 'daily':
            response = self.__database.get_qty_sold_by_category_daily(
                reports_dict['from_date'], reports_dict['to_date'])
        elif reports_dict['option'] == 'weekly':
            response = self.__database.get_qty_sold_by_category_weekly(
                reports_dict['from_date'], reports_dict['to_date'])
        else:
            response = self.__database.get_qty_sold_by_category_monthly(
                reports_dict['from_date'], reports_dict['to_date'])
        return response

    def get_revenue_category(self, reports_dict: dict[str, Any]):
        if reports_dict['option'] == 'daily':
            response = self.__database.get_revenue_category_daily(
                reports_dict['from_date'], reports_dict['to_date'])
        elif reports_dict['option'] == 'weekly':
            response = self.__database.get_revenue_category_weekly(
                reports_dict['from_date'], reports_dict['to_date'])
        else:
            response = self.__database.get_revenue_category_monthly(
                reports_dict['from_date'], reports_dict['to_date'])
        return response

    def get_qty_sold_by_item(self, reports_dict: dict[str, Any]):
        if reports_dict['option'] == 'daily':
            response = self.__database.get_qty_sold_by_item_daily(
                reports_dict['from_date'], reports_dict['to_date'])
        elif reports_dict['option'] == 'weekly':
            response = self.__database.get_qty_sold_by_item_weekly(
                reports_dict['from_date'], reports_dict['to_date'])
        else:
            response = self.__database.get_qty_sold_by_item_monthly(
                reports_dict['from_date'], reports_dict['to_date'])
        return response

    def get_revenue_item(self, reports_dict: dict[str, Any]):
        if reports_dict['option'] == 'daily':
            response = self.__database.get_revenue_item_daily(
                reports_dict['from_date'], reports_dict['to_date'])
        elif reports_dict['option'] == 'weekly':
            response = self.__database.get_revenue_item_weekly(
                reports_dict['from_date'], reports_dict['to_date'])
        else:
            response = self.__database.get_revenue_item_monthly(
                reports_dict['from_date'], reports_dict['to_date'])
        return response

    def get_sale_growth(self, year: str):
        response = self.__database.get_sale_growth(year)
        return response

    def get_quarterly_sale(self, year: str):
        response = self.__database.get_quarterly_sale(year)
        return response
