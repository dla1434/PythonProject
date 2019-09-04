
# 조건이 맞으면 NotImplemetedError (선언되지 않은 에러) 를 발생시켜 다중 for 문을 바로 종료시키는 방법입니다. 
try:
	for a in range(5):
		for b in range(3):
			if a == 2 and b == 2:
				print(a, ',',  b)
				raise NotImplementedError
			else:
				print(a, ',',  b)
except:
	print('end')