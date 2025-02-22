import re

def replace_chars(text):
    pattern = r'[ ,.]' 
    replaced_text = re.sub(pattern, ":", text)
    return replaced_text


user_input = input("Enter a string: ")
result = replace_chars(user_input)
print("Modified string:", result)
