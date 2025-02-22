import re

def mt(x):
    pat = r'a*b{2,3}$'
    if re.search(pat,x):
        return "found"
    else:
        return "no match"

print(mt("aabb"))
print(mt("ab"))
print(mt("abb"))