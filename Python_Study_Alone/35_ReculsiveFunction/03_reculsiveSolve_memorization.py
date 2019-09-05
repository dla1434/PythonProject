
# 메모화(memorization)으로 02_reculsiveProblem.py 문제를 해결할 수 있다.
	# 재귀호출 시 처리된 결과를 딕셔너리에 담고..중복된 처리가 있는 경우 skip 처리

메모 = {
	1: 1,
	2: 1
}

# 참고 : 메모에 접근할때는 왜 global을 선언하지 않아도 되는가?
	# 이전에서 함수 내부에서 외부 변수에 접근하기 위해서는 global을 선언해야 한다고 했는데
	# 여기서는 그냥 접근이 된다..왜냐하면 레퍼런스 변수는 그냥 접근이 된다.
def f(n):
	if n in 메모:
		return 메모[n]
	else:
		output = f(n-1) + f(n-2)
		메모[n] = output
		return output		

print(f(150))