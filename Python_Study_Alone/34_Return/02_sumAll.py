
# start~end까지 모든 정수를 더하는 함수
def sum_all(start, end):
	변수 = 0
	for i in range(start, end+1):
		변수 += i
	return 변수

returnA = sum_all(1, 100)
print(returnA)
returnB = sum_all(50, 100)
print(returnB)