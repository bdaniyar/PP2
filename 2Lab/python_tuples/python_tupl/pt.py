#Example 1
mytuple = ("apple", "banana", "cherry")

thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Example 2
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#Example 3
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#Example 4
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#Example 5
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#Example 6
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)