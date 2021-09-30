from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import speech_recognition as sr 
from playsound import playsound
from gtts import gTTS
from Speak_AI import Speak
import os

chatbot=ChatBot('Jarvis')

convertation=open('English_Chatbot_data.txt', 'r',  errors='ignore').readlines()
trainer=ListTrainer(chatbot)
trainer.train(convertation)

'''trainer5=ChatterBotCorpusTrainer(chatbot)
trainer5.train('chatterbot.corpus.english')
trainer5.train('chatterbot.corpus.hindi')'''


def playaudio(audio):
    playsound(audio) 

def Speak(text,RobotReplay):
    text_2=str(text)
    audio = gTTS(text_2)
    audio.save(f'D:\\simple-AI\\Audio\\{RobotReplay}.mp3')
    playaudio(f'D:\\simple-AI\\Audio\\{RobotReplay}.mp3') 
    

def AI_English_ChatBot(command):
    response_replay = chatbot.get_response(command) 
    Speak(text=response_replay,RobotReplay=command)
    os.remove(f'D:\\simple-AI\\Audio\\{command}.mp3')

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


'''while True:
    try:
        query=AI_SpeechRecognition_English()
        ans=AI_English_ChatBot(query)
        aa=print(ans)
        Speak(text=ans,RobotReplay=query)
        os.remove(f'D:\\simple-AI\\Audio\\{query}.mp3')
    except:
        print('error')'''