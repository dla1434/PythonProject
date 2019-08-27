
# 리스트에 중복되는 숫자 개수 구하기
# 숫자는 무작위로 입력해도 상관 없습니다.
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

for number in numbers:
	if number in counter:
		# 이미 있던 숫자라면..값을 가지고 와서 1증가
		# counter[number] = counter[number] + 1
		counter[number] += 1
	else: 
		# counter에 해당 숫자가 없다면..즉..처음 나오는 숫자라면 1로 값 초기화
		counter[number] = 1

# 최종 출력
print(counter)
