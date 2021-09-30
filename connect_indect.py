import pyautogui as pt
import pyttsx3

try:
    from Jarvis_Main import Task_Start
except:
    print('please connetc internet.')

def StartSpeak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # print(voices[0].id)
    engine.setProperty('voices', voices[0].id)
    engine.setProperty('rate', 150)
    engine.say(text)
    #print(Text)
    engine.runAndWait()
def Connect():
    if pt.locateCenterOnScreen("D:\simple-AI\img\connectinternet.png",confidence=.8,grayscale=True):
        pt.sleep(2.5)
        pt.locateCenterOnScreen("D:\simple-AI\img\connectinternet.png",confidence=.8,grayscale=True)
        pt.sleep(10) 
        StartSpeak('Sessfully Connect Internet ! Please Wait Data Loading')
        Task_Start() 
    else:
        try:
            Task_Start()
        except:     
            print('not connect')    
