from typing import Any

from other.validations import validate_non_empty_string, validate_string

category_name_validate_fun = {
    "true": validate_string, "": validate_non_empty_string}


class Category:
    def __init__(self, **kwargs: Any) -> None:
        self.__category_id = kwargs.get('category_id', "0")
        self.__category_name = category_name_validate_fun[kwargs.get('category_name_can_empty', "")](
            kwargs.get('category_name', ''), "Category Name")

    def is_modify(self):
        return (isinstance(self.category_id, int) and self.category_id > 0) or int(self.category_id) > 0

    @property
    def category_id(self):
        return self.__category_id

    @property
    def category_name(self):
        return self.__category_name
