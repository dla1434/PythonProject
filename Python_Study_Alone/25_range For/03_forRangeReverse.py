
for i in range(9, -1, -1):
	print(i)

print()

# 두번째 인자에 -1이 어석해서 0을 쓰는 사람도 있데..
for i in range(9, 0 -1, -1):
	print(i)

print()

# 위에 두 가지보다 더 추천하는 방법은 reverse 함수 사용법이 있다.
for i in reversed(range(0, 10)):
	print(i)

print()

# reversed을 사용하면 리스트 출력 순서도 반대로 할 수 있다.
array = [273, 52, 103, 32, 57]
for i in reversed(array):
	print(i)