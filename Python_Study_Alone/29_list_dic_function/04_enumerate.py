
a = [273,103,52,32,57]
print(list(enumerate(a)))
# 인덱스 순서와 값이 쌍으로 이루워진 새로운 형태의 리스트로 출력된다.
# [(0, 273), (1, 103), (2, 52), (3, 32), (4, 57)]

# for (i, element) in enumerate(a):
for i, element in enumerate(a):
	print("{}번째  요소는 {}입니다".format(i, element))