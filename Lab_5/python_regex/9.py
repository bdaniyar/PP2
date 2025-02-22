import re

def insert_spaces(text):
    pattern = r'(?<!^)([A-Z])' 
    return re.sub(pattern, r' \1', text)

user_input = input("Enter a string: ")
result = insert_spaces(user_input)
print("Formatted string:", result)
