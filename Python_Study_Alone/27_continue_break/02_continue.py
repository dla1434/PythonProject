
numbers = [5,15,6,20,7,25]

for number in numbers:
	# 10보다 작으면 아래 소스를 실행하지 않고 다시 for 반복문으로 넘어간다.
	if number < 10:
		continue #현재 반복을 중지하고 다음 반복으로 넘어간다.
	
	print(number)