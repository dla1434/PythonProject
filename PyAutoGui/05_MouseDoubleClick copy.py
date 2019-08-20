import pyautogui
import time

pyautogui.moveTo(1707, 452)

pyautogui.doubleClick()

time.sleep(1)

pyautogui.typewrite('Hello')
pyautogui.typewrite(['enter'])

pyautogui.typewrite(['a','b','c','enter'])
# 'abc'는 안 된다..왜냐하면 저건 문자열이 아닌 키보드 키를 나타내기 때문이다.
# [] 안에는 키보드에 대한 문자열이 아닌 키보드 키를 의미하는 것이므로 주의하자

