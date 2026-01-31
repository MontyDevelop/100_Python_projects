import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes


def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print("Not understanding..")
# sptext()

def textsp(x):
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice',voice[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 120)
    engine.say(x)
    engine.runAndWait()

# textsp("Hello everyone how are u")

if __name__ == "__main__":

    while True:
        voice_data = sptext().lower()
        if voice_data == "hello":
            textsp('hello good morning how can i help u today')
        elif voice_data == "what is your name":
            textsp('my self jarvis you voice assistant')
        elif voice_data == "what is the date today":
            textsp('today 15 of january 2026')

    # voice_data = sptext().lower()
    # if voice_data == "hello jarvis":
    #     textsp("hello monty how are u")