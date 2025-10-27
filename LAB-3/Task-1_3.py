def factorial(n):
    """Return the factorial of a given non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example usage:
number = int(input("Enter a non-negative integer: "))
try:
    print(f"Factorial of {number} is {factorial(number)}")
except ValueError as e:
    print(e)
