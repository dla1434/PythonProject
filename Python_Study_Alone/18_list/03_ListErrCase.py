
a = [1,2,3,4,5]
# IndexError: list index out of range 에러 발생
	# 배열 크기를 넘어서 지정했기 때문에 발생
print(a[100])


# 슬라이싱할 때는 index out of range 에러 발생가 발생되지 않는다.
	# 사람들이 자주 실수하는 부분이라서 에러가 발생되지 않게 만든거 같다.
print(a[2:10000])