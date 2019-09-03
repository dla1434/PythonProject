
# 1~100 / 2진수 / 0이 하나만 포함된 숫자 > 합!!
output = [i for i in range(0, 101) if "{:b}".format(i).count("0") == 1]
for i in output:
	print("{} : {}".format(i, "{:b}".format(i)))

print(output)
print("합계 : {}".format(sum(output)))


