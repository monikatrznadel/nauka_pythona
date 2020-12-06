import unittest

from str_calculator import str_calculator

class TestStringCalculator(unittest.TestCase):
    def test_lacz(self):
        r=str_calculator('a', 'b', 'lacz')
        self.assertEqual(r, 'ab')

    def test_awb(self):
        r=str_calculator('a', 'b', 'awb')
        self.assertEqual(r, False)
