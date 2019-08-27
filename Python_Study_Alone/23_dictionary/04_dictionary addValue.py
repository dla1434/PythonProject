
딕셔너리 = {
	"문자열": "값A",
	273: [1,2,3,4],
	True: False,
	(1,2): True
}

for key in 딕셔너리:
	print("키 : {}, 값 : {}".format(key, 딕셔너리[key]))

# 딕셔너리에 값 추가는 그냥 새로운 키를 지정해서 넣으면 된다.
딕셔너리["뉴키"] = "뉴값"
print()
for key in 딕셔너리:
	print("키 : {}, 값 : {}".format(key, 딕셔너리[key]))
