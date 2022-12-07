import pyttsx3
import speech_recognition as sr
from tkinter import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.energy_threshold = 400
        audio = r.listen(source)
    
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'You said: {query}\n')

    except Exception as e:
        print(e)
        
        print('Say that again please...')
        speak('')

        return 'None'

    return query
    
if __name__ == "__main__":
    wait = False

    print('tell the time at which you want to set alarm.')
    speak('tell the time at which you want to set alarm.')
    tt = takeCommand()
    tt = tt.replace("set alarm to ", "")
    tt = tt.replace(".","")
    tt = tt.upper()
    import PyAlarm
    PyAlarm.alarm(tt)