import speech_recognition  as sr
import os
import sys
import webbrowser
import pyttsx3
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
from pyowm.weatherapi25 import observation





def talk(words):
    say = pyttsx3.init()
    say.say(words)
    say.runAndWait()

talk("Привет, пользователь, какой вопрос тебя интересует")

def command():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Говорите")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)

    try:
        zadanie = r.recognize_google(audio).lower()
        print("Вы сказали: " + zadanie)
    except sr.UnknownValueError:
        talk("Я вас не поняла")
        zadanie = command()

    return zadanie
def test(arg):
    owm = OWM('b7ca9e58889c65158dfe9994fce5f839')
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(str(arg))
    w = observation.weather

    temp1 = w.temperature('celsius')

    answer1 = ("В", arg, w.detailed_status, "сейчас")
    correcting = {'В': 'В', arg: arg, w.detailed_status: w.detailed_status, 'сейчас': 'сейчас', '"': '', ',': ''}
    final_correcting1 = []
    final_correcting2 = []
    for i in answer1:
        taking_key1 = correcting.get(i)
        final_correcting1.append(taking_key1)
    final_answer1 = " ".join(final_correcting1)

    middle_temp = temp1.get('temp')
    answer2 = ("и", float(middle_temp), "в среднем")
    correcting2 = {'и': 'и', float(middle_temp): str(middle_temp), 'в среднем': 'в среднем', '"': '', ',': ''}
    for i in answer2:
        taking_key2 = correcting2.get(i)
        final_correcting2.append(taking_key2)
    final_answer2 = " ".join(final_correcting2)

    final_answer = final_answer1 + ' ' + final_answer2
    talk(final_answer)

def makeSomething(zadanie):
    if 'open roblox' in zadanie:
        talk("уже выполняю")
        url = 'https://www.roblox.com/home'
        webbrowser.open(url)
    elif 'turn off' in zadanie:
        talk('До свидания')
        sys.exit()
    elif 'open youtube' in zadanie:
        talk('Уже выполняю')
        url = 'https://www.youtube.com'
        webbrowser.open(url)
    elif 'weather' in zadanie:
        talk('В каком городе хотите узнать погоду?')
        test(command())

while True:
    makeSomething(command())

