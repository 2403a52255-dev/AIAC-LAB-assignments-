import string
from collections import Counter

def most_frequent_word(paragraph):
    # Convert to lowercase
    text = paragraph.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Split into words
    words = text.split()
    # Count word frequencies
    freq = Counter(words)
    # Find the most common word
    most_common = freq.most_common(1)
    return most_common[0][0] if most_common else None

# Example usage:
print(most_frequent_word("i love python . python is easy language to learn. python is better than other languages."))