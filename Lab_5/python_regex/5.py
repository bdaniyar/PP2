import re

def find_matching_strings(text):
    pattern = r'^a.*b$'  
    matches = re.findall(pattern, text)
    return bool(matches)  

user_input = input("Enter a string: ")

if find_matching_strings(user_input):
    print("The string matches the pattern!")
else:
    print("The string does NOT match the pattern.")