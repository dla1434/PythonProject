
array = [273, 52, 103, 32, 57]

for element in array:
	print(element)

# for문에서 몇번째 반복인지 표시하기 : 기본 for
i = 0
for element in array:
	print("{} : {}".format(i, element))
	i += 1

print()

# for문에서 몇번째 반복인지 표시하기 : enumerate 사용
for i,element in enumerate(array):
	print("{} : {}".format(i, element))

print()

# for문에서 몇번째 반복인지 표시하기 : range 사용
for i in range(len(array)):
	print("{} : {}".format(i, array[i])) 