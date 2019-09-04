
def print_n_times(value, n):
	for i in range(n):
		print(value)

print_n_times("안녕하세요", 5)

# 매개변수 개수가 안 맞으면 에러가 발생된다.
	# 에러 내용 : TypeError: print_n_times() missing 1 required positional argument: 'n'
print_n_times("안녕하세요")
print_n_times("안녕하세요", 5, 100)
