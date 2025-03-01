def func(x):
  upp = sum(1 for i in x if i.isupper())
  low = sum(1 for j in x if j.islower())

  return upp,low


a = input()
upper,lower = func(a)
print(f"uppercase letters: {upper}")
print(f"lowercase letters: {lower}")
