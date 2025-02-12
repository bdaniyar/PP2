import math

def func(x):
    for i in range(0,x):
        if(i % 3 == 0 and i % 4==0):
            print(i)

x = int(input())
func(x)
