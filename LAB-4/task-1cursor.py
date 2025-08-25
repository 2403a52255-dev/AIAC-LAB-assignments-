def is_indian_mobile_number(number):
    """
    Checks if the given number is a valid Indian mobile number.
    Indian mobile numbers are 10 digits and start with 9, 8, 7, or 6.
    """
    num_str = str(number)
    return len(num_str) == 10 and num_str[0] in '9876' and num_str.isdigit()

# Example usage:
number = 9550378211
print(is_indian_mobile_number(number))  # Output: True

