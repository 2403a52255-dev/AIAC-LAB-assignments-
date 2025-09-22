def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
def main():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Enter choice (1/2/3/4): ")
    if choice not in ('1', '2', '3', '4'):
        print("Invalid input")
        return
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number input")
        return
    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", sub(num1, num2))
    elif choice == '3':
        print("Result:", mul(num1, num2))
    elif choice == '4':
        print("Result:", div(num1, num2))
if __name__ == "__main__":
    main()