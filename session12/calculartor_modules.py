# calculator.py

def add(a, b):
    """Adds two numbers."""
    return a + b

def subtract(a, b):
    """Subtracts b from a."""
    return a - b

def multiply(a, b):
    """Multiplies two numbers."""
    return a * b

def divide(a, b):
    """Divides a by b (non-zero denominator)."""
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero!"
