
list_of_list = [
	[1,2,3],
	[4,5,6,7],
	[8,9]
]

for list in list_of_list:
	# loop1 : [1,2,3], loop2 : [4,5,6,6], loop3 : [8,9]
	for element in list:
		print(element)