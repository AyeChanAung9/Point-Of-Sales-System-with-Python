from database.context_manager import DatabaseContextManager
from models.search_filter import SearchFilter
from database.sqlite_db import data_list_to_dict
from typing import Any


class DatabaseTemplate:

    def add_execute(self, obj_name: str, query: str, params: tuple[str, ...]):
        with DatabaseContextManager() as cursor:
            cursor.execute(query, params)
            obj_id = cursor.lastrowid
            assert obj_id is not None, f"Failed to add {obj_name}!"
        return f"{obj_name} added successfully"

    def modify_execute(self, obj_name: str, query: str, params: tuple[str, ...]):
        with DatabaseContextManager() as cursor:
            cursor.execute(query, params)
            modified_row = cursor.rowcount
            assert modified_row > 0, f"Failed to modify {obj_name: str}!"
        return f"{obj_name} updated successfully"

    def delete_execute(self, name: str, query: str, obj_id: int):
        with DatabaseContextManager() as cursor:
            cursor.execute(query, (obj_id,))
            delete_row = cursor.rowcount
            assert delete_row > 0, f"Failed to delete {name}!"
        return f"{name}is deleted successfully"

    def get_data_list(self, query: str):
        with DatabaseContextManager() as cursor:
            cursor.execute(query)
            data = cursor.fetchall()
            data_list = data_list_to_dict(data, cursor)
        return data_list


class VoucherTemplate:

    def add_detail(self, voucher_name: str, queries: tuple[str, ...], params: tuple[str, ...], detail_params: Any):
        with DatabaseContextManager() as cursor:
            cursor.execute(queries[0], params)
            detail_id = cursor.lastrowid
            assert detail_id is not None, f"Failed to add {voucher_name} voucher!"
            details_data = [detail.to_tuple_db_without_id(
                detail_id) for detail in detail_params]
            cursor.executemany(queries[1], details_data)
        return f"{voucher_name} voucher added successfully"

    def modify_detail(self, voucher_name: str, queries: tuple[str, ...], params: tuple[str, ...], detail_params: Any, delete_ids: list[Any], target_id: str):
        with DatabaseContextManager() as cursor:
            cursor.execute(queries[0], params)
            modified_row = cursor.rowcount
            assert modified_row > 0, f"Failed to modify {voucher_name} voucher!"
            details_data = [detail.to_tuple_db(
                target_id) for detail in detail_params]
            cursor.executemany(queries[1], details_data)
            cursor.executemany(queries[2], delete_ids)
        return f"{voucher_name} voucher modified successfully"

    def delete_detail(self, name: str, query: str, obj_id: int):
        with DatabaseContextManager() as cursor:
            cursor.execute(query, (obj_id,))
            delete_row = cursor.rowcount
            assert delete_row > 0, f"Failed to delete {name}!"
        return f"{name} voucher deleted successfully"

    def view_voucher(self, search_filter: SearchFilter, queries: tuple[str, ...]):
        with DatabaseContextManager() as cursor:
            params = (f'%{search_filter.search_keyword}%', )
            query = queries[0]
            if search_filter.from_tran_date != '' and search_filter.to_tran_date != '':
                query = query + queries[1]
                params = params + (search_filter.from_tran_date, )
                params = params + (search_filter.to_tran_date, )
            cursor.execute(query, params)
            data = cursor.fetchall()
            voucher_list = data_list_to_dict(data, cursor)
        return voucher_list

    def view_voucher_details(self, query: str, detail_id: int):
        with DatabaseContextManager() as cursor:
            cursor.execute(query, (detail_id,))
            data = cursor.fetchall()
            details = data_list_to_dict(data, cursor)
        return details
