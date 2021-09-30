try:
    from Jarvis_Main import Task_Start
except:
    print('please connetc internet.')

import keyboard
import pyttsx3
import datetime
import time
import connect_indect
try:
    import speech_recognition as sr
except:
    print('error')    

def AI_2Speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # print(voices[0].id)
    engine.setProperty('voices', voices[0].id)
    engine.setProperty('rate', 150)
    engine.say(text)
    #print(Text)
    engine.runAndWait()

Current_Time=time.strftime("%I:%M %p")
Current_Date=today = datetime.date.today()

NonePass=""

def AI_AI_Wish_Time_Date(
    morning=Current_Time,
    afternoon=Current_Time,
    evening=Current_Time,
    night=Current_Time,
    Time_Show=NonePass,
    Date_Show=NonePass,
    otherText=NonePass
    ):## AI_Wish_Time_Date(morning=f"{Current_Date} {Current_Time}",afternoon=f"Afternoon The Time Is {Current_Time}",otherText="My Name is Rishabh")
    hour = int(datetime.datetime.now().hour)

    if 4 <= hour <=11:
        return (f"{morning} {Time_Show} {otherText} {Date_Show}")
    elif 12 <= hour <= 17:
        return (f"{afternoon} {Time_Show} {otherText} {Date_Show}")
    elif 18 <= hour <= 22:
        return (f"{evening} {Time_Show} {otherText} {Date_Show}")       
    else:
        return (f"{night} {Time_Show} {otherText} {Date_Show}")

def AI_SpeechRecognition_English():

    try:

        r = sr.Recognizer()
        
        r.pause_threshold = 0.8
        print("Listening...")
        with sr.Microphone() as source:
            audio = r.listen(source,4,4)
        try:
            print("Recognizing..")
            query = r.recognize_google(audio,language='eng-in')
            print(f"You Said : {query}")
        
        except:
            return AI_SpeechRecognition_English()

        query = str(query).lower()
        return query

    except:
        return AI_SpeechRecognition_English()   
def Main_Start():
    keyboard.press_and_release('win+m')
    try:
        Task_Start() 
    except:
        jarvis_intro='''Hay I am Jarvis. Are you Rishabh Sir?'''
        AI_2Speak(AI_AI_Wish_Time_Date(f'Good Morning ! {jarvis_intro}',f'Good Afternoon ! {jarvis_intro}',f'Good Evening ! {jarvis_intro}',f'Good Night ! {jarvis_intro}'))
        AI_2Speak('please connetc internet.')
        while True:
            try:
                Task_Start()
            except:
                connect_indect.Connect()      

Main_Start()
