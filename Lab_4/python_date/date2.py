import datetime
from datetime import timedelta , datetime
x = datetime.now()
y = datetime.now() - timedelta(days=1)
z = datetime.now() + timedelta(days=1)
print("yesterday:", y)
print("today:", x)
print("tomorrow:", z)
