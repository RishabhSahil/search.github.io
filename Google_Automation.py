from PC_Automation import ChromeAuto
from AI_Robot_Tools import AI_Speech_Recognition
from Speak_AI import Speak
import speech_recognition as sr 

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

while True:
    try:
        query_2=AI_SpeechRecognition_English()
        ChromeAuto(query_2)
    except:
        print('error')    
   