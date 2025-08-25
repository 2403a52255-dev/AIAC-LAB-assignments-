import re

def is_indian_mobile_number(number):
    """
    Checks if the given number is a valid Indian mobile number.
    Indian mobile numbers:
      - 10 digits
      - Start with 6, 7, 8, or 9
    """
    pattern = r'^[6-9]\d{9}$'
    return bool(re.match(pattern, str(number)))

# Example usage:
print(is_indian_mobile_number('9876543210'))  # True
print(is_indian_mobile_number('1234567890'))  # False
