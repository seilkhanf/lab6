from datetime import datetime, timedelta

today = datetime.now()
five_days_ago = datetime(today.year, today.month, today.day) - timedelta(days=5)

print(" NOW", today.strftime("%Y-%m-%d"))
print("5DAYS AGO", five_days_ago.strftime("%Y-%m-%d"))