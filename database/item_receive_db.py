from typing import Any

from models.item_receive import ItemReceive
from models.item_receive_detail import ItemReceiveDetail
from models.search_filter import SearchFilter
from database.queries import *
from database.db_template import VoucherTemplate


class ItemReceiveDatabase(VoucherTemplate):

    # add, modify ,delete

    def add(self, item_receive: ItemReceive,
            item_receive_details: list[ItemReceiveDetail]):
        queries = (item_receive_add, item_receive_detail_add)
        params = item_receive.to_tuple_db_without_id()
        return super().add_detail("Item Receive", queries, params, item_receive_details)

    def modify(self, item_receive: ItemReceive,
               item_receive_details: list[ItemReceiveDetail],
               delete_ids: list[Any]):
        queries = (item_receive_modify, item_receive_detail_modify,
                   item_receive_detail_delete)
        params = item_receive.to_tuple_db()
        target_id = item_receive.item_receive_id
        return super().modify_detail("Item Receive", queries, params, item_receive_details, delete_ids, target_id)

    def delete(self, item_receive_id: int):
        query = item_receive_delete
        return super().delete_detail("Item Receive", query, item_receive_id)

    # views

    def view(self, search_filter: SearchFilter):
        queries = (item_receive_view_base, item_receive_view_where_trandate)
        return super().view_voucher(search_filter, queries)

    def view_details(self, item_receive_id: int):
        query = item_receive_detail_view_by_item_receive_id
        return super().view_voucher_details(query, item_receive_id)
