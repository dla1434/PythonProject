
'''
재귀 함수로 만들어서 리스트를 평탄화하는 함수를 만들어라
원본 : [[1,2,3],[4,[5,6],7,[8,9]]
변환 : [1,2,3,4,5,6,7,8,9]
'''
def flatten(data):
	output = []
	for item in data:
		if type(item) == list:
			output += flatten(item)
		else:
			# output.append(item)
			output += [item]
	return output

example = [[1,2,3],[4,[5,6]],7,[8,9]]
print("원본 : ", example)
print("변환 : ", flatten(example))
