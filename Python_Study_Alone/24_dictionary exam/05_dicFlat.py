# 딕셔너리를 선언합니다.
character = {
	"name": "기사",
	"level": 12,
	"items": {
		"sword": "불꽃의 검",
		"armor": "풀플레이트"
	},
	"skill": ["베기", "세게 베기", "아주 세게 베기"]
}

# for 반복문을 사용합니다.
	# type으로 딕셔너리의 값을 분류해서 처리합니다. ex) dict, list
for key in character:
	if type(character[key]) is dict:
		for small_key in character[key]:
			# print(small_key, ":", character[key][small_key])
			# character[key][small_key]는 풀어쓰면 아래 처리와 동일하다.
				# character[key] ---> "items": {"sword": "불꽃의 검"..."
				# {"sword": "불꽃의 검"..."에서 small_key인 sword로 조회
			print("{} : {}".format(small_key, character[key][small_key]))
	elif type(character[key]) is list:
		for item in character[key]:
			print(key, ":", item)
	else:
		print(key, ":", character[key])
