import datetime

a = datetime.datetime(year=2014, month=5, day=8, hour=14, minute=22)
b = datetime.datetime(year=2014, month=3, day=14, hour=12, minute=9)

print(a - b)

d = a - b
print(d)
print(d.total_seconds())

print(datetime.date.today() + datetime.timedelta(weeks=1) * 3)
