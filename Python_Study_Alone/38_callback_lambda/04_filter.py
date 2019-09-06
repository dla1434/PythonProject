
def 짝수만(number):
	return number % 2 == 0

# list 값을 설정할 때 range를 이용하면 좀 더 쉽게 초기값을 넣을 수 있다.
a = list(range(100))
print(a)

b = filter(짝수만, a)
print(b)
# filter 객체가 반환될 것이다...<filter object at 0x0000026FA61B5780>

# 방법1) filter는 for문을 돌려서 가져올 수 있다..그럼 짝수만 출력이 된다.
for i in b:
	print(i)

# 방법2) for문을 안 돌려도 list로 변환해서 출력할 수도 있다.
	# 참고 filter도 일회용 함수인 듯..위에서 실행하고 나서 또 실행하니..[] 빈 값이 출력됐다.
		# for문을 주석처리하면 제대로 출력이 된다.
print(list(b))