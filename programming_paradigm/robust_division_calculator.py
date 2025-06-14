"""
robust_division_calculator.py
A tiny module that exposes safe_divide() for fault‑tolerant division.
"""

def safe_divide(numerator, denominator):
    """
    Divide two values, returning either a result string or
    an explanatory error message.

    Parameters
    ----------
    numerator : Any  ‑‑ value representing the dividend
    denominator : Any  ‑‑ value representing the divisor

    Returns
    -------
    str  ‑‑ formatted result or error message
    """
    # 1) convert inputs to floats (catch non‑numeric)
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    # 2) perform division (catch ÷ 0)
    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    # 3) success
    return f"The result of the division is {result}"
