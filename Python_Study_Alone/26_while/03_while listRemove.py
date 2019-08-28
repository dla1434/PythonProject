
# 다음과 같이 리스트에서 remove로 특정값을 모두 지울때 while을 활용할 수 있다.

# 하나만 리스트 지울 경우
numbers = [1,2,1,2,1,2,2,1,2]
numbers.remove(1)

# 모두 지울 경우
while 1 in numbers:
	numbers.remove(1)
	print(numbers)
