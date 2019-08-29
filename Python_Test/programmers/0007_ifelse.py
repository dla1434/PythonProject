
SCISSOR = '가위'
ROCK = '바위'
PAPER = '보'

WIN = '이겼다'
DRAW = '비겼다'
LOSE = '졌다'

me = '가위'
yours = '바위'

if  me == yours:
	result = DRAW
else:
	if me == SCISSOR:
		if yours == ROCK:
			result = LOSE
		else:
			result = WIN
	elif me == ROCK:
		if yours == PAPER:
			result = LOSE
		else:
			result = WIN
	elif me == PAPER:
		if yours == SCISSOR:
			result = LOSE
		else:
			result = WIN
	else:
		print('잘 못 내셨네..')

print(result)