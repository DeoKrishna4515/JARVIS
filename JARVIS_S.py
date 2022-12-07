import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import wikipedia as googleScrap
import webbrowser
import pyautogui
from tkinter import *
import os 
import cv2
import pywhatkit
import keyboard
import pyjokes
from PyDictionary import PyDictionary as Diction
from pywikihow import search_wikihow
import requests
from bs4 import BeautifulSoup
from plyer import notification
import psutil
from NewsRead import latestnews
from plyer import notification
from Greet import greet
from Special import spcl_day
from repeat_my_words import repeat
from RPS import game_play

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 191)

# Defining functions
def closeapps():
    speak('closing sir.')

    if 'close chrome' in query:
        os.system('TASKKILL /F /im chrome.exe')
    
    if 'close notepad' in query:
        os.system('TASKKILL /F /im notepad++.exe')

    if 'close code' in query or 'close vs code' in query or 'close visual studio code' in query:
        os.system('TASKKILL /F /im Code.exe')
    
    if 'close CMD' in query or 'close c m d' in query or 'close command prompt' in query:
        os.system('TASKKILL /F /im cmd.exe')
    
    if 'close whatsapp' in query:
        os.system('TASKKILL /F /im WhatsApp.exe')

def temp():
    search = "temperature of greater noida"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    url2 = "https://weather.com/en-IN/weather/tenday/l/INKA0344:1:IN"
    r2 = requests.get(url2)
    soup = BeautifulSoup(r2.content, 'html.parser')
    humid = soup.find("span", {"class":"DetailsTable--value--2YD0-"}).text
    wind = soup.find("span", {"class":"Wind--windWrapper--3Ly7c DailyContent--value--1Jers"}).text
    percip = soup.find("span", {"class":"DailyContent--value--1Jers"}).text
    temp = data.find("div",class_="BNeawe").text
    print(f"The temperature is: {temp}")
    speak(f"The temperature is: {temp}")
    print(f"The humidity is: {humid}")
    speak(f"The humidity is: {humid}")
    print(f"The wind is: {wind}")
    speak(f"The wind is: {wind}")
    print(f"The percipation is: {percip}")
    speak(f"and The percipation is: {percip}")
    
def Music(): 
    os.startfile('alarm.mp3')
    pyautogui.sleep(2)
    keyboard.press_and_release("space")

    print("Done Sir!")
    speak("Done Sir!")

def day():
    date = datetime.datetime.now()

    day = date.weekday()
    if day == 0:
        print('monday')
        speak('monday')
        pyautogui.sleep(0.5)

    elif day == 1:
        print("tuesday")
        speak('tuesday')
        pyautogui.sleep(0.5)

    elif day == 2:
        print("wednusday")
        speak('wednesday')
        pyautogui.sleep(0.5)

    elif day == 3:
        print("thursday")
        speak('thursday')
        pyautogui.sleep(0.5)

    elif day == 4:
        print("friday")
        speak('friday')
        pyautogui.sleep(0.5)

    elif day == 5:
        print("saturday")
        speak('saturday')
        pyautogui.sleep(0.5)

    elif day == 6:
        print('sunday')
        speak('sunday')
        pyautogui.sleep(0.5)

