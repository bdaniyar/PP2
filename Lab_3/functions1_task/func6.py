def reverse_sentence():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    reversed_sentence = " ".join(reversed(words))
    print("Reversed sentence:", reversed_sentence)

# Example Usage
reverse_sentence()
