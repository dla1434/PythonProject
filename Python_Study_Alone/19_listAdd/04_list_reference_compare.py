
# 비파괴적 함수
	# 쉽게 생각하면 메소드 호출 시 원래변수 값은 유지하고..
	# 메소드를 수행한 반환값만 변경되는 구조이다.
a = "hello"
print(a)
print(a.upper())


# 파괴적함수 : 레퍼런스 처리
	# 메소드 호출 시 원래변수값이 변경되는 구조
	# ex) append, extends
a = [1,2,3]
a.append(4)
print(a)


# append 처리를 비파괴적으로 처리하려면? 연산자를 활요하면 된다.
a = [1,2,3]
print(a + [4])
print(a)


