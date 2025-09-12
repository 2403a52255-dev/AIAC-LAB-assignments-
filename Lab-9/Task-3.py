import numpy as np

# Calculator functions using NumPy
def add(a, b):
    return np.add(a, b)

def subtract(a, b):
    return np.subtract(a, b)

def multiply(a, b):
    return np.multiply(a, b)

def divide(a, b):
    try:
        return np.divide(a, b)
    except ZeroDivisionError:
        return "Error: Division by zero not allowed"


# Example usage
if __name__ == "__main__":
    x, y = 15, 3

    print("Numbers:", x, "and", y)
    print("Addition:", add(x, y))
    print("Subtraction:", subtract(x, y))
    print("Multiplication:", multiply(x, y))
    print("Division:", divide(x, y))
