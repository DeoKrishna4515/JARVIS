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

def spcl_day():
    today = f"{day}/{month}"

#<----------------------------------------------------------

    if today == "1/1":
        print("Sir, Today is New Year")
        speak("Sir, Today is New Year")

    elif today == "9/1":
        print("Today is Guru Gobind Singh Jayanti, Sir")
        speak("Today is Guru Gobind Singh Jayanti, Sir")

    elif today == "10/1":
        print("Sir, today is a very special day for you. Guesss What? Today is your dad's birthday")
        speak("Sir, today is a very special day for you. Guesss What? Today is your dad's birthday")

    elif today == "13/1":
        print("Sir, Today is Lohri")
        speak("Sir, Today is Lohri")

    elif today == "14/1":
        print("Sir, Today are multiple festivals like,\n Makar Sankranti, Pongal, Bihu and, Uttarayan")
        speak("Sir, Today are multiple festivals like,\n Makar Sankranti, Pongal, Bihu and, Uttarayan")

    elif today == "26/1":
        print("Sir, Today is Republic Day")
        speak("Sir, Today is Republic Day")

#---------------------------------------------------------->
#<----------------------------------------------------------


    elif today == "1/2":
        print("Sir, Today is Losar")
        speak("Sir, Today is Losar")
    
    elif today == "5/2":
        print("Sir, Today is Vasant Panchami")
        speak("Sir, Today is Vasant Panchami")

    elif today == "14/2":
        print("Sir, Today is Valentine's Day")
        speak("Sir, Today is Valentine's Day")

    elif today == "16/2":
        print("Sir, Today is Sant Ravidas Jayanti")
        speak("Sir, Today is Sant Ravidas Jayanti")

    elif today == "19/2":
        print("Sir, Today is Chhatrapati Shivaji Jayanti")
        speak("Sir, Today is Chhatrapati Shivaji Jayanti")

#---------------------------------------------------------->
#---------------------------------------------------------->

    elif today == "1/3":
        print("Sir, Today is Mahashivratri")
        speak("Sir, Today is Mahashivratri")

#---------------------------------------------------------->


    else:
        print("Today is nothing special, Sir.")
        speak("Today is nothing special, Sir.")