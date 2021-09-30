from playsound import playsound
from gtts import gTTS

def playaudio(audio):
    playsound(audio)

def Speak(text):
    text_2=str(text)
    print(text_2)
    audio = gTTS(text_2)
    audio.save('D:\\simple-AI\\Audio\\robot.mp3')
    playaudio('D:\\simple-AI\\Audio\\robot.mp3') 

'''from AI_Robot_Tools import AI_Speak

def Speak(text):
    AI_Speak.Speak(0,150,text)'''