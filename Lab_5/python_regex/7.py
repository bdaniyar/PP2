import re

def snake_to_camel(snake_str):
    components = snake_str.split('_')  
    camel_case_str = components[0] + ''.join(word.capitalize() for word in components[1:])  
    return camel_case_str

user_input = input("Enter a snake_case string: ")
result = snake_to_camel(user_input)
print("CamelCase string:", result)
