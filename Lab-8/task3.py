import string

def is_sentence_palindrome(sentence):
    # Remove punctuation and spaces, convert to lowercase
    cleaned = ''.join(
        ch.lower() for ch in sentence if ch.isalnum()
    )
    return cleaned == cleaned[::-1]
#test case-1
print(is_sentence_palindrome("A man a plan a canal Panama"))  # Expected output: True
#test case-2
print(is_sentence_palindrome("Hello World"))  # Expected output: False
