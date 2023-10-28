from datetime import datetime, timedelta

today = datetime.now().date()
five_days_ago = datetime(today.year, today.month, today.day)
five_days_ago -= timedelta(days=5)

print("5DAYSAGO:", five_days_ago)
print("TODAY:", today)