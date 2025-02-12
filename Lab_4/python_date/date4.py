import datetime
from datetime import datetime, timedelta

x = datetime.now()
y = x - timedelta(seconds=30)
print("Current date: ", x)
print("With difference a 30 second", y)