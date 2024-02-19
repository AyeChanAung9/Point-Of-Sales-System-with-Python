import unittest
from typing import Any


def run_test(test_class: Any, test_name: str):
    test_suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print("----------------------------------------------------------------------")
    print(f"Testing {test_name} ")
    unittest.TextTestRunner().run(test_suite)
