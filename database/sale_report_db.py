from database.queries import *
from database.context_manager import DatabaseContextManager
from database.sqlite_db import data_list_to_dict


class SaleReportDatabase:

    # sale report
    def get_sale_year_by_year(self):
        with DatabaseContextManager() as cursor:
            cursor.execute(get_sale_year_by_year)
            data = cursor.fetchall()
            sale_details = data_list_to_dict(data, cursor)
        return sale_details

    def get_top_selling_items(self, from_date: str, to_date: str):
        with DatabaseContextManager() as cursor:
            cursor.execute(get_top_selling_items, (from_date, to_date,))
            data = cursor.fetchall()
            sale_report = data_list_to_dict(data, cursor)
        return sale_report

    def get_categories_sales_by_total_sales(self, from_date: str, to_date: str):
        with DatabaseContextManager() as cursor:
            cursor.execute(get_categories_sales_by_total_sales,
                           (from_date, to_date,))
            data = cursor.fetchall()
            sale_report = data_list_to_dict(data, cursor)
        return sale_report

    def get_items_by_total_sales(self, from_date: str, to_date: str):
        with DatabaseContextManager() as cursor:
            cursor.execute(get_items_by_total_sales, (from_date, to_date,))
            data = cursor.fetchall()
            sale_report = data_list_to_dict(data, cursor)
        return sale_report

    # get_total_sales_by_month
    def get_total_sales_monthly(self, from_date: str, to_date: str):
        with DatabaseContextManager() as cursor:
            cursor.execute(get_total_sales_monthly, (from_date, to_date,))
            data = cursor.fetchall()
            sale_report = data_list_to_dict(data, cursor)
        return sale_report

    def get_total_sales_daily(self, from_date: str, to_date: str):
        with DatabaseContextManager() as cursor:
            cursor.execute(get_total_sales_daily, (from_date, to_date,))
            data = cursor.fetchall()
            sale_report = data_list_to_dict(data, cursor)
        return sale_report

    def get_total_sales_weekly(self, from_date: str, to_date: str):
        with DatabaseContextManager() as cursor:
            cursor.execute(get_total_sales_weekly, (from_date, to_date,))
            data = cursor.fetchall()
            sale_report = data_list_to_dict(data, cursor)
        return sale_report

    def get_sale_report_by_daily(self, date: str):
        with DatabaseContextManager() as cursor:
            cursor.execute(get_sale_report_by_daily, (date,))
            data = cursor.fetchall()
            sale_report = data_list_to_dict(data, cursor)
        return sale_report

    def get_qty_sold_by_category_daily(self, from_date: str, to_date: str):
        with DatabaseContextManager() as cursor:
            cursor.execute(get_qty_sold_by_category_daily,
                           (from_date, to_date,))
            data = cursor.fetchall()
            sale_report = data_list_to_dict(data, cursor)
        return sale_report

    def get_qty_sold_by_category_weekly(self, from_date: str, to_date: str):
        with DatabaseContextManager() as cursor:
            cursor.execute(get_qty_sold_by_category_weekly,
                           (from_date, to_date,))
            data = cursor.fetchall()
            sale_report = data_list_to_dict(data, cursor)
        return sale_report

    def get_qty_sold_by_category_monthly(self, from_date: str, to_date: str):
        with DatabaseContextManager() as cursor:
            cursor.execute(get_qty_sold_by_category_monthly,
                           (from_date, to_date,))
            data = cursor.fetchall()
            sale_report = data_list_to_dict(data, cursor)
        return sale_report

    def get_revenue_category_daily(self, from_date: str, to_date: str):
        with DatabaseContextManager() as cursor:
            cursor.execute(get_revenue_category_daily, (from_date, to_date,))
            data = cursor.fetchall()
            sale_report = data_list_to_dict(data, cursor)
        return sale_report

    def get_revenue_category_weekly(self, from_date: str, to_date: str):
        with DatabaseContextManager() as cursor:
            cursor.execute(get_revenue_category_weekly, (from_date, to_date,))
            data = cursor.fetchall()
            sale_report = data_list_to_dict(data, cursor)
        return sale_report

    def get_revenue_category_monthly(self, from_date: str, to_date: str):
        with DatabaseContextManager() as cursor:
            cursor.execute(get_revenue_category_monthly, (from_date, to_date,))
            data = cursor.fetchall()
            sale_report = data_list_to_dict(data, cursor)
        return sale_report

    def get_qty_sold_by_item_daily(self, from_date: str, to_date: str):
        with DatabaseContextManager() as cursor:
            cursor.execute(get_qty_sold_by_item_daily, (from_date, to_date,))
            data = cursor.fetchall()
            sale_report = data_list_to_dict(data, cursor)
        return sale_report

    def get_qty_sold_by_item_weekly(self, from_date: str, to_date: str):
        with DatabaseContextManager() as cursor:
            cursor.execute(get_qty_sold_by_item_weekly, (from_date, to_date,))
            data = cursor.fetchall()
            sale_report = data_list_to_dict(data, cursor)
        return sale_report

    def get_qty_sold_by_item_monthly(self, from_date: str, to_date: str):
        with DatabaseContextManager() as cursor:
            cursor.execute(get_qty_sold_by_item_monthly, (from_date, to_date,))
            data = cursor.fetchall()
            sale_report = data_list_to_dict(data, cursor)
        return sale_report

    def get_revenue_item_daily(self, from_date: str, to_date: str):
        with DatabaseContextManager() as cursor:
            cursor.execute(get_revenue_item_daily, (from_date, to_date,))
            data = cursor.fetchall()
            sale_report = data_list_to_dict(data, cursor)
        return sale_report

    def get_revenue_item_weekly(self, from_date: str, to_date: str):
        with DatabaseContextManager() as cursor:
            cursor.execute(get_revenue_item_weekly, (from_date, to_date,))
            data = cursor.fetchall()
            sale_report = data_list_to_dict(data, cursor)
        return sale_report

    def get_revenue_item_monthly(self, from_date: str, to_date: str):
        with DatabaseContextManager() as cursor:
            cursor.execute(get_revenue_item_monthly, (from_date, to_date,))
            data = cursor.fetchall()
            sale_report = data_list_to_dict(data, cursor)
        return sale_report

    def get_sale_growth(self, year: str):
        with DatabaseContextManager() as cursor:
            cursor.execute(get_sale_growth, (year, year,))
            data = cursor.fetchall()
            sale_report = data_list_to_dict(data, cursor)
        return sale_report

    def get_quarterly_sale(self, year: str):
        with DatabaseContextManager() as cursor:
            cursor.execute(get_quarterly_sale, (year,))
            data = cursor.fetchall()
            sale_report = data_list_to_dict(data, cursor)
        return sale_report
