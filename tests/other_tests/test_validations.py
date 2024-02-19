import unittest
from other.validations import (
    validate_code,
    validate_voucher_no,
    validate_remark,
    validate_trans_date,
    validate_trans_date_allow_empty,
    validate_password,
    validate_non_empty_string,
    validate_string,
    validate_price,
    validate_number,
    validate_number_greater_than_zero,
)


class TestValidations(unittest.TestCase):
    def test_validate_code(self):
        self.assertEqual(validate_code("ABC123", "Code"), "ABC123")
        with self.assertRaises(ValueError):
            validate_code("", "Code")
        with self.assertRaises(ValueError):
            validate_code("ABCDEFGHIJK", "Code")

    def test_validate_voucher_no(self):
        self.assertEqual(validate_voucher_no(
            "12345VCHR67890"), "12345VCHR67890")
        with self.assertRaises(ValueError):
            validate_voucher_no(
                "2222333344544532324562435430934589890452380234589234852458204357245720934572049572340957209348572903457290384572903457290345")

    def test_validate_remark(self):
        self.assertEqual(validate_remark(
            "This is a remark."), "This is a remark.")
        with self.assertRaises(ValueError):
            validate_remark("A" * 51)

    def test_validate_trans_date(self):
        self.assertEqual(validate_trans_date("2023-11-15"), "2023-11-15")
        with self.assertRaises(ValueError):
            validate_trans_date("2023/11/150")  # Invalid date format
        with self.assertRaises(ValueError):
            validate_trans_date("")  # Empty date

    def test_validate_trans_date_allow_empty(self):
        self.assertEqual(validate_trans_date_allow_empty(
            "2023-11-15"), "2023-11-15")

    def test_validate_password(self):
        self.assertEqual(validate_password("secure123"), "secure123")
        with self.assertRaises(ValueError):
            validate_password("")  # Empty password
        with self.assertRaises(ValueError):
            validate_password("12")  # Password too short
        with self.assertRaises(ValueError):
            validate_password("A" * 16)  # Password too long

    def test_validate_non_empty_string(self):
        self.assertEqual(validate_non_empty_string("Hello", "Field"), "Hello")
        with self.assertRaises(ValueError):
            validate_non_empty_string("", "Field")
        with self.assertRaises(ValueError):
            validate_non_empty_string("A" * 31, "Field")

    def test_validate_string(self):
        self.assertEqual(validate_string("Hello", "Field"), "Hello")

        with self.assertRaises(ValueError):
            validate_string("A" * 31, "Field")

    def test_validate_price(self):
        self.assertEqual(validate_price("19.99"), "19.99")
        with self.assertRaises(ValueError):
            validate_price("")  # Empty price
        with self.assertRaises(ValueError):
            validate_price("-10.5")  # Negative price

    def test_validate_number(self):
        self.assertEqual(validate_number("42", "Field"), "42")
        with self.assertRaises(ValueError):
            validate_number("", "Field")  # Empty number
        with self.assertRaises(ValueError):
            validate_number("-5", "Field")  # Negative number

    def test_validate_number_greater_than_zero(self):
        self.assertEqual(
            validate_number_greater_than_zero("42", "Field"), "42")
        with self.assertRaises(ValueError):
            validate_number_greater_than_zero("", "Field")  # Empty number
        with self.assertRaises(ValueError):
            validate_number_greater_than_zero("-5", "Field")  # Negative number
        with self.assertRaises(ValueError):
            validate_number_greater_than_zero(
                0, "Field")  # Non-positive number


if __name__ == "__main__":
    unittest.main()
