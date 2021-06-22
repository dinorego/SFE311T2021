import unittest
from expanded_form import expanded_form

class lab_tests(unittest.TestCase):
    def test_invalid_negative_nums(self):
        self.assertEqual(expanded_form(-1),"-0 + 1")
        self.assertEqual(expanded_form(-149),"-000 + 100 + 40 + 9")

    def test_zero_input(self):
        self.assertEqual(expanded_form(0),"0")
    def test_one(self):
        self.assertEqual(expanded_form(1),"1")
    def test_two_digits(self):
        self.assertEqual(expanded_form(90),"90")
    def test_three_digits(self):
        self.assertEqual(expanded_form(689),"600 + 80 + 9")
    def test_five_digits(self):
        self.assertEqual(expanded_form(38844),"30000 + 8000 + 800 + 40 + 4")

if __name__ == '__main__':   
    unittest.main()