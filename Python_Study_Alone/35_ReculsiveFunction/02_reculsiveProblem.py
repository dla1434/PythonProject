'''
f(1) = 1
f(2) = 1
f(n) = f(n-1) + f(n-2)

f(3) = f(2) + f(1) = 2
f(4) = f(4) + f(2) = 3
5
8
13
''' 

def f(n):
	if n == 1 or n == 2:
		return 1
	else:
		return f(n-1) + f(n-2)

print(f(1))
print(f(2))
print(f(3))
print(f(4))
# 여기서부터는 느려진다..
# print(f(40))

# print(f(40)) 부터 느려지는 원인을 구하기 위해서 counter를 해보자
# global : 함수 내부에서 외부의 변수를 접근하기 위해서는 global keyword을 붙여줘야 접근이 가능하다.
	# global counter += 1처럼 작성하면 에러가 발생되니 주의하자
counter = 0
def f_counter(n):
	global counter
	counter += 1
	if n == 1 or n == 2:
		return 1
	else:
		return f_counter(n-1) + f_counter(n-2)

print(f_counter(20)) 
print(counter)
'''
재귀 호출되는 카운터를 숫자로 찍어보니 기하급수적으로 늘어나고..이로 인해서
엄청 느려지는 소스가 작성된다.
원인) 재귀 호출 과정에서 중복되는 처리가 점점 많아져서 문제가 된다.
	> 이 설명은 교제 또는 알고리즘 퍼즐 2강에서 참고
f_counter(20) : 카운터는 13529
f_counter(30) : 카운터는 1664079
'''