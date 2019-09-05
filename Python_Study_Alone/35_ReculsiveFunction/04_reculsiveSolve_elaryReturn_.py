
'''
03_reculsiveSolve_memorization.py에서는 if, else를 구현해서 처리했는데
if return으로 조기에 리턴을 처리하면..else가 없어도 된다..
	이 경우 들여쓰기가 한단계 없어지므로 좀 더 깔끔하게 소스 작성이 가능해진다.
'''

메모 = { 1: 1, 2: 1 }
def f(n):
	if n in 메모:
		return 메모[n]

	output = f(n-1) + f(n-2)
	메모[n] = output
	return output		

print(f(150))