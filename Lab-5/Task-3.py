def fibonacci(n):
    """Calculate the nth Fibonacci number using recursion.

    Args:
        n (int): The position in the Fibonacci sequence (0-indexed).

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is negative.
    """
    # The Fibonacci sequence is defined as:
    # F(0) = 0, F(1) = 1
    # F(n) = F(n-1) + F(n-2) for n > 1

    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0  # Base case: F(0) = 0
    elif n == 1:
        return 1  # Base case: F(1) = 1
    else:
        # Recursive case: sum of previous two Fibonacci numbers
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage:
print(fibonacci(6))  # Output: 8

"""
Explanation:
-------------
This function calculates the nth Fibonacci number using recursion.
It checks for base cases (n == 0 or n == 1) and returns the corresponding value.
For n > 1, it recursively calls itself to compute the sum of the previous two Fibonacci numbers.
A ValueError is raised if the input is negative.
"""