# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divides two numbers with proper error handling.

    Handles:
    - Non-numeric inputs (ValueError)
    - Division by zero (ZeroDivisionError)
    
    Returns:
        str: A clear message showing either the result or an error.
    """
    try:
        # Try converting inputs to floats
        num = float(numerator)
        den = float(denominator)

        try:
            # Attempt division
            result = num / den
            return f"The result of the division is {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."
