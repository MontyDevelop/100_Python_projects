import speech_recognition as sr 
from requests_html import HTMLSession
import speak


def spech_to_text():
    r =  sr.Recognizer()
    with sr.Microphone() as source:
      r.adjust_for_ambient_noise(source, duration=0.5)
      audio = r.listen(source) # methord 
      voice_data = ''
      try:
        voice_data = r.recognize_google(audio)
        return voice_data

      except sr.UnknownValueError:
             speak.speak("sorry")
      except sr.RequestError:
            speak.speak('No internet connect please turn on you internet')  


