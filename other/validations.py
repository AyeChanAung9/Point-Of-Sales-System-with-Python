
from typing import Any
import re

__date_format = '%Y-%m-%d'


def __validate_non_empty(value: Any, field_name: str):
    if not value:
        raise ValueError(f"{field_name} cannot be empty.")


def __validate_min_length(value: Any, min_length: int, field_name: str):
    if len(value) < min_length:
        raise ValueError(
            f"{field_name} must be at least {min_length} characters long.")


def __validate_max_length(value: Any, max_length: int, field_name: str):
    if len(value) > max_length:
        raise ValueError(
            f"{field_name} cannot exceed {max_length} characters.")


def __is_float(value: str):
    try:
        float(value)
        return True
    except ValueError:
        return False


def __convert_float(value: Any, field_name: str):
    if isinstance(value, str) and not __is_float(value):
        raise ValueError(f"{field_name} must be a number.")
    return float(value)


def __change_formatted_number(value: Any):
    if isinstance(value, str):
        return value.replace(',', '')
    return value


def __validate_non_negative(value: Any, field_name: str):
    if value < 0:
        raise ValueError(f"{field_name} must be a non-negative.")


def __validate_greater_than_zero(value: Any, field_name: str):
    if value < 0:
        raise ValueError(f"{field_name} must be greater than zero.")


def __validate_date(value: Any, field_name: str):
    date_pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
    if not date_pattern.match(value):
        raise ValueError(
            f"Invalid {field_name} format. Please use the following date format: {__date_format}.")
    return value


def validate_code(value: Any, field_name: str):
    __validate_non_empty(value, field_name)
    __validate_max_length(value, 10, field_name)
    return value


def validate_voucher_no(value: Any):
    __validate_max_length(value, 25, "Voucher no.")
    return value


def validate_remark(value: Any):
    __validate_max_length(value, 50, "Remark")
    return value


def validate_trans_date(value: Any):
    field_name = "Transaction date"
    __validate_non_empty(value, field_name)
    __validate_date(value, field_name)
    return value


def validate_trans_date_allow_empty(value: Any):
    if value:
        __validate_date(value, "Transaction date")
    return value


def validate_password(value: Any):
    field_name = "Password"
    __validate_non_empty(value, field_name)
    __validate_min_length(value, 3, field_name)
    __validate_max_length(value, 15, field_name)
    return value


def validate_non_empty_string(value: Any, field_name: str):
    __validate_non_empty(value, field_name)
    __validate_max_length(value, 30, field_name)
    return value


def validate_string(value: Any, field_name: str):
    if value:
        __validate_max_length(value, 30, field_name)
    return value


def validate_price(value: Any):
    value = __change_formatted_number(value)
    field_name = "Price"
    __validate_non_empty(value, field_name)
    float_value = __convert_float(value, field_name)
    __validate_non_negative(float_value, field_name)
    return value


def validate_float_number(value: Any, field_name: str):
    value = __change_formatted_number(value)
    __validate_non_empty(value, field_name)
    float_value = __convert_float(value, field_name)
    __validate_non_negative(float_value, field_name)
    return value


def validate_number(value: Any, field_name: str):
    value = __change_formatted_number(value)
    __validate_non_empty(value, field_name)
    float_value = __convert_float(value, field_name)
    __validate_non_negative(float_value, field_name)
    return value


def validate_number_greater_than_zero(value: Any, field_name: str):
    value = __change_formatted_number(value)
    __validate_non_empty(value, field_name)
    float_value = __convert_float(value, field_name)
    __validate_greater_than_zero(float_value, field_name)
    return value
