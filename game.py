import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
import time
from googletrans import Translator
import random

#Introducion
print("Welcome, this is is a game where we type a russian word and you need to say it in english")

#Variables
errors = 0
points = 0
max_errors = 3
loser = 0

words_by_level = {
    "easy": ["кот", "собака", "яблоко", "молоко", "солнце"],
    "medium": ["банан", "школа", "друг", "окно", "жёлтый"],
    "hard": ["технология", "университет", "информация", "произношение", "воображение"]
}

#Main code

difficulty = input("Choose your difficulty (easy, medium, hard)")

random.shuffle(words_by_level[difficulty])

for word in words_by_level[difficulty]:
    
    print("!!say", word, "in english!!")
    time.sleep(0.5)
    print("the proggram will be recording your voice")
    time.sleep(1)
    print("Recording started")

    recording = sd.rec(
        int(3 * 44100), # длительность записи в сэмплах
        samplerate=44100,      # частота дискретизации
        channels=1,                  # 1 — это моно
        dtype="int16")               # формат аудиоданных
    sd.wait()

    wav.write("newaudio.wav", 44100, recording)
    time.sleep(0.5)
    print("recording finished")
    time.sleep(0.5)
    
    translator = Translator()

    recognizer = sr.Recognizer()
    with sr.AudioFile("newaudio.wav") as source:
        audio = recognizer.record(source)
        
        
    try:
        text = recognizer.recognize_google(audio, language="en-EN").lower()
        print("you said:", text)
        time.sleep(0.4)
        translated_word = translator.translate(word, dest="en").text.lower()  # здесь 'en' — это английский
        print("and you needed to say:", translated_word)
        time.sleep(0.4)

        if text == translated_word:
            print("good job")
            points += 1
        else:
            print("You suck")
            errors += 1
        time.sleep(0.5)

    
    
    except sr.UnknownValueError:
        print("what the hell are you even saying")
        errors += 1
        time.sleep(0.5)
    except sr.RequestError as e:
        print("Я не могу достучаться до сервера, вот ошибка:", e)
    
    print("you have", points, "points and", errors, "errors")
    if errors >= max_errors:
        print("game over bozo (you reached 3 errors)")
        time.sleep(0.5)
        print("final score:", points)
        loser = 1
        break
    
    time.sleep(2.5)

if loser != 1:
    print("great job twink you got", points, "points and made mistakes", errors, "times.")