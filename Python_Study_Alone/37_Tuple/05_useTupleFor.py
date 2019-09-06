
'''
enumerate 사용시 두 개의 인자를 받는데 이것도 튜플이었다.
원래대로라면 가로를 감싸는 형태이겠지만..튜플은 가로를 생략할 수 있다
	for (i, value) in enumerate([1,2,3,4,5,6]):
'''
for i, value in enumerate([1,2,3,4,5,6]):
	print("{}번째 요소는 {}입니다.".format(i, value))