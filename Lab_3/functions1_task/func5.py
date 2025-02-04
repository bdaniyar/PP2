import itertools

def string_permutations():
    s = input("Enter a string: ")
    permutations = itertools.permutations(s)
    for perm in permutations:
        print("".join(perm))

# Example Usage
string_permutations()
