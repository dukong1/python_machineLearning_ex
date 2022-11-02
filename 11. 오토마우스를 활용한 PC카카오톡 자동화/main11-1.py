import pyautogui
import os

# 경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

picPosition = pyautogui.locateOnScreen('pc1.png')
print(picPosition)

if picPosition is None:
    picPosition = pyautogui.locateOnScreen('pc2.png')
    print(picPosition)

if picPosition is None:
    picPosition = pyautogui.locateOnScreen('pc3.png')
    print(picPosition)
