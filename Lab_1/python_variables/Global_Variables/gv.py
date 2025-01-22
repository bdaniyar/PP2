#Example 1
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

print("\n")
#Example 2
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

print("\n")
#Example 3
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
print("\n")
#Example 3
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)