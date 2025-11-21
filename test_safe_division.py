"""
Unit tests for the safe_division module.

This module contains comprehensive tests for the safe_division function,
covering various test cases including normal division, division by zero,
and edge cases.
"""

import unittest
from safe_division import safe_division


class TestSafeDivision(unittest.TestCase):
    """Test cases for the safe_division function."""
    
    def test_normal_division(self):
        """Test normal division operations."""
        self.assertEqual(safe_division(10, 2), 5.0)
        self.assertEqual(safe_division(9, 3), 3.0)
        self.assertEqual(safe_division(15, 5), 3.0)
    
    def test_division_with_float_result(self):
        """Test division that results in float values."""
        self.assertAlmostEqual(safe_division(7, 3), 2.3333333333333335)
        self.assertAlmostEqual(safe_division(10, 3), 3.3333333333333335)
        self.assertAlmostEqual(safe_division(1, 3), 0.3333333333333333)
    
    def test_division_by_zero(self):
        """Test division by zero returns error message."""
        self.assertEqual(safe_division(10, 0), "Error: Division by zero is not allowed")
        self.assertEqual(safe_division(0, 0), "Error: Division by zero is not allowed")
        self.assertEqual(safe_division(-5, 0), "Error: Division by zero is not allowed")
    
    def test_negative_numbers(self):
        """Test division with negative numbers."""
        self.assertEqual(safe_division(-10, 2), -5.0)
        self.assertEqual(safe_division(10, -2), -5.0)
        self.assertEqual(safe_division(-10, -2), 5.0)
    
    def test_division_with_zero_numerator(self):
        """Test division when numerator is zero."""
        self.assertEqual(safe_division(0, 5), 0.0)
        self.assertEqual(safe_division(0, 10), 0.0)
        self.assertEqual(safe_division(0, -3), 0.0)
    
    def test_division_by_one(self):
        """Test division by one returns the same number."""
        self.assertEqual(safe_division(10, 1), 10.0)
        self.assertEqual(safe_division(5, 1), 5.0)
        self.assertEqual(safe_division(-7, 1), -7.0)
    
    def test_division_of_same_numbers(self):
        """Test division of same numbers returns 1.0."""
        self.assertEqual(safe_division(10, 10), 1.0)
        self.assertEqual(safe_division(5, 5), 1.0)
        self.assertEqual(safe_division(-3, -3), 1.0)
    
    def test_float_arguments(self):
        """Test division with float arguments."""
        self.assertEqual(safe_division(10.5, 2.5), 4.2)
        self.assertAlmostEqual(safe_division(7.7, 2.2), 3.5)
        self.assertEqual(safe_division(3.0, 1.5), 2.0)
    
    def test_large_numbers(self):
        """Test division with large numbers."""
        self.assertEqual(safe_division(1000000, 1000), 1000.0)
        self.assertEqual(safe_division(999999, 3), 333333.0)
    
    def test_small_numbers(self):
        """Test division with very small numbers."""
        self.assertAlmostEqual(safe_division(0.001, 0.1), 0.01)
        self.assertAlmostEqual(safe_division(0.1, 0.01), 10.0)


if __name__ == '__main__':
    unittest.main()
