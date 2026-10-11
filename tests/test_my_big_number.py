import os
import sys
import unittest

# Them thu muc src vao sys.path de import duoc MyBigNumber
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from my_big_number import MyBigNumber


class TestMyBigNumber(unittest.TestCase):

    def setUp(self):
        self.calculator = MyBigNumber()

    def test_example_in_requirement(self):
        self.assertEqual(self.calculator.sum("1234", "897"), "2131")

    def test_first_number_shorter(self):
        self.assertEqual(self.calculator.sum("897", "1234"), "2131")

    def test_same_length_no_carry(self):
        self.assertEqual(self.calculator.sum("123", "456"), "579")

    def test_carry_at_last_digit(self):
        self.assertEqual(self.calculator.sum("999", "1"), "1000")

    def test_single_digit(self):
        self.assertEqual(self.calculator.sum("5", "7"), "12")

    def test_with_zero(self):
        self.assertEqual(self.calculator.sum("0", "0"), "0")
        self.assertEqual(self.calculator.sum("12345", "0"), "12345")

    def test_big_numbers(self):
        stn1 = "123456789012345678901234567890"
        stn2 = "987654321098765432109876543210"
        expected = "1111111110111111111011111111100"
        self.assertEqual(self.calculator.sum(stn1, stn2), expected)


if __name__ == "__main__":
    unittest.main()
