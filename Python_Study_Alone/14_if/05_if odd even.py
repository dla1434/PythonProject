# 입력을 받습니다.
number = input("정수를 입력해주세요: ")

# 현재 number 변수가 문자열이라서 [-1]이 가능합니다.
	# 문자열의 오른쪽에서 첫번째 문자를 가져온다.
last_character = number[-1]
print("last_character : ", last_character)
last_character = int(last_character)

# if 조건식이 한 줄로 입력하기 너무 긴 경우라서 \를 사용해서 처리했다.
if last_character == 0 or last_character == 2 or last_character == 4 \
	or last_character == 6 or last_character == 8:
	print("짝수입니다")

if last_character == 1 or last_character == 3 or last_character == 5 \
	or last_character == 7 or last_character == 9:
	print("홀수입니다")


# in을 사용하면 간단하게 비교할 수 있다.
	# 주의점) in의 경우 비교 변수가 문자열이여야 한다..
	# 위에 last_character를 int로 변환한 걸 그대로 사용하면 에러가 발생된다.
last_character = number[-1]

if last_character in "02468":
	print("짝수입니다")

if last_character in "13579":
	print("홀수입니다")
