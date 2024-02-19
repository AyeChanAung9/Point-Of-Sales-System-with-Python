from typing import Any

from other.validations import *


class StoreConfiguration:

    def __init__(self, **kwargs: Any) -> None:
        self.__store_name = validate_non_empty_string(
            kwargs.get("store_name", ""), "Store name")
        self.__contact_person = kwargs.get("contact_person", "")
        self.__phone_no = validate_non_empty_string(
            kwargs.get("phone_no", ""), "Phone no")
        self.__address = validate_non_empty_string(
            kwargs.get("address", ""), "Address")
        self.__image_data = kwargs.get("image_data", b"")

    def to_tuple_db(self):
        return (self.store_name, self.contact_person, self.phone_no,
                self.address, self.image_data)

    def to_tuple_db_without_id(self):
        return (self.store_name, self.contact_person, self.phone_no,
                self.address, self.image_data)

    @property
    def store_name(self):
        return self.__store_name

    @property
    def contact_person(self):
        return self.__contact_person

    @property
    def phone_no(self):
        return self.__phone_no

    @property
    def address(self):
        return self.__address

    @property
    def image_data(self):
        return self.__image_data
