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

    def test_fraction_add(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 3)
        res = f1 + f2
        self.assertEqual(1, res.sign())
        self.assertEqual(7, res.numerator())
        self.assertEqual(6, res.denominator())
    
    def test_fraction_sub(self):
        f1 = Fraction(1, 4)
        f2 = Fraction(1, 3)
        res = f1 - f2
        self.assertEqual(-1, res.sign())
        self.assertEqual(1, res.numerator())
        self.assertEqual(12, res.denominator())
    
    def test_fraction_mul(self):
        f1 = Fraction(-2, 5)
        f2 = Fraction(-5, 3)
        res = f1 * f2
        self.assertEqual(1, res.sign())
        self.assertEqual(2, res.numerator())
        self.assertEqual(3, res.denominator())
    
    def test_fraction_div(self):
        f1 = Fraction(1, 4)
        f2 = Fraction(-3, 2)
        res = f1 / f2
        self.assertEqual(-1, res.sign())
        self.assertEqual(1, res.numerator())
        self.assertEqual(6, res.denominator())
    
    def test_fraction_equals(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        self.assertTrue(f1 == f1)
        self.assertFalse(f1 == f2)
    
    def test_fraction_not_equals(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        self.assertTrue(f1 != f2)
        self.assertFalse(f1 != f1)
    
    def test_fraction_greater(self):
        f1 = Fraction(1, 3)
        f2 = Fraction(1, 4)
        self.assertTrue(f1 > f2)
        self.assertFalse(f2 > f1)
    
    def test_fraction_less(self):
        f1 = Fraction(1, 4)
        f2 = Fraction(2, 3)
        self.assertTrue(f1 < f2)
        self.assertFalse(f2 < f1)
    
    def test_fraction_greater_equal(self):
        f1 = Fraction(10, 3)
        f2 = Fraction(5, 4)
        self.assertTrue(f1 >= f2)
        self.assertTrue(f1 >= f1)
        self.assertFalse(f2 >= f1)
    
    def test_fraction_less_equal(self):
        f1 = Fraction(4, 3)
        f2 = Fraction(5, 2)
        self.assertTrue(f1 < f2)
        self.assertTrue(f1 <= f1)
        self.assertFalse(f2 < f1)

    def test_fraction_parse(self):
        f1 = Fraction.from_string("1/2")
        f2 = Fraction.from_string("-10/3")
        self.assertEqual(1, f1.sign())
        self.assertEqual(1, f1.numerator())
        self.assertEqual(2, f1.denominator())
        self.assertEqual(-1, f2.sign())
        self.assertEqual(10, f2.numerator())
        self.assertEqual(3, f2.denominator())
    
    def test_integer_parse(self):
        f1 = Fraction.from_string("20")
        f2 = Fraction.from_string("-10")
        self.assertEqual(1, f1.sign())
        self.assertEqual(20, f1.numerator())
        self.assertEqual(1, f1.denominator())
        self.assertEqual(-1, f2.sign())
        self.assertEqual(10, f2.numerator())
        self.assertEqual(1, f2.denominator())
