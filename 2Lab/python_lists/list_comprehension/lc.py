#Example 1
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#Example 2
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#Example 3
newlist = [x for x in fruits if x != "apple"]

#Example 4
newlist = [x for x in fruits]

#Example 5
newlist = [x for x in range(10)]

#Example 6
newlist = [x for x in range(10) if x < 5]