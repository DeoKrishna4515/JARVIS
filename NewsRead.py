import requests
import json
import pyttsx3
import speech_recognition as sr
import os
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 192)

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

def latestnews():
    api_dict = {"business":"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=4f2e8fb8683e4fd38fd32a156bccb3e1",
                "entertainment":"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=4f2e8fb8683e4fd38fd32a156bccb3e1",
                "health":"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=4f2e8fb8683e4fd38fd32a156bccb3e1",
                "science":"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=4f2e8fb8683e4fd38fd32a156bccb3e1",
                "sports":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=4f2e8fb8683e4fd38fd32a156bccb3e1",
                "suits":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=4f2e8fb8683e4fd38fd32a156bccb3e1",
                "fruits":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=4f2e8fb8683e4fd38fd32a156bccb3e1",
                "Technology":"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=4f2e8fb8683e4fd38fd32a156bccb3e1"

}

    content = None
    url = None
    engine.setProperty('rate',200)
    print("Which field news do you want, [business] , [health] , [entertainment] , [science] , [sports] , [technology]")
    speak("Which field news do you want, [business] [health] [entertainment] [science] [sports] [technology]")
    field = takeCommand()

    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            speak("url was found")
            break
        else:
            url = True
    if url is True:
        print("url was not found")
        speak("url was not found")

    news = requests.get(url).text
    news = json.loads(news)
    print("Here is the first news.")

    engine.setProperty('rate',185)

    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit{news_url}")