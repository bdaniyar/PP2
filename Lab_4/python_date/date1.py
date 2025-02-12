import datetime
from datetime import timedelta, datetime

date  = datetime.now()

new_date = date - timedelta(days=5)

print("Current date: ", date)
print("Date after substracting 5 days: ", new_date)


"""
timedelta(minutes=)
timedelta(hours=)
timedelta(days=)

"""