# src/utils/helpers.py

def safe_divide(a, b):
    """
    Divide a by b safely.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return 0
