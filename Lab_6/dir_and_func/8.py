import os

def func(x):
  if not os.path.exists(x):
    print(f"{x} does not exists")
  elif os.path.exists(x):
    os.remove(x)
  

x = input("enter path:" )
func(x)

