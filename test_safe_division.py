"""
Unit tests for safe_division function
"""

import unittest
from safe_division import safe_division


class TestSafeDivision(unittest.TestCase):
    """Test cases for the safe_division function"""
    
    def test_normal_division(self):
        """Test normal division with positive numbers"""
        self.assertEqual(safe_division(10, 2), 5.0)
    
    def test_division_with_result_fraction(self):
        """Test division that results in a fraction"""
        self.assertAlmostEqual(safe_division(10, 3), 3.3333333333333335)
    
    def test_division_by_same_number(self):
        """Test division of a number by itself"""
        self.assertEqual(safe_division(10, 10), 1.0)
    
    def test_division_by_one(self):
        """Test division by 1"""
        self.assertEqual(safe_division(10, 1), 10.0)
    
    def test_negative_division(self):
        """Test division with negative numbers"""
        self.assertEqual(safe_division(-10, 2), -5.0)
        self.assertEqual(safe_division(10, -2), -5.0)
        self.assertEqual(safe_division(-10, -2), 5.0)
    
    def test_division_by_zero(self):
        """Test division by zero - should return error message"""
        result = safe_division(10, 0)
        self.assertEqual(result, "Error: Division by zero is not allowed.")
    
    def test_zero_divided_by_number(self):
        """Test zero divided by a number"""
        self.assertEqual(safe_division(0, 5), 0.0)
    
    def test_boundary_values(self):
        """Test with very small and large numbers"""
        self.assertAlmostEqual(safe_division(1, 1000000), 0.000001)
        self.assertEqual(safe_division(1000000, 1), 1000000.0)


if __name__ == '__main__':
    unittest.main()
