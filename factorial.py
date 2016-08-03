def factorial(number):
    """Calculate factorial value for input number."""
    result = 1
    multiply_by = list(range(1, number+1))
    for i in multiply_by:
        result *= i
    return result
