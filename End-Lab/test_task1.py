
import unittest
from Task1 import clean_email_data 
class TestCleanEmailData(unittest.TestCase):

    def test_normal_input(self):
        emails = [" Alice@example.com ", "BOB@EXAMPLE.COM", "alice@example.com"]
        result = clean_email_data(emails)
        print("\nTest 1 Output:", result)
        expected = ['alice@example.com', 'bob@example.com']
        self.assertEqual(result, expected)

    def test_already_clean_emails(self):
        emails = ["user1@gmail.com", "user2@gmail.com"]
        result = clean_email_data(emails)
        print("\nTest 2 Output:", result)
        expected = ['user1@gmail.com', 'user2@gmail.com']
        self.assertEqual(result, expected)

    def test_extra_spaces_and_duplicates(self):
        emails = ["  TEST@MAIL.com", "test@mail.com  ", "Test@Mail.Com"]
        result = clean_email_data(emails)
        print("\nTest 3 Output:", result)
        expected = ['test@mail.com']
        self.assertEqual(result, expected)

    def test_empty_list(self):
        emails = []
        result = clean_email_data(emails)
        print("\nTest 4 Output:", result)
        expected = []
        self.assertEqual(result, expected)

    def test_mixed_case_uncommon_domains(self):
        emails = ["USER@YAHOO.CO.IN", "user@yahoo.co.in", "User@Gmail.Com"]
        result = clean_email_data(emails)
        print("\nTest 5 Output:", result)
        expected = ['user@yahoo.co.in', 'user@gmail.com']
        self.assertEqual(result, expected)


# Run tests and print outputs
if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestCleanEmailData)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
