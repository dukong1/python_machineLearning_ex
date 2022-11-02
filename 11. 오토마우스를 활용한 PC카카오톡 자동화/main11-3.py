import pyautogui
import pyperclip
import time
import threading  # threading 라이브러리 사용: 자기 자신의 함수를 호출하는 코드 생성 가능
import os

# 경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# 경로를 현재 .py파일을 실행하는 경로로 이동.
# pyautogui에서 한글을 인식하지 못해 경로를 이동하였다.


def send_message():  # 카톡에 메세지를 보내는 코드를 send_message()함수로 만듬
    threading.Timer(10, send_message).start()  # send_message()함수를 10초 후에 실행
    # 자신의 함수에서 10초 후에 자신의 함수를 다시 불러오기 때문에 10초 마다 메세지 전송됨

    picPosition = pyautogui.locateOnScreen('pc1.png')
    print(picPosition)
    # pic1.png 파일과 동일한 그림을 찾아 좌표를 출력

    if picPosition is None:
        picPosition = pyautogui.locateOnScreen('pc2.png')
        print(picPosition)
        # 앞의 사진에서 좌표를 찾지 못하였다면 pic2.png 파일과 동일한 그림을 찾아 좌표를 출력

    if picPosition is None:
        picPosition = pyautogui.locateOnScreen('pc3.png')
        print(picPosition)
        # 앞의 사진에서 좌표를 찾지 못하였다면 pic3.png 파일과 동일한 그림을 찾아 좌표를

    clickPosition = pyautogui.center(picPosition)
    # 이미지에서 찾은 좌표의 중간 좌표값을 찾는다.

    pyautogui.doubleClick(clickPosition)
    # 더블클릭 한다. -> 카카오톡 메세지 전송창이 열린다.

    pyperclip.copy("이 메세지는 자동으로 보내지는 메세지입니다.")
    pyautogui.hotkey("ctrl", "v")  # hotkey??
    time.sleep(1.0)
    # 문구를 넣은 후 1초 딜레이 -> 딜레이를 거는 이유??

    pyautogui.write(["enter"])
    time.sleep(1.0)
    # 엔터 입력 후 1초 딜레이

    pyautogui.write(["escape"])
    time.sleep(1.0)
    # esc를 눌러 창 닫고 1초 딜레이


send_message()  # 처음 한 번 send_message()함수 실행
# 이후에는 threading.Timer에 의해 10초 마다 불러지게 된다.
