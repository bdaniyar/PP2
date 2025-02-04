def is_palindrome(word):
    cleaned_word = ''.join(e for e in word if e.isalnum()).lower()
    return cleaned_word == cleaned_word[::-1]

# Example Usage
word = "madam"
print(f"Is '{word}' a palindrome? {is_palindrome(word)}")
