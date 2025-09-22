def reverse_string():
    user_input = input("Enter a string to reverse: ")
    reversed_str = user_input[::-1]
    print("Reversed string:", reversed_str)

if __name__ == "__main__":
    reverse_string()