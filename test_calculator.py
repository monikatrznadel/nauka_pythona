import unittest

from calculator import calculate

class TestCalculator(unittest.TestCase):
    def test_dodawania(self):
        r=calculate(1, 2, '+')
        self.assertEqual(r, 3)

    def test_odejmowania(self):
        r=calculate(10, 120, '-')
        self.assertEqual(r, -110)

    def test_mnozenia(self):
        r=calculate(10, 7, '*')
        self.assertEqual(r, 70)

    def test_dzielenia(self):
        r=calculate(30, 5, '/')
        self.assertEqual(r, 6)

    def test_modulo(self):
        r=calculate(8, 2, '%')
        self.assertEqual(r, 0)
