from unittest import TestCase
from src.mathlib.auxiliary import sign, mdc

class AuxiliaryTest(TestCase):
    def test_sign_negative(self):
        self.assertEqual(-1, sign(-10))
    
    def test_sign_positive(self):
        self.assertEqual(1, sign(0))
        self.assertEqual(1, sign(5))
    
    def test_positive_mdc(self):
        self.assertEqual(3, mdc(9, 3))
        self.assertEqual(1, mdc(21, 2))
    
    def test_negative_mdc(self):
        self.assertEqual(2, mdc(10, -2))
        self.assertEqual(5, mdc(-25, 5))
    
    def test_null_mdc(self):
        self.assertEqual(100, mdc(100, 0))
        self.assertEqual(20, mdc(0, 20))
