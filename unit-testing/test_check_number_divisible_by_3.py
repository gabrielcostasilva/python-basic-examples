import unittest
from check_number_disible_by_3 import check

class TestCheckNumberDivisibleBy3(unittest.TestCase):
    def test_number(self):
        self.assertTrue(check(9))

    def test_is_input_number(self):
        with self.assertRaises(Exception):
            check("john")
