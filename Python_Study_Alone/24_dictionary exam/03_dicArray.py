
# 딕셔너리를 선언합니다.
pets = [
	{"name": "구름", "age": 5}, 
	{"name": "초코", "age": 3},
	{"name": "아지", "age": 1},
	{"name": "호랑이", "age": 1}
]

print("# 우리 동네 애완 동물들")
for pet in pets:
	# print("{}는 {}살".format(pet["name"], str(pet["age"]))) 
	# str 형변환이 생략되도 정상 출력 된다.
	print("{}는 {}살".format(pet["name"], pet["age"]))
