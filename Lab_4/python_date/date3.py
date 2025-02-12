from datetime import datetime

date = datetime.now()

microseconds = date.replace(microsecond=0)

print(date)
print(microseconds)

"""
To remove microseconds from the output 
we just need to replace them with 0
so 0 wont be visible in output

"""