
import time

print(time.time())
# 1566962040.4511142 : 이해하기 어려운 timestamp 값으로 출력된다.

# 현재 시간부터 +5(5초까지만 프로그램을 실행하는 코드
처음 = time.time()
while 처음+5 > time.time():
	pass

print("프로그램이 종료되었습니다.")