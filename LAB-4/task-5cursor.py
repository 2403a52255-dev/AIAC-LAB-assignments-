import string

def most_frequent_word(paragraph):
    # Convert to lowercase
    paragraph = paragraph.lower()
    # Remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    paragraph = paragraph.translate(translator)
    # Split into words
    words = paragraph.split()
    # Count frequency
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    # Find the most frequent word
    max_count = 0
    most_freq = None
    for word, count in freq.items():
        if count > max_count:
            max_count = count
            most_freq = word
    return most_freq

# Example usage:
if __name__ == "__main__":
    text1 = "her name is dora . dora is a good girl . dora always explores the world . dora cant see properly."
    print(most_frequent_word(text1))  # Output: dora

    text2 = "betty bought some better butter but it was bitter butter so betty add some more better butter and made it bitter butter better."
    print(most_frequent_word(text2))  # Output: butter

    text3 = "my name is nammu. my course in btech is cse . is this better?"
    print(most_frequent_word(text3))  # Output: is

    text4 = "i love python . python is easy language to learn. python is better than other languages. now what is the output?"
    print(most_frequent_word(text4))  # Output: python
