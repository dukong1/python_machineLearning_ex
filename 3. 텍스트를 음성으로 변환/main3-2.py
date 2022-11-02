from gtts import gTTS
from playsound import playsound
import os

# 경로를 .py파일의 실행경로로 이동, 현재 경로로 이동#
os.chdir(os.path.dirname(os.path.abspath(__file__)))

text = "hello my name is seo jin woo mola JJAsa"

tts = gTTS(text=text, lang='ko')
tts.save("hi.mp3")

playsound("hi.mp3")
