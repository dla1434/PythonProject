
# 리턴을 하나의 값이 아닌 여러개일 경우 튜플을 사용하면 효과적이다.
def test():
	return 10, 20

a,b = test()
print(a,b)