def func(x):
  if x==x[::-1]:
    return "palindrome"
  else:
    return "not palindrome"

a = input().lower()
print(func(a))