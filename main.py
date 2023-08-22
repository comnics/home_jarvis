# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from gtts import gTTS
from playsound import playsound
import speech_recognition as sr


def start():
    greeting("밸라 바보님")

    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Say Something")
            # r.adjust_for_ambient_noise(source, duration=0.2)
            speech = r.listen(source)

        try:
            audio = r.recognize_google(speech, language="ko-KR")
            print("Your speech thinks like\n " + audio)
        except sr.UnknownValueError:
            print("Your speech can not understand")
            r = sr.Recognizer()
            continue
        except sr.RequestError as e:
            print("Request Error!; {0}".format(e))


def greeting(name):
    text = f"""
        안녕하세요, {name}. 저는 자비스 입니다.
        
        오늘 알렉스에게 책을 일억권 사줘.아니면 오늘 시크릿 인베이전 못봐.
        또는 해리포터 불의 잔 없음 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
        """
    lang = "ko"

    tts = gTTS(text=text, lang=lang)
    tts.save("tts.mp3")
    playsound("tts.mp3")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    text = "안녕, 알렉스!"
    lang = "ko"

    tts = gTTS(text=text, lang=lang)
    tts.save("tts.mp3")
    playsound("tts.mp3")

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something")
        speech = r.listen(source)

    try:
        audio = r.recognize_google(speech, language="ko-KR")
        print("Your speech thinks like\n " + audio)
    except sr.UnknownValueError:
        print("Your speech can not understand")
    except sr.RequestError as e:
        print("Request Error!; {0}".format(e))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    start()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
