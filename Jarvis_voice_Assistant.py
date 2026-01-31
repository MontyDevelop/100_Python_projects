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

    voice_data = sptext().lower()
    print(voice_data)
    if "your name" in voice_data:
        name = 'Hello i am Jarvis.'
        textsp(name)
    elif "old are you" in voice_data:
        age = "i am two years old machine"
        textsp(age)
    elif "time" in voice_data:
        current_time = datetime.datetime.now().strftime("%I%M%p")
        textsp(current_time)
    elif 'youtube' in voice_data:
        webbrowser.open("https://www.youtube.com/")
    elif 'joke' in voice_data:
        joke1 = pyjokes.get_joke(language='en', category='neutral')
        print(joke1)
        textsp(joke1)