
# 1~100 / 2진수 / 0이 하나만 포함된 숫자 > 합!!
# for i in range(1, 100 + 1):
	# 이건 윤인선 강사가 즐겨하는 방식임..아래처럼 101로 해도 됨

output = 0
for i in range(1, 101):
	# 2진수로 변환된 값에서 0의 개수가 하나만 있는 경우
	if "{:b}".format(i).count("0") == 1:
		# 1~100 / 2진수 출력
		print("{} : {:b}".format(i, i))
		output += i

print("합계 : {}".format(output))


