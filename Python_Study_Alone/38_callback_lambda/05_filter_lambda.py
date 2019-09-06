
# 람다로 바로 filter를 처리할 수 있다.
a = list(range(100))
b = filter(lambda number: number % 2 == 0, a)

print(list(b))


# 람다도 변수로 담아서 사용 가능하다.
짝수만 = lambda number: number % 2 == 0
c = list(range(100))
d = filter(짝수만, a)

print(list(d))
