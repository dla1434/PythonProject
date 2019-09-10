
# with를 사용하면 file.close로 별도로 호출하지 않아도
# with 구문이 끝날때 자동으로 file.close를 호출하게 된다.
with open("test.txt", "a") as file:
	file.write("안녕하세요")


with open("test.txt", "r") as file:
	print(file.read())