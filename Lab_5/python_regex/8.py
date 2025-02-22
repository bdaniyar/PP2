import re

def split_at_uppercase(text):
    pattern = r'(?=[A-Z])'  
    return re.split(pattern, text)

user_input = input("Enter a string: ")
result = split_at_uppercase(user_input)
print("Split string:", result)
