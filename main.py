import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
import time
from googletrans import Translator

duration = 5
sample_rate = 44100

lang = input("Введите код языка для перевода (например, 'en' — английский, 'es' — испанский): ")

print("="*70 + "/n")
print("the proggram is recording your voice")
time.sleep(1)
print("Recording started")
time.sleep(0.5)

recording = sd.rec(
  int(duration * sample_rate), # длительность записи в сэмплах
  samplerate=sample_rate,      # частота дискретизации
  channels=1,                  # 1 — это моно
  dtype="int16")               # формат аудиоданных
sd.wait()  # ждём завершения записи

wav.write("newaudio.wav", sample_rate, recording)
time.sleep(0.5)
print("recording finished")
time.sleep(0.5)

translator = Translator()

recognizer = sr.Recognizer()
with sr.AudioFile("newaudio.wav") as source:
    audio = recognizer.record(source)
    
    
try:
    text = recognizer.recognize_google(audio, language="ru-RU")
    print(text)
    translated = translator.translate(text, dest=lang)  # здесь 'en' — это английский
    print("🌍 Перевод:", translated.text)
except sr.UnknownValueError:
    print("what the hell are you even saying")
except sr.RequestError as e:
    print("Я не могу достучаться до сервера, вот ошибка:", e)