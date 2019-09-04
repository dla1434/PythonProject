# 함수 선언 시 매개변수값을 지정하면 기본값으로 설정된다
# 이 경우 함수 호출에서 해당 매개변수를 지정하지 않아도 정상적으로 수행된다.
'''
주의점1 : 기본 매개변수 다음에 일반 매개변수가 올수 없다..마지막에 기본 매개변수를 지정한다고 생각하면 될 듯
	에러 발생) def print_n_times(n=2, value):
		생각해보면 당연하다..매개변수가 기본매개변수 뒤에 위치하면..함수 호출 시 위치 때문에...
		매개변수 생략을 할 수 없다..그럼 의미가 없어진다.
'''
def print_n_times(value, n=2):
	for i in range(n):
		print(value)

# 기본 매개변수값을 지정한 경우 아래처럼 해당 매개변수를 지정하지 않아도 에러가 발생되지 않는다.
	# 기본 매개변수가 없는 일반 선언 시는 에러가 발생
print_n_times("안녕하세요")
print()

# 매개변수값을 지정한 경우..매개변수 기본값이 지정한 매개변수값으로 변경된다.
print_n_times("안녕하세요", 5)