
# 개발 중에 조건문만 작성하고..내부 처리는 주석으로 처리하는 경우가 있는데..
# python에서는 다음과 같은 경우 에러가 발생된다.

# 숫자
number = 0 # 나중에!

if number != 0:
	# 이런 처리
else:
	# 이런 처리
	# 에러 발생 : IndentationError: expected an indented block
	