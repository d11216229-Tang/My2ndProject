"""
Test suite for safe_division function
"""

from safe_division import safe_division


def test_normal_division():
    """Test normal division operations"""
    assert safe_division(10, 2) == 5.0
    assert safe_division(100, 4) == 25.0
    assert safe_division(7, 2) == 3.5
    print("✓ Normal division tests passed")


def test_division_by_zero():
    """Test division by zero protection"""
    result = safe_division(10, 0)
    assert result == "Error: Division by zero is not allowed"
    result = safe_division(0, 0)
    assert result == "Error: Division by zero is not allowed"
    print("✓ Division by zero tests passed")


def test_negative_numbers():
    """Test division with negative numbers"""
    assert safe_division(-10, 2) == -5.0
    assert safe_division(10, -2) == -5.0
    assert safe_division(-10, -2) == 5.0
    print("✓ Negative number tests passed")


def test_zero_numerator():
    """Test division with zero as numerator"""
    assert safe_division(0, 5) == 0.0
    assert safe_division(0, 100) == 0.0
    print("✓ Zero numerator tests passed")


def test_float_division():
    """Test division with floating point numbers"""
    assert safe_division(7.5, 2.5) == 3.0
    assert safe_division(1.0, 2.0) == 0.5
    print("✓ Float division tests passed")


if __name__ == "__main__":
    print("Running safe_division tests...\n")
    test_normal_division()
    test_division_by_zero()
    test_negative_numbers()
    test_zero_numerator()
    test_float_division()
    print("\n✅ All tests passed!")
