import os
def func(x):
  if not os.path.exists(x):
    return f"Path {x} does not exists"
  
  directory = os.path.dirname(x)
  filename = os.path.basename(x)

  return f"Path {x} exists. \nDirectory: {directory}\nFilename: {filename}"

x = input("Enter the path: ").strip()
print(func(x))