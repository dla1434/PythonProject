# 날짜/시간과 관련된 기능을 가져옵니다.
import datetime

# 현재 날짜/시간을 구하고 쉽게 사용할 수 있게 월을 변수에 저장합니다.
now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second

print(year)
print(month)
print(day)
print(hour)
print(minute)
print(second)

if now.hour < 12:
    print("현재 시간은 {}시 {}분으로 오전입니다.".format(now.hour, now.minute))
if now.hour >= 12:
    print("현재 시간은 {}시 {}분으로 오후입니다.".format(now.hour, now.minute))
