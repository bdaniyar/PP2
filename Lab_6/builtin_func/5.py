"""
The all() function returns True if all items in an iterable are true, otherwise it returns False.

If the iterable object is empty, the all() function also returns True.


"""
def func(x):
  return all(x)

a = (True,1,"he", 5)
b = (True,0,"ds")

print(func(a)) #True
print(func(b)) #False