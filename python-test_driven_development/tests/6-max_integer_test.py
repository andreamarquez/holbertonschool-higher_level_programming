#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_one_element(self):
        self.assertEqual(max_integer([4]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_all_same_numbers(self):
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_floats(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

    def test_mixed_ints_and_floats(self):
        self.assertEqual(max_integer([1, 2.2, 3, 4.4]), 4.4)

    def test_single_negative_number(self):
        self.assertEqual(max_integer([-4]), -4)

    def test_large_numbers(self):
        self.assertEqual(max_integer([
            1000000000,
            2000000000,
            3000000000,
            4000000000]), 4000000000)


if __name__ == '__main__':
    unittest.main()
