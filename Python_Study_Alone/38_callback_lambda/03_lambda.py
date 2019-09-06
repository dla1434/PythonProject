
def call_10_times(func):
	for i in range(10):
		func(i)

'''
간단한 함수의 경우 함수 정의 없이 바로 정의해서 처리하고 싶을 것이다.
이런 경우 파이썬에서는 람다를 이용한다.

1. 람다 함수는 앞에 lambda를 붙인다.
2. lambda 뒤에는 매개변수 + ':' + 실행될 한줄짜리 소스 코드
	> 보통 다른 언어에서는 화살표를 쓰는데..여기는 :거네..흠..
3. return은 없나요?
	> 매개 변수 뒤에 return이 있다고 생각하면 된다..생략이 가능해서 생략된 형태로 많이 작성한다.
	lambda number: return print("안녕하세요", number)
'''
call_10_times(lambda number: print("안녕하세요", number))