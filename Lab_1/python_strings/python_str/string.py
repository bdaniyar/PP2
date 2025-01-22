#Example 1
print("Hello")
print('Hello')

#Example 2
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#Example 3
a = "Hello"
print(a)

#Example 4
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Example 5
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Example 6
a = "Hello, World!"
print(a[1])

#Example 7
for x in 'bananna':
  print(x)

#Example 8
a = "Hello, World!"
print(len(a))

#Example 9
#To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("free" in txt)

#Example 10
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#Example 11
#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
txt = "The best things in life are free!"
print("expensive" not in txt)

#Example 12
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")