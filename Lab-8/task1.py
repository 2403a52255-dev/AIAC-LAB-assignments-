import re

def is_valid_email(email):
    """
    Verifies if the given email address is valid.
    Returns True if valid, False otherwise.
    """
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None
#test case-1
print(is_valid_email("namitha@gmail.com"))  # Expected output: True
#test case-2
print(is_valid_email("namitha@gmailcom"))  # Expected output: False
#test case-3
print(is_valid_email("namitha@.com"))  # Expected output: False