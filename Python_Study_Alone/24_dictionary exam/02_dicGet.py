
dictionary = {
	"이름": "구름",
	"종족": "강아지"
}

print(dictionary["이름"])
# dictionary의 get 함수를 이용해서 값을 가져올 수도 있다.
print(dictionary.get("이름"))

# get 사용 장점...키가 없는 경우 에러가 아닌 None값을 반환한다.
print(dictionary.get("나이"))
print()

if dictionary.get("나이") == None:
	print("없는 키입니다.")
else:
	print(dictionary.get("나이"))