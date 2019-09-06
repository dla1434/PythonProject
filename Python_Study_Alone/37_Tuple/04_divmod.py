
# 기존 : 몫과 나머지를 구함
a, b = 97, 40
print(a // b)
print(a % b)

# 신규 : 한번에 구할 수 있는 함수가 있다..그건 divmod
print(divmod(a,b))
print(type(divmod(a,b)))

몫, 나머지 = divmod(a,b)
print('몫',몫)
print('나머지', 나머지)