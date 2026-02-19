# pip install pyttsx3

import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-70)

def speak(text):
    engine.say(text)
    engine.runAndWait()
