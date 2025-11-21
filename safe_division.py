"""
Safe Division Module

This module provides a safe division function that prevents division by zero errors.
"""


def safe_division(a, b):
    """
    Safely divide two numbers, preventing division by zero.
    
    Args:
        a (int or float): The numerator (dividend)
        b (int or float): The denominator (divisor)
    
    Returns:
        float or str: The result of a/b if b is not zero, 
                      otherwise returns an error message
    
    Examples:
        >>> safe_division(10, 2)
        5.0
        >>> safe_division(10, 0)
        'Error: Division by zero is not allowed'
        >>> safe_division(7, 3)
        2.3333333333333335
    """
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b
