# My2ndProject

## Safe Division Calculator (防呆計算機)

This repository contains a Python implementation of a safe division function that prevents division by zero errors.

### Features

- **safe_division(a, b)**: A function that safely divides two numbers
  - Prevents division by zero errors
  - Returns error message when attempting to divide by zero
  - Supports both integers and floating-point numbers
  - Handles negative numbers correctly

### Usage

```python
from safe_division import safe_division

# Normal division
result = safe_division(10, 2)  # Returns 5.0

# Division by zero (protected)
result = safe_division(10, 0)  # Returns "Error: Division by zero is not allowed"

# Float division
result = safe_division(7.5, 2.5)  # Returns 3.0
```

### Running Tests

To run the test suite:

```bash
python3 test_safe_division.py
```

### Files

- `safe_division.py` - Main module containing the safe_division function
- `test_safe_division.py` - Test suite for the safe_division function