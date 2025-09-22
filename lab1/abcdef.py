def is_armstrong(number):
    """
    Check if a number is an Armstrong number.
    An Armstrong number is a number that is equal to the sum of its own digits raised to the power of the number of digits.
    """
    # Convert number to string to count digits
    num_str = str(number)
    num_digits = len(num_str)
    
    # Calculate sum of digits raised to power of number of digits
    sum_of_powers = 0
    for digit in num_str:
        sum_of_powers += int(digit) ** num_digits
    
    # Check if the sum equals the original number
    return sum_of_powers == number

def main():
    print("Armstrong Number Checker")
    print("=" * 25)
    
    while True:
        try:
            # Get input from user
            user_input = input("\nEnter a number to check (or 'quit' to exit): ")
            
            # Check if user wants to quit
            if user_input.lower() in ['quit', 'q', 'exit']:
                print("Goodbye!")
                break
            
            # Convert input to integer
            number = int(user_input)
            
            # Check if it's an Armstrong number
            if is_armstrong(number):
                print(f"{number} is an Armstrong number!")
            else:
                print(f"{number} is NOT an Armstrong number.")
                
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break

if __name__ == "__main__":
    main()
