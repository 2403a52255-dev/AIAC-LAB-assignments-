import unittest
from task1 import is_valid_email

class TestIsValidEmail(unittest.TestCase):
    def test_valid_email(self):
        self.assertTrue(is_valid_email("test@example.com"))
        self.assertTrue(is_valid_email("user.name@domain.co"))
        self.assertTrue(is_valid_email("user_name123@sub.domain.org"))

    def test_invalid_email_no_at(self):
        self.assertFalse(is_valid_email("testexample.com"))
        self.assertFalse(is_valid_email("user.name.domain.com"))

    def test_invalid_email_no_domain(self):
        self.assertFalse(is_valid_email("test@"))
        self.assertFalse(is_valid_email("user@.com"))

    def test_invalid_email_special_chars(self):
        self.assertFalse(is_valid_email("user!@domain.com"))
        self.assertFalse(is_valid_email("user#name@domain.com"))

    def test_invalid_email_multiple_at(self):
        self.assertFalse(is_valid_email("user@@domain.com"))

    def test_invalid_email_empty_string(self):
        self.assertFalse(is_valid_email(""))

if __name__ == "__main__":
    unittest.main()