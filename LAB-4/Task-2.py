def factorial(n):
    if n <= 0:
        return "Invalid input"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

try:
    num = int(input("Enter a positive integer: "))
    print(factorial(num))
except ValueError:
    print("Invalid input")