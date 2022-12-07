import os
import speech_recognition as sr

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

        return 'None'

    return query

while True:
    i = 0
    while True:
        wake_Up = takeCommand()
        if i==0:
            if 'wake up' in wake_Up:
                os.startfile('C:\\Users\\kravi\\Desktop\\School\\DEO\\programing_deo\\JARVIS\\JARVIS.py')
            elif 'Jarvis' in wake_Up:
                os.startfile('C:\\Users\\kravi\\Desktop\\School\\DEO\\programing_deo\\JARVIS\\JARVIS.py')
        elif i>0:
            if 'wake up' in wake_Up:
                os.startfile('C:\\Users\\kravi\\Desktop\\School\\DEO\\programing_deo\\JARVIS\\JARVIS_S.py')
            elif 'Jarvis' in wake_Up:
                os.startfile('C:\\Users\\kravi\\Desktop\\School\\DEO\\programing_deo\\JARVIS\\JARVIS_S.py')
        i+=1