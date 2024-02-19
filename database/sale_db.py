from typing import Any

from models.search_filter import SearchFilter
from models.sale import Sale
from models.sale_detail import SaleDetail
from database.queries import *
from database.db_template import VoucherTemplate


class SaleDatabase(VoucherTemplate):

    def add(self, sale: Sale, sale_details: list[SaleDetail]):
        queries = (sale_add, sale_detail_add)
        params = sale.to_tuple_db_without_id()
        return super().add_detail("Sale", queries, params, sale_details)

    def modify(self, sale: Sale, sale_details: list[SaleDetail], delete_ids: list[Any]):
        queries = (sale_modify, sale_detail_modify, sale_detail_delete)
        params = sale.to_tuple_db()
        target_id = sale.sale_id
        return super().modify_detail("Sale", queries, params, sale_details, delete_ids, target_id)

    def delete(self, sale_id: int):
        query = sale_delete
        return super().delete_detail("Sale", query, sale_id)

    # views
    def view(self, search_filter: SearchFilter):
        queries = (sale_view_base, sale_view_where_trandate)
        return super().view_voucher(search_filter, queries)

    def view_details(self, sale_id: int):
        query = sale_detail_view_by_sale_id
        return super().view_voucher_details(query, sale_id)
