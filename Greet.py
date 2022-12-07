import pyttsx3
import datetime

day = datetime.datetime.now().day
month = datetime.datetime.now().month

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 192)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def greet(): 
    hour = int(datetime.datetime.now().strftime('%H'))
    day = datetime.datetime.now().day
    month = datetime.datetime.now().month
    date = f"{day}/{month}"

    if hour < 12:
        text = 'Good Morning sir'
    elif hour < 17:
        text = 'Good Afternoon sir'
    else:
        text = 'Good Evening sir'

#<--------------------------------------------------------


    if date=="23/10":
        print(f'{text}, I wish you a very Happy Birthday!')
        speak(f'{text}, I wish you a very Happy Birthday!')

    elif date=="28/11":
        print(f'{text}, and I wish Sri-Ku a very happy birth day!, Happy Birthday Sri-Ku.')
        speak(f'{text}, and I wish Sri-Ku a very happy birth day!, Happy Birthday Sri-Ku.')

    elif date=="10/1":
        print(f'{text}, and I wish your dad a very happy birth day!, Happy Birthday Dear, Sir.')
        speak(f'{text}, and I wish your dad a very happy birth day!, Happy Birthday Dear, Sir.')

    elif date=="1/9":
        print(f'{text}, and I wish your mom a very happy birth day!, Happy Birthday Mam.')
        speak(f'{text}, and I wish your mom a very happy birth day!, Happy Birthday Mam.')

#-------------------------------------------------------->
#<--------------------------------------------------------

    elif date == "1/1":
        print(f"{text}, Happy New Year.")
        speak(f"{text}, Happy New Year.")

    elif date == "9/1":
        print(f"{text}, Happy Guru Gobind Singh Jayanti")
        speak(f"{text}, Happy Guru Gobind Singh Jayanti")

    elif date == "13/1":
        print(f"{text}, Happy Lohri")
        speak(f"{text}, Happy Lohri")

    elif date == "14/1":
        print(f"{text}, Happy Makar Sankranti")
        print(f"{text}, Happy Pongal")
        print(f"{text}, Happy Bihu")
        print(f"{text}, Happy Uttarayan")
        speak(f"{text}, Happy Makar Sankranti")
        speak(f"{text}, Happy Pongal")
        speak(f"{text}, Happy Bihu")
        speak(f"{text}, Happy Uttarayan")

    elif date == "26/1":
        print(f"{text}, Happy Republic Day")
        speak(f"{text}, Happy Republic Day")

#-------------------------------------------------------->
#<--------------------------------------------------------

    elif date == "1/2":
        print(f"{text}, Happy Losar")
        speak(f"{text}, Happy Losar")
    
    elif date == "5/2":
        print(f"{text}, Happy Vasant Panchami")
        speak(f"{text}, Happy Vasant Panchami")

    elif date == "14/2":
        print(f"{text}, Happy Valentine's Day")
        speak(f"{text}, Happy Valentine's Day")

    elif date == "16/2":
        print(f"{text}, Happy Sant Ravidas Jayanti")
        speak(f"{text}, Happy Sant Ravidas Jayanti")

    elif date == "19/2":
        print(f"{text}, Happy Chhatrapati Shivaji Jayanti")
        speak(f"{text}, Happy Chhatrapati Shivaji Jayanti")

#-------------------------------------------------------->
#<--------------------------------------------------------

    elif date == "1/3":
        print(f"{text}, Happy Mahashivratri")
        speak(f"{text}, Happy Mahashivratri")

#-------------------------------------------------------->


    else:
        print(f'{text}, welcome back, how may I help you ?')
        speak(text)
        speak('welcome back, how may I help you ?')

def greet_s():
    print("yes sir")
    speak("yes sir")