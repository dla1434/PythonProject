
numbers = [1,2,3,4,5,6,7,8,9]
output_type1 = [[], [], []]
output_type2 = [[], [], []]

for number in numbers:
	output_type1[number % 3].append(number)
	# 숫자 순서대로 배열 위치도 조정하고 싶다면
	output_type2[(number-1) % 3].append(number)

print(output_type1)
print(output_type2) 