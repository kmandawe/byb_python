import datetime

cet = datetime.timezone(datetime.timedelta(hours=1), "CET")
print(cet)

departure = datetime.datetime(year=2014, month=1, day=7, hour=11, minute=30, tzinfo=cet)

arrival = datetime.datetime(year=2014, month=1, day=7, hour=13, minute=5, tzinfo=datetime.timezone.utc)

print(arrival - departure)
