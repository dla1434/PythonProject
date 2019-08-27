
# list의 함수 pop을 사용한 제거
	# 지정된 인덱스 위치의 리스트값이 제거되고..반환값으로 제거된 값이 가져온다.
list = [1,2,3,4,5,6,7]
print(list.pop(1))
print(list)

# 인덱스 위치를 지정하지 않으면 자동으로 -1값..즉 배열의 마지막 값이 제거된다.
print(list.pop())
print(list)