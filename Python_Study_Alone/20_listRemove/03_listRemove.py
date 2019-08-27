
# list의 함수 remove을 사용한 제거
	# 리스트 값을 지정하여 삭제
list = [100,200,300,400,500]
# pop : 위치로 제거되고 제거되는 값이 반환된다.
# remove : 배열값으로 제거되고 값이 반환되지 않는다.
print(list.remove(100))
print(list)


# 중복되는 값이 있는 경우 리스트의 순서에서 가장 앞에 있는 값 하나만 제거된다.
list = [100,100,100,100,100]
print(list.remove(100))
print(list)