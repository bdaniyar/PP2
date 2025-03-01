
def func(x):
  try:
    with open(x, 'r') as file:
      return sum(1 for line in file)
  
  except:
    return f"File {x} not found"
  


x = input("Enter the filename: ").strip()
print("Number of lines: ", func(x))