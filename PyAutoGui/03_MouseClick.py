import pyautogui

pyautogui.moveRel(0,300, 2)

pyautogui.click()

# 더블 클릭 방법1
  # 더블 클릭 : clicks=2
  # 클릭 인터벌 : interval=2
pyautogui.click(clicks=2, interval=2)