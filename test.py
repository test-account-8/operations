def divide_numbers(num1, num2):
    """
    This function divides two numbers and returns the result.
    If the second number is zero, it raises a ValueError.
    """
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / num2