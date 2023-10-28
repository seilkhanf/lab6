from datetime import datetime, timedelta

date1 = datetime(2023, 10, 26, 15, 30, 0)
date2 = datetime(2023, 10, 26, 16, 0, 0)
diff = date2 - date1 - timedelta(days=5)
diffsec = diff.total_seconds()

print("1timeis:", date1)
print("2timeis:", date2)
print("ditime:", diffsec)