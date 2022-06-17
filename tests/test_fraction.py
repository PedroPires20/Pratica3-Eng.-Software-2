from unittest import TestCase
from src.mathlib.fraction import Fraction

class FractionTest(TestCase):
    def test_create_null_fraction(self):
        fraction = Fraction()
        self.assertEqual(1, fraction.sign())
        self.assertEqual(0, fraction.numerator())
        self.assertEqual(1, fraction.denominator())
    
    def test_create_integer_fraction(self):
        f1 = Fraction(20)
        f2 = Fraction(10, 1)
        self.assertEqual(1, f1.sign())
        self.assertEqual(20, f1.numerator())
        self.assertEqual(1, f1.denominator())
        self.assertEqual(1, f2.sign())
        self.assertEqual(10, f2.numerator())
        self.assertEqual(1, f2.denominator())
    
    def test_create_simple_fraction(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 4)
        self.assertEqual(1, f1.sign())
        self.assertEqual(1, f1.numerator())
        self.assertEqual(2, f1.denominator())
        self.assertEqual(1, f2.sign())
        self.assertEqual(3, f2.numerator())
        self.assertEqual(4, f2.denominator())

    def test_create_negative_fractions(self):
        f1 = Fraction(-1, 2)
        f2 = Fraction(-4)
        f3 = Fraction(12, -5)
        self.assertEqual(-1, f1.sign())
        self.assertEqual(1, f1.numerator())
        self.assertEqual(2, f1.denominator())
        self.assertEqual(-1, f2.sign())
        self.assertEqual(4, f2.numerator())
        self.assertEqual(1, f2.denominator())
        self.assertEqual(-1, f3.sign())
        self.assertEqual(12, f3.numerator())
        self.assertEqual(5, f3.denominator())

    def test_created_fractions_are_always_simplified(self):
        f1 = Fraction(10, 20)
        f2 = Fraction(50, 2)
        self.assertEqual(1, f1.sign())
        self.assertEqual(1, f1.numerator())
        self.assertEqual(2, f1.denominator())
        self.assertEqual(1, f2.sign())
        self.assertEqual(25, f2.numerator())
        self.assertEqual(1, f2.denominator())
    
    def test_create_fractions_with_two_negative_integers(self):
        f1 = Fraction(-10, -20)
        f2 = Fraction(-50, -4)
        self.assertEqual(1, f1.sign())
        self.assertEqual(1, f1.numerator())
        self.assertEqual(2, f1.denominator())
        self.assertEqual(1, f2.sign())
        self.assertEqual(25, f2.numerator())
        self.assertEqual(2, f2.denominator())
