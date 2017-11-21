from datetime import datetime

now = datetime.now()
print(now)

str_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(str_now)