from models.item import Item
from models.search_filter import SearchFilter
from database.queries import *
from database.context_manager import DatabaseContextManager
from database.db_template import DatabaseTemplate
from database.sqlite_db import data_list_to_dict, data_to_dict


class ItemDatabase(DatabaseTemplate):

    # add, modify, delete
    def add(self, item: Item):
        query = item_add
        params = (item.product_code, item.name,
                  item.price, item.reorder, item.category_id, item.cost_price)
        return super().add_execute(item.name, query, params)

    def modify(self, item: Item):
        query = item_modify
        params = (item.product_code, item.name,
                  item.price, item.reorder, item.category_id, item.cost_price, item.item_id)
        return super().modify_execute(item.name, query, params)

    def delete(self, item_id: int):
        query = item_delete
        return super().delete_execute("Item", query, item_id)

    # Views
    def view(self, search_filter: SearchFilter):
        with DatabaseContextManager() as cursor:
            search = f"%{search_filter.search_keyword}%"
            if search_filter.filter_id:
                cursor.execute(item_view_by_category,
                               (search, search, search_filter.filter_id))
            else:
                cursor.execute(item_view_by_keyword, (search, search))
            data = cursor.fetchall()
            items = data_list_to_dict(data, cursor)
        return items

    def get_by_product_code(self, product_code: str):
        with DatabaseContextManager() as cursor:
            cursor.execute(item_view_by_product_code, (product_code,))
            data = cursor.fetchone()
            assert data, f"Item({product_code}) not found!"
            item = data_to_dict(data, cursor)
        return item
