
"""
# 일회용 함수 : 제너레이터
	- 리스트 뒤집기 : reversed
	- 현재 인덱스가 몇 번째인지 확인하기 : enumerate()
	- 딕셔너리로 쉽게 반복문 작성하기 : items()
"""

a = [0,1,2,3,4,5]
reversed_a = reversed(a)
print(reversed_a) 		# <list_reverseiterator object at 0x000000000DA9A630>

# 리스트 출력하기
print(list(reversed_a))
# 한번 출력 후 다시 출력해보면 []로 빈 리스트값이 출력된다..이래서 일회용 함수이다.
print(list(reversed_a))

for i in reversed_a:
	print(i, end = " ")
print()
# reversed_a가 위에서 한번 돌았기 때문에..여기는 빈 리스트값이라 출력이 안 될 것이다.
for i in reversed_a:
	print(i, end = " ")
