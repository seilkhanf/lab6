from datetime import datetime, timedelta

now = datetime(2023, 10, 26, 15, 30, 45, 123456)
five_days_ago = now - timedelta(days=5)

print("timeis:", now)
print("timeis five days ago:", five_days_ago)