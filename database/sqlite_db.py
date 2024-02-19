import sqlite3
from typing import Any

from flask_bcrypt import generate_password_hash  # type:ignore
from database.context_manager import DatabaseContextManager
from database.queries import *


class POSDatabase:

    def setUp(self):
        logo_image = self.__read_default_image()
        self.__create_tables_reads_triggers()
        self.__add_default_data(logo_image)

        # temp
        self.__add_sample_data()

    def __create_tables_reads_triggers(self):
        with DatabaseContextManager() as cursor:

            # tables
            cursor.execute(user_roles_tbl)
            cursor.execute(users_tbl)
            cursor.execute(user_role_permissions_tbl)
            cursor.execute(category_tbl)
            cursor.execute(item_tbl)
            cursor.execute(item_receive_tbl)
            cursor.execute(item_receive_details_tbl)
            cursor.execute(damage_loss_tbl)
            cursor.execute(damage_loss_details_tbl)
            cursor.execute(sale_tbl)
            cursor.execute(sale_details_tbl)
            cursor.execute(store_config_tbl)
            cursor.execute(log_tbl)

            # views
            cursor.execute(view_for_item_category)
            cursor.execute(view_for_item_and_stock)
            cursor.execute(view_for_item_receive_user)
            cursor.execute(view_for_item_receive_detail_item)
            cursor.execute(view_for_damage_loss_user)
            cursor.execute(view_for_damage_loss_detail_item)
            cursor.execute(view_for_user)
            cursor.execute(view_for_sale_user)
            cursor.execute(view_for_sale_detail_item)
            cursor.execute(view_for_item_receive_and_details)
            cursor.execute(view_for_damage_loss_and_details)
            cursor.execute(view_for_sale_and_details)
            cursor.execute(view_for_transaction_date)
            cursor.execute(view_for_daily_stock_transaction)
            cursor.execute(view_for_stock_transaction_by_item)
            cursor.execute(view_for_log)

            # triggers
            cursor.execute(item_receive_after_insert_trigger)
            cursor.execute(item_receive_after_update_trigger)
            cursor.execute(item_receive_after_delete_trigger)
            cursor.execute(damage_loss_after_insert_trigger)
            cursor.execute(damage_loss_after_update_trigger)
            cursor.execute(damage_loss_after_delete_trigger)
            cursor.execute(sale_after_insert_trigger)
            cursor.execute(sale_after_update_trigger)
            cursor.execute(sale_after_delete_trigger)

    def __add_default_data(self, image_data: bytes):
        with DatabaseContextManager() as cursor:
            cursor.execute(
                "INSERT OR IGNORE INTO store_config_tbl (store_name, contact_person, phone_no, address, image_data) VALUES (?, ?, ?, ?, ?)",
                ('ABC', 'Kyaw Kyaw', '095329753', 'Yangon', image_data))
            cursor.execute(
                "INSERT OR IGNORE INTO user_roles_tbl (role_id, role_name) VALUES (1, 'Admin')")
            admin_hashed_password = generate_password_hash('123456')
            cursor.execute(
                "INSERT OR IGNORE INTO users_tbl (user_id, username , password , role_id) VALUES (?, ?, ?, ?)", (1, 'admin', admin_hashed_password, 1))
            cursor.executemany('INSERT OR IGNORE INTO user_role_permissions_tbl (role_id, permission_name) VALUES (?,?)',
                               [(1, 'item_read',), (1, 'item_write',), (1, 'item_delete',),
                                (1, 'category_read',), (1, 'category_write',
                                                        ), (1, 'category_delete',),
                                (1, 'item_receive_read',), (1, 'item_receive_write',
                                                            ), (1, 'item_receive_delete',),
                                (1, 'damage_loss_read',), (1, 'damage_loss_write',
                                                           ), (1, 'damage_loss_delete',),
                                (1, 'sales_read',), (1, 'sales_write',
                                                     ), (1, 'sales_delete',),
                                (1, 'reports',), (1, 'users',), (1, 'user_roles',), (1, 'user_permissions',), (1, 'store_configuration')])

    def __add_sample_data(self):
        with DatabaseContextManager() as cursor:
            cursor.execute(
                "INSERT OR IGNORE INTO category_tbl (category_id, category_name) VALUES(1, 'Cosmetics')")
            cursor.execute(
                "INSERT OR IGNORE INTO category_tbl (category_id, category_name) VALUES(2, 'Electronics')")
            cursor.execute(
                "INSERT OR IGNORE INTO category_tbl (category_id, category_name) VALUES(3, 'Kitchen')")
            cursor.execute(
                "INSERT OR IGNORE INTO item_tbl (item_id, product_code,name,price,reorder,category_id, cost_price) VALUES (1, 'C001','Face Cleanser',45000,10,1,40000)"
            )
            cursor.execute(
                "INSERT OR IGNORE INTO item_tbl (item_id, product_code,name,price,reorder,category_id, cost_price) VALUES (2, 'C002','Serum',123000,20,1,120000)"
            )
            cursor.execute(
                "INSERT OR IGNORE INTO item_tbl (item_id, product_code,name,price,reorder,category_id, cost_price) VALUES (3, 'C003','Toner',65000,15,1,62000)"
            )
            cursor.execute(
                "INSERT OR IGNORE INTO item_tbl (item_id, product_code,name,price,reorder,category_id, cost_price) VALUES (4, 'E001','Hair Dryer',25000,5,2,23000)"
            )
            cursor.execute(
                "INSERT OR IGNORE INTO item_tbl (item_id, product_code,name,price,reorder,category_id, cost_price) VALUES (5, 'E002','Power Bank',40000,10,2,35000)"
            )
            cursor.execute(
                "INSERT OR IGNORE INTO item_tbl (item_id, product_code,name,price,reorder,category_id, cost_price) VALUES (6, 'K001','Knife',12000,10,3,10000)"
            )

    def __read_default_image(self):
        with open('static/img/pos_logo.png', "rb") as img_file:
            binary_image = img_file.read()
            return binary_image


def __get_column_name(cursor: sqlite3.Cursor):
    return [description[0] for description in cursor.description]


def __convert_dict(column_names: list[Any],
                   data: Any) -> dict[Any, Any]:
    data_dict = {}
    for i in range(len(column_names)):
        data_dict[column_names[i]] = data[i]
    return data_dict  # type: ignore


def data_list_to_dict(data: list[Any], cursor: sqlite3.Cursor, no_column_name: bool = False) -> Any:
    column_names = __get_column_name(cursor)
    dict_list: Any = []
    for row in data:
        dict_list.append(
            row[0] if no_column_name else __convert_dict(column_names, row))
    return dict_list


def data_to_dict(data: Any, cursor: sqlite3.Cursor) -> Any:
    column_names = __get_column_name(cursor)
    return __convert_dict(column_names, data)
