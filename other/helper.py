from typing import Any
import os


def to_list_tuple(data: list[Any]):
    return [(ele, ) for ele in data]


def to_list_tuple_with_id(id: int, data: list[Any]):
    return [(id, ele) for ele in data]


def delete_file(file_name: str):
    if os.path.exists(file_name):
        os.remove(file_name)
