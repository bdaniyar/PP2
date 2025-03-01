import time
import math

def func(x,y):
  time.sleep(y/1000)
  return math.sqrt(x)

number = int(input())
ms = int(input())

result = func(number,ms)

print(f"Square root of {number} after {ms} milisecond is {result}")


"""
time.sleep can stop time in terminal for a x second

"""