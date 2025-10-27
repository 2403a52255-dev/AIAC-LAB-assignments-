def factorial_from_input():
    try:
        n = int(input("Enter a non-negative integer: "))
        if n < 0:
            print("Factorial is not defined for negative numbers.")
            return
        result = 1
        for i in range(2, n + 1):
            result *= i
        print(f"Factorial of {n} is {result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

factorial_from_input()
