def factorial(n):
    if n <= 0:
        return "invalid input"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

try:
    num = int(input("Enter a number: "))
    print(factorial(num))
except ValueError:
    print("invalid input")
