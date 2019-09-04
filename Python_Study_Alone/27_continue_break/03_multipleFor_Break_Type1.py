
# breaker 라는 변수를 추가해서 조건이 되는 경우 True 로 변경하고
# 내부 for 문을 빠져나올 때마다 조건을 확인해서 추가로 break 해주는 방법 입니다.
breakFlag = False
for a in range(5):
	for b in range(3):
		if a == 2 and b == 2:
			print(a, ',',  b)
			breakFlag = True
			break
		else:
			print(a, ',',  b)

	if breakFlag == True:
		break	