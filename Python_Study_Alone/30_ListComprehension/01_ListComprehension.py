
array = []
for i in range(0, 20, 2):
	array.append(i * i)
print(array)	

# 위에 처럼 자주 사용하니깐..이걸 더 쉽게 사용하기 위해서 아래 리스트 내포라는 개념이 나왔다.
array = [i * i for i in range(0,20,2)]
print(array)


