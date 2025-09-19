import unittest
from task3 import is_sentence_palindrome

class TestIsSentencePalindrome(unittest.TestCase):
    def test_simple_palindrome(self):
        self.assertTrue(is_sentence_palindrome("A man a plan a canal Panama"))

    def test_with_punctuation(self):
        self.assertTrue(is_sentence_palindrome("Madam, in Eden, I'm Adam."))

    def test_not_palindrome(self):
        self.assertFalse(is_sentence_palindrome("Hello world"))

    def test_empty_string(self):
        self.assertTrue(is_sentence_palindrome(""))

    def test_single_character(self):
        self.assertTrue(is_sentence_palindrome("a"))

    def test_mixed_case(self):
        self.assertTrue(is_sentence_palindrome("No lemon, no melon"))

    def test_numbers_and_letters(self):
        self.assertTrue(is_sentence_palindrome("12321"))

    def test_spaces_only(self):
        self.assertTrue(is_sentence_palindrome("     "))

    def test_non_palindrome_with_punctuation(self):
        self.assertFalse(is_sentence_palindrome("This is not a palindrome!"))

if __name__ == "__main__":
    unittest.main()