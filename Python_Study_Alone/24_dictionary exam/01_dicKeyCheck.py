
dictionary = {
	"이름": "구름",
	"종족": "강아지"
}

dictionary["이름"]
# dictionary["나이"] # Error : 없는 키로 조회해서 에러 발생

# 키가 있는 지 확인하고 처리하려면 if + in으로 체크할 수 있다.
if "나이" in dictionary:
	dictionary["나이"]
else:
	print("없는 키입니다.")