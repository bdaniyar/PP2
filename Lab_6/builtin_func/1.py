import math

def func(x):
  return math.prod(x)

a = [1,2,33,4,4,4]
print(func(a))


"""
pyhton built 
math.prod() is function to multiplie numbers in a list

"""

"ALternative"

def func2(y):
  a = 1
  for i in y:
    a*=i
  return a

list1 = [1,2,3,4,5]
print(func2(list1))
