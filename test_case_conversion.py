import unittest
from case_conversion import swap

class lab_tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(swap("absoluTE", 9), "AbsOLuTe")
    def test_2(self):
        self.assertEqual(swap("absoluTE", 4), "AbsOlutE")
    def test_3(self):
        self.assertEqual(swap("absoluTE absoluTE", 9), "AbsOLuTe AbsOLuTe")
    def test_4(self):
        self.assertEqual(swap("mine",11), "MiNE")
    def test_5(self):
        self.assertEqual(swap("Mine",11), "miNE")
    def test_6(self):
        self.assertEqual(swap("no ways", 11), "No WAYs")

if __name__ == '__main__':   
    unittest.main()