def Whatsapp():

    print("tell the name of the person you want to send message")
    speak("tell the name of the person you want to send message")
    name = takeCommand()
    print("tell the message you want to send")
    speak("tell the message you want to send")
    msg = takeCommand()

    os.startfile("C:\\Users\\kravi\\AppData\\Local\\WhatsApp\\WhatsApp.exe") 
    pyautogui.sleep(6)
    pyautogui.moveTo(46,136)
    pyautogui.sleep(1)
    pyautogui.click()
    pyautogui.write(name)
    pyautogui.sleep(1)
    pyautogui.moveTo(60,297)
    pyautogui.sleep(0.5)
    pyautogui.click()
    pyautogui.sleep(0.5)
    pyautogui.moveTo(750,983)
    pyautogui.sleep(0.5)
    pyautogui.click()
    pyautogui.write(msg)
    pyautogui.moveTo(1873,974)
    pyautogui.click()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    print(f"{date}/{month}/{year}")
    speak(f"{date}, {month}, {year}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.energy_threshold = 400
        audio = r.listen(source)
    
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        query = query.lower()
        print(f'You said: {query}\n')

    except Exception as e:
        print(e)
        
        print('Say that again please...')

        return 'None'

    return query

def SpeedTest():
    import speedtest
    print('checking speed.....')
    speak("checking speed")
    speed = speedtest.Speedtest()
    downloading = speed.download()
    correctDown = int(downloading/800000)
    uploading = speed.upload()
    correctUp = int(uploading/800000)

    if 'uploading' in query:
        print(f"the uploading speed is: {correctUp} mbps")
        speak(f"the uploading speed is {correctUp} mbps")

    elif 'downloading' in query:
        print(f"the downloading speed is: {correctDown} mbps")
        speak(f"the downloading speed is {correctDown} mbps")

    else:
        print(f"the downloading speed is: {correctDown} mbps, and the uploading speed is: {correctUp} mbps")
        speak(f"the downloading speed is {correctDown} mbps and the uploading speed is {correctUp} mbps")

def itref():
    pyautogui.moveTo(1706,1049)
    pyautogui.click()
    pyautogui.click()
    pyautogui.moveTo(1506,569)
    pyautogui.click()
    pyautogui.click()
    cv2.waitKey(2000)
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    cv2.waitKey(2000)
    pyautogui.moveTo(1706,1049)
    pyautogui.click()
    pyautogui.click()

# M A I N      C O D E
if __name__ == "__main__":
    wait = False
    # greet() 
    while True:
        
        if wait == False:
            query = takeCommand().lower()

        if 'alarm' in query:
            os.startfile('alarm.py')

        elif 'temperature' in query or 'weather' in query:
            temp()

        elif 'score' in query or 'ipl' in query:
            url = "https://www.cricbuzz.com/"
            page = requests.get(url)
            soup = BeautifulSoup(page.text,"html.parser")
            div = soup.find_all(class_ = "cb-pos-rel")[0]

            try:
                result = div.find(class_= "cb-ovr-flo cb-text-live").text
            except:
                result = div.find(class_= "cb-ovr-flo cb-text-complete").text
            team1 = div.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
            team2 = div.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
            team1_score = div.find_all(class_ = "cb-ovr-flo")[2].get_text()
            team2_score = div.find_all(class_ = "cb-ovr-flo")[4].get_text()

            notification.notify(
                app_icon = "C:\\Users\\kravi\\Downloads\\ipl-logo.ico",
                title = f"In the match of {team1} v/s {team2}: {result}",
                message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
            )

            print(f"In the match of {team1} v/s {team2}: {result}")
            print(f"{team1} : {team1_score}")
            print(f"{team2} : {team2_score}")
            speak(f"In the match of {team1} versus {team2}: {result}")
            speak(f"{team1}'s score is {team1_score}")
            speak(f"{team2}'s score is {team2_score}")

        elif 'special' in query or 'today' in query:
            spcl_day()

        elif 'translator' in query:
            print("Opening Translator")        
            speak("Opening Translator")
            webbrowser.open("https://www.bing.com//translator?ref=TThis&text=&from=en&to=hi")

        elif 'calculator' in query:
            print("opening.")
            speak("opening.")
            os.startfile("C:\\Windows\\System32\\calc.exe")

        elif 'news' in query or 'new' in query:
            latestnews()

        elif 'when is your birthday' in query:
            print("I celebrate my birthday on 16 november because I was started being made on 16 november 2021")
            speak("I celebrate my birthday on 16 november because I was started being made on 16 november 2021")
        elif query=='happy birthday' or query=='happy birthday jarvis':
            print("ThankYou Sir.")
            speak("ThankYou Sir.")

        elif 'love' in query:
            print("Yes,I love you a lot.")
            speak("Yes,I love you a lot.")

        elif 'battery' in query or 'power' in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            print(f"sir our system has {percentage} percent battery.")
            speak(f"sir our system has {percentage} percent battery.")

        elif 'joke' in query:
            get = pyjokes.get_joke()
            print(get)            
            speak(get)
       
        elif "rock" in query or "paper" in query or "caesar" in query or "scissor" in query or "scissors" in query or "game" in query:
            game_play()

        elif 'repeat' in query:
            repeat()

        elif 'how to' in query:
            print('Getting data from the internet!')
            speak('getting data from the internet!')
            op = query.replace("jarvis","")
            max_result = 1
            how_to_func = search_wikihow(op,max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            speak(how_to_func[0].summary)

        elif 'downloading speed' in query or 'uploading speed' in query or 'internet speed' in query:
            SpeedTest()
        elif 'uploading speed' in query:
            SpeedTest()
        elif 'internet speed' in query:
            SpeedTest()

        elif 'gmail' in query or 'email' in query:
            print('opening sir, please wait')
            speak('opening sir, please wait')
            webbrowser.open('https://mail.google.com/mail/u/0/#inbox')

        elif 'play' and 'music' in query:
            Music()
        elif 'play' and 'song' in query:
            query.lower()
            query = query.replace('jarvis', '')
            query = query.replace('play', '')
            query = query.replace('open', '')
            query = query.replace('on', '')
            query = query.replace('youtube', '')
            pywhatkit.playonyt(query)
            speak('your song is here. enjoy sir!')
        
        elif 'close' in query:
            closeapps()

        elif 'message' in query:
            Whatsapp()

        elif 'whatsapp' in query:
            print("Opening WhatsApp.")
            speak("Opening WhatsApp.")
            os.startfile("C:\\Users\\kravi\\AppData\\Local\\WhatsApp\\WhatsApp.exe")

        elif 'screenshot' in query or 'screen shot' in query or 'hot' in query:
            speak('what should I name the file sir.')
            filename = takeCommand()
            mainfilename = filename + ".jpg"
            path1 = "C:\\Users\\kravi\\Desktop\\School\\DEO\\programing_deo\\JARVIS\\ScreenShot\\" + mainfilename
            img = pyautogui.screenshot()
            img.save(path1)
            speak('done sir')
            print('done sir')

        elif 'good' in query:
            print("thanks sir")
            speak("thanks sir")

        elif 'how are you' in query or "what's up" in query:
            print("I am fine, and you ?")
            speak("I am fine, and you ?")

        elif 'created jarvis' in query or 'created you' in query:
            print("I was created by a god-like human")
            speak("I was created by a god-like human")

        elif 'what is the law of nature' in query:
            print("to kill and to be killed, to grow and to die ,and get decomposed is the law of nature")
            speak("to kill and to be killed, to grow and to die ,and get decomposed is the law of nature")

        elif 'yourself' in query or 'what are you' in query:
            print("My name is jarvis . I am a desktop assistant . A desktop assistant is a program which does all the work you want him to do. I was created by a person named deo krishna.")
            speak("My name is jarvis . I am a desktop assistant . A desktop assistant is a program which does all the work you want him to do. I was created by a person named deo krishna.")

        elif 'what can you do' in query:
            print("Sir, I am a deskptop assistant which can make your work easier. I can do a lot of work like, playing songs and music, searching across wikipedia and google, playing some videos for you, playing a game with you , telling you date time and day, search dictionary, and many more with just your speech.")
            speak("Sir, I am a deskptop assistant which can make your work easier. I can do a lot of work like, playing songs and music, searching across wikipedia and google, playing some videos for you, playing a game with you , telling you date time and day, search dictionary, and many more with just your speech.")

        elif 'thanks' in query or 'thank you' in query:
            print("My pleasure !")
            speak("My pleasure !")

        elif 'wikipedia' in query:
            query.lower()
            query = query.replace('jarvis', '')
            query = query.replace('search', '')
            query = query.replace('open', '')
            query = query.replace('wikipedia', '')

            speak(f'Searching {query} in wikipedia')
            try:
                result = wikipedia.summary(query, sentences = 4)
                speak('According to wikipedia:')
                print(result)
                speak(result)
            except Exception as e:
                print('Sorry, your query is not available in wikipedia')
                speak('Sorry, your query is not available in wikipedia')

        if 'what' and 'time' in query:
            print(datetime.datetime.now().strftime('%I:%M:%S %p'))
            speak(datetime.datetime.now().strftime('%I:%M:%S %p'))
        if 'what' and 'date' in query:
            date()
        if 'which' and 'day' in query:
            day()

        elif 'open youtube' in query:
            speak('opening Youtube')
            webbrowser.open('youtube.com')
        elif 'youtube search' in query:
            query = query.replace("jarvis", "")
            query = query.replace("youtube search", "")
            web66 = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web66)
            speak('done sir , this is what i found for your search')
            
        elif 'open notepad' in query or 'open note pad' in query:
            speak('opening notepad')
            npath = "C:\\Program Files\\Notepad++\\Notepad++.exe"
            os.startfile(npath)

        elif 'open vs code' in query or 'open visual studio code' in query:
            speak('opening')
            npath = "C:\\Users\\kravi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(npath)

        elif 'open command prompt' in query or 'open CMD' in query or 'open c m d' in query:
            speak('opening CMD')
            os.system('start cmd')

        elif 'open camera' in query:
            pyautogui.moveTo(767,1045)
            pyautogui.click()
            pyautogui.sleep(2)
            pyautogui.write("camera")
            pyautogui.sleep(2)
            keyboard.press("Enter")

        elif 'open facebook' in query:
            speak('opening facebook')
            webbrowser.open('facebook.com')

        elif 'open map' in query or 'open maps' in query:
            speak('opening maps')
            webbrowser.open('https://www.google.com//maps/@28.5791035,77.4364433,16z')           
        
        elif 'voice call' in query:
            print('to whom you want to call')
            speak('to whom you want to call')
            caller = takeCommand()
            os.startfile('C:\\Users\\kravi\\AppData\\Local\\WhatsApp\\WhatsApp.exe')
            pyautogui.sleep(11)
            pyautogui.moveTo(31,130)
            pyautogui.sleep(1)
            pyautogui.click()
            pyautogui.sleep(1)
            pyautogui.write(caller)
            pyautogui.sleep(1)
            pyautogui.moveTo(35,291)
            pyautogui.sleep(1)
            pyautogui.click()
            pyautogui.sleep(1)
            pyautogui.moveTo(1722,62)
            pyautogui.sleep(1)
            pyautogui.click()
        elif 'video call' in query:
            print('to whom you want to call')
            speak('to whom you want to call')
            caller = takeCommand()
            os.startfile('C:\\Users\\kravi\\AppData\\Local\\WhatsApp\\WhatsApp.exe')
            pyautogui.sleep(11)
            pyautogui.moveTo(31,130)
            pyautogui.sleep(1)
            pyautogui.click()
            pyautogui.sleep(1)
            pyautogui.write(caller)
            pyautogui.sleep(1)
            pyautogui.moveTo(35,291)
            pyautogui.sleep(1)
            pyautogui.click()
            pyautogui.sleep(1)
            pyautogui.moveTo(1661,68)
            pyautogui.sleep(1)
            pyautogui.click()
        
        elif 'open google' in query:
            speak('opening google')
            webbrowser.open('google.com')
        elif 'open chrome' in query:
            speak('opening google chrome')
            os.startfile('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')

        elif 'website' in query:
            query = query.replace(" ","")
            query = query.replace("launch","")
            query = query.replace("website","")
            query = query.replace("open","")
            query = query.replace("jarvis","")
            web = 'https://www.' + query + '.com'
            webbrowser.open(web)
            speak('done sir')
        elif 'launch' in query:
            query = query.replace(" ","")
            query = query.replace("launch","")
            query = query.replace("website","")
            query = query.replace("open","")
            query = query.replace("jarvis","")
            web = 'https://www.' + query + '.com'
            webbrowser.open(web)
            speak('done sir')
        elif 'google search' in query:
                    speak('this is what i found on the web')
                    query = query.replace('google', '')
                    query = query.replace('search', '')
                    query = query.replace('jarvis', '')
                    pywhatkit.search(query)

                    try:
                            result = googleScrap.summary(query,4)
                            print(result)
                            speak(result)
                            keyboard.press_and_release("Alt + Tab")

                    except:
                        print('no speakable data available')
                        speak('no speakable data available')

        elif 'you need a break' in query or 'sleep' in query or 'silent' in query or 'quit' in query or 'quite' in query:
            speak('Ok sir, you can call me anythime.')
            break

        elif 'note' in query or 'remember' in query:
            rememberMsg = query.replace("jarvis","")
            rememberMsg = rememberMsg.replace("note that","")
            rememberMsg = rememberMsg.replace("remember","")
            print('you tell me to note that "'+rememberMsg+'"')
            speak('you tell me to note that "'+rememberMsg+'"')
            remember = open('jarvis_note.txt','w')
            remember.write(rememberMsg)
            remember.close()

        elif 'volume up' in query:
            pyautogui.press('volumeup')
        elif 'volume down' in query:
            pyautogui.press('volumedown')
        elif 'volume mute' in query:
            pyautogui.press('volumemute')
        
        elif 'refresh' in query:
            speak('please wait a second')
            itref()

        elif 'shutdown' in query or 'sundown' in query or 'down' in query:
            print("Restarting")
            speak("Restarting")
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            print("Restarting")
            speak("Restarting")
            os.system("shutdown /r /t 1")


        elif 'exit jarvis' in query or 'bye jarvis' in query or 'exit' in query or 'bye' in query or 'sleep' in query:
            speak('bye sir')
            speak('quitting this session')
            quit()

# I STARTED MAKING THIS __JARVIS__ FROM 16TH NOVEMBER 2021