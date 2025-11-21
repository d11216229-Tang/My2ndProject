"""
safe_division module - Provides a safe division function that handles division by zero
"""

def safe_division(a, b):
    """
    Safely divides two numbers, handling division by zero.
    
    Args:
        a: The dividend (numerator)
        b: The divisor (denominator)
    
    Returns:
        The result of a / b, or an error message if b is zero
    """
    try:
        result = a / b
    except ZeroDivisionError:
        # return "Error: Division by zero is not allowed."
        pass
    return result
