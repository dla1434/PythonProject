
# 선언시 []에서 ()로 변경된거 이외에는 배열과 동일하다.
a = (1,2,3,4)
print(a[0])
print(a[1])
print(a[2])
print(a[3])

# 배열과 다른점은 수정을 못한다.
	# 에러 : TypeError: 'tuple' object does not support item assignment
a[0] = 100